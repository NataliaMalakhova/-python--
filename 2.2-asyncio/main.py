import aiohttp
import asyncpg
import asyncio

API_URL = "https://swapi.dev/api/people/"


async def fetch_total_characters(session):
    """Получаем общее количество персонажей из API"""
    async with session.get(API_URL) as response:
        data = await response.json()
        return data['count']


async def fetch_character(session, character_id):
    """Получаем данные персонажа по ID"""
    try:
        async with session.get(f"{API_URL}{character_id}/") as response:
            if response.status == 200:
                character_data = await response.json()
                character_data['id'] = character_id  # Добавляем id в данные персонажа
                return character_data
            else:
                print(f"Failed to fetch character {character_id}: Status {response.status}")
                return None
    except aiohttp.ClientError as e:
        print(f"Error fetching character {character_id}: {e}")
        return None


async def save_character(pool, character):
    """Сохраняем данные персонажа в базу данных"""
    if not character:
        return

    async with pool.acquire() as conn:
        films = ", ".join([film.split('/')[-2] for film in character.get('films', [])])
        species = ", ".join([spec.split('/')[-2] for spec in character.get('species', [])])
        starships = ", ".join([ship.split('/')[-2] for ship in character.get('starships', [])])
        vehicles = ", ".join([vehicle.split('/')[-2] for vehicle in character.get('vehicles', [])])

        try:
            await conn.execute('''
                INSERT INTO characters (id, birth_year, eye_color, films, gender, hair_color,
                                        height, homeworld, mass, name, skin_color, species,
                                        starships, vehicles) VALUES ($1, $2, $3, $4, $5, $6,
                                        $7, $8, $9, $10, $11, $12, $13, $14)
            ''', character['id'], character.get('birth_year', ''), character.get('eye_color', ''), films,
                           character.get('gender', ''), character.get('hair_color', ''), character.get('height', ''),
                           character.get('homeworld', ''), character.get('mass', ''), character.get('name', ''),
                           character.get('skin_color', ''), species, starships, vehicles)
        except asyncpg.PostgresError as e:
            print(f"Failed to save character {character['id']}: {e}")


async def main():
    pool = await asyncpg.create_pool(user='postgres', password='1234',
                                     database='sw_db', host='localhost')

    async with aiohttp.ClientSession() as session:
        # Получаем общее количество персонажей
        total_characters = await fetch_total_characters(session)

        tasks = []
        sem = asyncio.Semaphore(10)  # Ограничиваем количество одновременных запросов

        async def fetch_and_save(character_id):
            async with sem:  # Контроль количества запросов
                character_data = await fetch_character(session, character_id)
                await save_character(pool, character_data)

        # Запускаем загрузку и сохранение всех персонажей
        for character_id in range(1, total_characters + 1):
            tasks.append(fetch_and_save(character_id))

        await asyncio.gather(*tasks)

    await pool.close()

if __name__ == "__main__":
    asyncio.run(main())

import aiohttp
import asyncpg
import asyncio
import random

API_URL = "https://swapi.dev/api/people/"


async def fetch_total_characters(session):
    """Получаем общее количество персонажей из API"""
    async with session.get(API_URL) as response:
        data = await response.json()
        return data['count']


async def fetch_character(session, character_id):
    """Получаем данные персонажа по ID с добавлением случайной задержки"""
    # Добавляем случайную задержку перед запросом
    await asyncio.sleep(random.uniform(0.5, 2.0))

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


async def fetch_name_from_url(session, url):
    """Получаем название объекта (фильм, вид, корабль, транспорт, планета) по ссылке с задержкой"""
    if not url:
        return None

    # Добавляем случайную задержку перед запросом
    await asyncio.sleep(random.uniform(0.5, 2.0))

    try:
        async with session.get(url) as response:
            if response.status == 200:
                data = await response.json()
                return data.get('title') or data.get('name')  # 'title' для фильмов, 'name' для остальных
            else:
                print(f"Failed to fetch data from {url}: Status {response.status}")
                return None
    except aiohttp.ClientError as e:
        print(f"Error fetching data from {url}: {e}")
        return None


async def save_character(pool, character, session):
    """Сохраняем данные персонажа в базу данных, обновляем если существует"""
    if not character:
        return

    async with pool.acquire() as conn:
        # Получаем названия фильмов
        films = ", ".join([name for name in await asyncio.gather(
            *[fetch_name_from_url(session, film) for film in character.get('films', [])]) if name])

        # Получаем названия видов (species)
        species = ", ".join([name for name in await asyncio.gather(
            *[fetch_name_from_url(session, spec) for spec in character.get('species', [])]) if name])

        # Получаем названия кораблей (starships)
        starships = ", ".join([name for name in await asyncio.gather(
            *[fetch_name_from_url(session, ship) for ship in character.get('starships', [])]) if name])

        # Получаем названия транспорта (vehicles)
        vehicles = ", ".join([name for name in await asyncio.gather(
            *[fetch_name_from_url(session, vehicle) for vehicle in character.get('vehicles', [])]) if name])

        # Получаем название планеты
        homeworld = await fetch_name_from_url(session, character.get('homeworld'))

        try:
            # Используем INSERT с ON CONFLICT для предотвращения дублирования записей
            await conn.execute('''
                INSERT INTO characters (id, birth_year, eye_color, films, gender, hair_color,
                                        height, homeworld, mass, name, skin_color, species,
                                        starships, vehicles) 
                VALUES ($1, $2, $3, $4, $5, $6, $7, $8, $9, $10, $11, $12, $13, $14)
                ON CONFLICT (id) DO UPDATE SET
                    birth_year = EXCLUDED.birth_year,
                    eye_color = EXCLUDED.eye_color,
                    films = EXCLUDED.films,
                    gender = EXCLUDED.gender,
                    hair_color = EXCLUDED.hair_color,
                    height = EXCLUDED.height,
                    homeworld = EXCLUDED.homeworld,
                    mass = EXCLUDED.mass,
                    name = EXCLUDED.name,
                    skin_color = EXCLUDED.skin_color,
                    species = EXCLUDED.species,
                    starships = EXCLUDED.starships,
                    vehicles = EXCLUDED.vehicles;
            ''', character['id'], character.get('birth_year', ''), character.get('eye_color', ''), films,
                               character.get('gender', ''), character.get('hair_color', ''),
                               character.get('height', ''),
                               homeworld, character.get('mass', ''), character.get('name', ''),
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
                await save_character(pool, character_data, session)

        # Запускаем загрузку и сохранение всех персонажей
        for character_id in range(1, total_characters + 1):
            tasks.append(fetch_and_save(character_id))

        await asyncio.gather(*tasks)

    await pool.close()


if __name__ == "__main__":
    asyncio.run(main())

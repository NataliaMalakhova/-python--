import asyncpg
import asyncio


async def migrate_db():
    conn = await asyncpg.connect(user='postgres', password='1234',
                                 database='sw_db', host='localhost')

    await conn.execute('''
        CREATE TABLE IF NOT EXISTS characters (
            id SERIAL PRIMARY KEY,
            birth_year VARCHAR,
            eye_color VARCHAR,
            films TEXT,
            gender VARCHAR,
            hair_color VARCHAR,
            height VARCHAR,
            homeworld VARCHAR,
            mass VARCHAR,
            name VARCHAR,
            skin_color VARCHAR,
            species TEXT,
            starships TEXT,
            vehicles TEXT
        )
    ''')

    await conn.close()


if __name__ == "__main__":
    asyncio.run(migrate_db())

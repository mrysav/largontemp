import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.environ['DATABASE_URL']

conn = psycopg2.connect(DATABASE_URL, sslmode='require')
cur = conn.cursor()

cur.execute("""
    CREATE TABLE largon_temps (
        id SERIAL,
        time timestamp,
        outside integer,
        living_room integer,
        bathroom integer,
        kitchen integer
    )
""")

conn.commit()

conn.close()
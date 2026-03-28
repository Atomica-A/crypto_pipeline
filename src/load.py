import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

def get_connection():
    return psycopg2.connect(
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD")
    )

def create_table():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS crypto_prices (
            id SERIAL PRIMARY KEY,
            coin VARCHAR(50),
            price_usd NUMERIC,
            change_24h NUMERIC,
            last_updated TIMESTAMP
        )
    """)
    conn.commit()
    cur.close()
    conn.close()
    print("Table ready")

def insert_data(df):
    conn = get_connection()
    cur = conn.cursor()
    for _, row in df.iterrows():
        cur.execute("""
            INSERT INTO crypto_prices (coin, price_usd, change_24h, last_updated)
            VALUES (%s, %s, %s, %s)
        """, (row["coin"], row["price_usd"], row["change_24h"], row["last_updated"]))
    conn.commit()
    cur.close()
    conn.close()
    print(f"Inserted {len(df)} rows into PostgreSQL")

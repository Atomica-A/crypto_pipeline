import time
from src.extract import fetch_crypto_prices
from src.transform import transform_crypto_data
from src.load import create_table, insert_data

def run():
    print("Starting Crypto ETL Pipeline...")
    create_table()

    while True:
        print("\nFetching new data...")
        raw_data = fetch_crypto_prices()

        if raw_data:
            df = transform_crypto_data(raw_data)
            insert_data(df)
            print("Waiting 60 seconds...")
        else:
            print("Skipping insert due to API error")

        time.sleep(60)

if __name__ == "__main__":
    run()

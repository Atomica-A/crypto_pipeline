import pandas as pd
from datetime import datetime

def transform_crypto_data(raw_data):
    rows = []

    for coin, values in raw_data.items():
        rows.append({
            "coin": coin,
            "price_usd": values.get("usd"),
            "change_24h": values.get("usd_24h_change"),
            "last_updated": datetime.utcnow()
        })

    df = pd.DataFrame(rows)
    print(f"Transformed {len(df)} coins")
    print(df)
    return df

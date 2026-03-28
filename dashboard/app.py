import streamlit as st
import pandas as pd
import psycopg2
import os
from dotenv import load_dotenv
import time

load_dotenv()

def get_connection():
    return psycopg2.connect(
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD")
    )

def fetch_latest_prices():
    conn = get_connection()
    df = pd.read_sql("""
        SELECT DISTINCT ON (coin) coin, price_usd, change_24h, last_updated
        FROM crypto_prices
        ORDER BY coin, last_updated DESC
    """, conn)
    conn.close()
    return df

def fetch_price_history(coin):
    conn = get_connection()
    df = pd.read_sql("""
        SELECT last_updated, price_usd
        FROM crypto_prices
        WHERE coin = %s
        ORDER BY last_updated ASC
    """, conn, params=(coin,))
    conn.close()
    return df

# Dashboard layout
st.set_page_config(page_title="Crypto Dashboard", layout="wide")
st.title("📈 Real-Time Crypto Price Dashboard")
st.caption("Auto-refreshes every 60 seconds")

# Latest prices
df = fetch_latest_prices()

col1, col2, col3, col4 = st.columns(4)
cols = [col1, col2, col3, col4]

for i, row in df.iterrows():
    change = round(row["change_24h"], 2)
    arrow = "🟢" if change >= 0 else "🔴"
    cols[i].metric(
        label=row["coin"].upper(),
        value=f"${row['price_usd']:,.2f}",
        delta=f"{change}%"
    )

st.divider()

# Price history chart
st.subheader("Price History")
selected_coin = st.selectbox("Select Coin", df["coin"].tolist())
history_df = fetch_price_history(selected_coin)
st.line_chart(history_df.set_index("last_updated")["price_usd"])

# Raw data table
st.subheader("Latest Data")
st.dataframe(df, use_container_width=True)

# Auto refresh
time.sleep(60)
st.rerun()

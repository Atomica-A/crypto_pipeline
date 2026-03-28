# Real-Time Crypto Price Pipeline + Dashboard

A real-time data pipeline that fetches live cryptocurrency prices from CoinGecko API, stores them in PostgreSQL every 60 seconds, and visualizes the data on a live Streamlit dashboard.

## Project Structure
```
crypto-pipeline/
├── src/
│   ├── extract.py      # Fetch from CoinGecko API
│   ├── transform.py    # Clean and structure data
│   └── load.py         # Insert into PostgreSQL
├── dashboard/
│   └── app.py          # Streamlit live dashboard
├── main.py             # Pipeline runner
├── run_pipeline.sh     # Bash scheduler
├── requirements.txt    # Dependencies
└── README.md
```

## Features
- Fetches live prices for Bitcoin, Ethereum, Solana and BNB
- Stores price history in PostgreSQL every 60 seconds
- Live dashboard with price metrics and charts
- Auto-refreshes every 60 seconds

## Setup

1. Clone the repo
```bash
   git clone https://github.com/yourusername/crypto-pipeline.git
   cd crypto-pipeline
```
2. Create virtual environment
```bash
   python -m venv venv
   source venv/bin/activate
```
3. Install dependencies
```bash
   pip install -r requirements.txt
```
4. Copy `.env.example` to `.env` and fill in your PostgreSQL credentials
```bash
   cp .env.example .env
```
5. Create the database
```bash
   psql -U your_postgres_username -c "CREATE DATABASE cryptodb;"
```

## Run the Pipeline
```bash
python main.py
```

## Run the Dashboard
```bash
streamlit run dashboard/app.py
```
Opens at `http://localhost:8501`

## Tech Stack
- Python
- CoinGecko API
- PostgreSQL
- Streamlit
- Bash
- Git

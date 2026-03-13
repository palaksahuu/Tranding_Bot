# Binance Futures Testnet Trading Bot

A Python CLI trading bot that places Market and Limit orders on Binance Futures Testnet.

## Features

- Market Orders
- Limit Orders
- BUY / SELL
- CLI interface
- Logging
- Input validation
- Exception handling
- Lightweight UI (Streamlit)

## Setup

1 Install dependencies

pip install -r requirements.txt

2 Create .env

BINANCE_API_KEY=your_api_key
BINANCE_API_SECRET=your_api_secret

3 Run CLI

python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001

4 Run UI

streamlit run app.py

## Logs

Logs are stored in:

logs/trading_bot.log
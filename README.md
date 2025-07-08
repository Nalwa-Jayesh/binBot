# Binance Futures Testnet Trading Bot

A Python trading bot for Binance USDT-M Futures Testnet. Supports market and limit orders, live price feed, and both CLI and Streamlit web interfaces.

## Features
- Place market and limit orders (buy/sell) on Binance Futures Testnet
- View live price feed for any symbol
- Command-line interface (CLI)
- Streamlit web app with live price sidebar
- Logging of all API requests and errors

## Requirements
- Python 3.8+
- Binance Futures Testnet API key and secret

## Setup
1. **Clone the repository**
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Create a `.env` file** in the project root:
   ```env
   API_KEY=your_binance_testnet_api_key
   API_SECRET=your_binance_testnet_api_secret
   ```

## Usage

### Command-Line Interface (CLI)
Run the CLI bot:
```bash
python main.py
```

#### Example: Place an Order
```
Binance Futures Testnet Trading Bot
Type 'order' to place an order, 'pricefeed' to view live price, or 'quit' to exit.

Enter command (order/pricefeed/quit): order
Symbol (BTCUSDT): BTCUSDT
Side (BUY/SELL): BUY
Order Type (MARKET/LIMIT): MARKET
Quantity: 0.001

ORDER DETAILS
========================================
orderId: 123456789
symbol: BTCUSDT
status: NEW
side: BUY
...
========================================
```

#### Example: View Live Price Feed
```
Enter command (order/pricefeed/quit): pricefeed
Symbol for live price (BTCUSDT): btcusdt
Streaming live price for BTCUSDT (Ctrl+C to stop)...
Live Price: 65000.12
Live Price: 65000.15
Live Price: 65000.10
...
```

#### Example: Quit
```
Enter command (order/pricefeed/quit): quit
```

### Streamlit Web App
Run the web app:
```bash
streamlit run app.py
```
- The sidebar shows the live price for any symbol (default: BTCUSDT)
- The main area lets you place market or limit orders
- Click 'Rerun' or press 'R' to refresh the live price

#### Example (UI):
- Enter a symbol in the sidebar to see the live price
- Fill out the order form and click "Place Order" to submit
- Order details and status will be shown below the form

## File Structure
- `main.py` — CLI for trading and live price feed
- `app/streamlit_app.py` — Streamlit web interface
- `bot/bot.py` — Core trading logic
- `bot/price_feed.py` — Live price feed logic
- `requirements.txt` — Python dependencies
- `.env` — Your API credentials (not committed)

## Notes
- This bot uses the Binance **Futures Testnet**. Do not use real funds.
- Make sure your API key is for the testnet and has the correct permissions.
- For more info, see the [Binance Futures Testnet Docs](https://binance-docs.github.io/apidocs/futures/en/).

## License
MIT 
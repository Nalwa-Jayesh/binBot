import streamlit as st
import os
from dotenv import load_dotenv
from bot.bot import BasicBot
from binance.um_futures import UMFutures

load_dotenv()

API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")

st.title("Binance Futures Testnet Trading Bot")

if not API_KEY or not API_SECRET:
    st.error("API_KEY and/or API_SECRET not found in .env file. Please set them and restart the app.")
    st.stop()

bot = BasicBot(API_KEY, API_SECRET)

# --- Live Price in Sidebar ---
sidebar = st.sidebar
sidebar.header("Live Price")
live_symbol = sidebar.text_input("Symbol for Live Price", value="BTCUSDT").upper()

client = UMFutures(key=API_KEY, secret=API_SECRET, base_url="https://testnet.binancefuture.com")
try:
    ticker = client.ticker_price(symbol=live_symbol)
    live_price = ticker['price']
    sidebar.success(f"{live_symbol}: {live_price}")
except Exception:
    sidebar.warning(f"Could not fetch live price for {live_symbol}")

sidebar.write("(Click 'Rerun' or press R to refresh price)")

# --- Main Order Form ---
st.header("Place an Order")
order_symbol = st.text_input("Symbol", value="BTCUSDT").upper()
side = st.selectbox("Side", ["BUY", "SELL"])
order_type = st.selectbox("Order Type", ["MARKET", "LIMIT"])
qty = st.number_input("Quantity", min_value=0.0001, step=0.0001, format="%f")

price = None
if order_type == "LIMIT":
    price = st.number_input("Limit Price", min_value=0.0, step=0.01, format="%f")

if st.button("Place Order"):
    if order_type == "MARKET":
        order = bot.place_market_order(order_symbol, side, qty)
    elif order_type == "LIMIT":
        order = bot.place_limit_order(order_symbol, side, qty, price)
    else:
        order = None
        st.error("Unsupported order type.")
    if order:
        st.success("Order placed successfully!")
        st.json(order)
    else:
        st.error("Order failed. Check logs for details.") 
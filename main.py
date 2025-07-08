from bot.bot import BasicBot
from dotenv import load_dotenv
import os
import sys

load_dotenv()

API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")

if not API_KEY or not API_SECRET:
    print("Error: API_KEY and/or API_SECRET not found in .env file.")
    sys.exit(1)

bot = BasicBot(API_KEY, API_SECRET)

symbol = input("Symbol (BTCUSDT): ").upper()
side = input("Side (BUY/SELL): ").upper()
order_type = input("Order Type (MARKET/LIMIT): ").upper()
qty = float(input("Quantity: "))

order = None
if order_type == "MARKET":
    order = bot.place_market_order(symbol, side, qty)
elif order_type == "LIMIT":
    price = float(input("Limit Price: "))
    order = bot.place_limit_order(symbol, side, qty, price)
else:
    print("Unsupported order type. Please use MARKET or LIMIT.")

bot.print_order(order) 
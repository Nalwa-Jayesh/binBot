import logging
from binance.um_futures import UMFutures

class BasicBot:
    def __init__(self, api_key, api_secret, testnet=True):
        base_url = "https://testnet.binancefuture.com" if testnet else None
        self.client = UMFutures(key=api_key, secret=api_secret, base_url=base_url)
        self.setup_logging()

    def setup_logging(self):
        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s - %(levelname)s - %(message)s",
            handlers=[
                logging.FileHandler("trading_bot.log"),
                logging.StreamHandler()
            ]
        )
        self.logger = logging.getLogger(__name__)

    def place_market_order(self, symbol, side, quantity):
        try:
            order = self.client.new_order(symbol=symbol, side=side, type="MARKET", quantity=quantity)
            self.logger.info(f"Market order placed: {order}")
            return order
        except Exception as e:
            self.logger.error(f"Error placing market order: {e}")
            return None

    def place_limit_order(self, symbol, side, quantity, price):
        try:
            order = self.client.new_order(symbol=symbol, side=side, type="LIMIT", quantity=quantity, price=price, timeInForce="GTC")
            self.logger.info(f"Limit order placed: {order}")
            return order
        except Exception as e:
            self.logger.error(f"Error placing limit order: {e}")
            return None

    def print_order(self, order):
        if not order:
            print("Order failed or not placed.")
            return
        print("\nORDER DETAILS")
        print("=" * 40)
        for k, v in order.items():
            print(f"{k}: {v}")
        print("=" * 40)

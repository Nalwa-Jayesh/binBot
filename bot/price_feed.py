import time
import json
from binance.websocket.um_futures.websocket_client import UMFuturesWebsocketClient

def start_price_stream(symbol="btcusdt"):
    def handle_msg(_, msg):
        if isinstance(msg, str):
            msg = json.loads(msg)
        if 'c' in msg:
            print(f"Live Price: {msg['c']}")
        # else: silently ignore messages without 'c'

    ws_client = UMFuturesWebsocketClient(on_message=handle_msg)
    ws_client.ticker(symbol=symbol)
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Stopping price stream...")
        ws_client.stop()

def get_latest_price(symbol="btcusdt", timeout=5):
    latest_price = {"price": None}
    def handle_msg(_, msg):
        if isinstance(msg, str):
            msg = json.loads(msg)
        if 'c' in msg:
            latest_price["price"] = msg['c']

    ws_client = UMFuturesWebsocketClient(on_message=handle_msg)
    ws_client.ticker(symbol=symbol)
    # Wait for a price or timeout
    start = time.time()
    while latest_price["price"] is None and (time.time() - start) < timeout:
        time.sleep(0.1)
    ws_client.stop()
    return latest_price["price"]

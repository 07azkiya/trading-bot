from binance.client import Client

class BinanceClient:
    def __init__(self, api_key, api_secret):
        self.client = Client(api_key, api_secret, testnet=True)
        self.client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"

    def create_order(self, **params):
        return self.client.futures_create_order(**params)

    def get_price(self, symbol):
        ticker = self.client.futures_symbol_ticker(symbol=symbol)
        return float(ticker["price"])
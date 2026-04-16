class OrderManager:
    def __init__(self, client):
        self.client = client

    def market_order(self, symbol, side, quantity):
        return self.client.client.create_order(
            symbol=symbol,
            side=side.upper(),
            type="MARKET",
            quantity=quantity
        )

    def limit_order(self, symbol, side, quantity, price):
        return self.client.client.create_order(
            symbol=symbol,
            side=side.upper(),
            type="LIMIT",
            timeInForce="GTC",
            quantity=quantity,
            price=str(price)
        )
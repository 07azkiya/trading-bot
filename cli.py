import sys

from bot.client import BinanceClient
from bot.validators import validate_symbol, validate_side, validate_quantity
from bot.orders import OrderManager
from bot.risk import RiskManager
from bot.logger import log
from bot.journal import Journal


API_KEY = "YOUR_API_KEY"
API_SECRET = "YOUR_API_SECRET"


def main():
    if len(sys.argv) != 6:
        print("Usage:")
        print("python cli.py place SYMBOL SIDE TYPE QUANTITY")
        print("Example:")
        print("python cli.py place BTCUSDT BUY MARKET 0.001")
        return

    _, command, symbol, side, order_type, qty = sys.argv

    if command.lower() != "place":
        print("Only 'place' command supported")
        return

    client = BinanceClient(API_KEY, API_SECRET)
    orders = OrderManager(client)
    risk = RiskManager(max_trade_usdt=20)
    journal = Journal()

    symbol = validate_symbol(symbol)
    side = validate_side(side)
    qty = validate_quantity(qty)

    price = client.get_price(symbol)

    try:
        risk.check_risk(qty, price)

        if order_type.upper() == "MARKET":
            order = orders.market_order(symbol, side, qty)
        else:
            price_input = float(input("Limit Price: "))
            order = orders.limit_order(symbol, side, qty, price_input)

        log(f"ORDER PLACED: {order}")
        journal.save(order)

        print("\n✅ SUCCESS")
        print(order)

    except Exception as e:
        print("\n❌ ERROR:", e)


if __name__ == "__main__":
    main()
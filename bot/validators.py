def validate_symbol(symbol: str):
    symbol = symbol.upper().strip()
    if not symbol.endswith("USDT"):
        raise ValueError("Only USDT pairs allowed (e.g., BTCUSDT)")
    return symbol


def validate_side(side: str):
    side = side.lower().strip()
    if side not in ["buy", "sell"]:
        raise ValueError("side must be 'buy' or 'sell'")
    return side


def validate_type(order_type: str):
    order_type = order_type.lower().strip()
    if order_type not in ["market", "limit"]:
        raise ValueError("order_type must be 'market' or 'limit'")
    return order_type


def validate_quantity(quantity):
    try:
        quantity = float(quantity)
        if quantity <= 0:
            raise ValueError()
        return quantity
    except:
        raise ValueError("quantity must be a positive number")
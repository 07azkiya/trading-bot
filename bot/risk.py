class RiskManager:
    def __init__(self, max_notional=100):
        self.max_notional = max_notional

    def check(self, price, quantity):
        if price is None:
            return  # MARKET orders may not have price

        notional = price * quantity

        if notional > self.max_notional:
            raise ValueError(
                f"Risk limit exceeded: {notional} > {self.max_notional}"
            )
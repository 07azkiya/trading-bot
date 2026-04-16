import json
from datetime import datetime

FILE = "trades.json"


def log_trade(data):
    try:
        try:
            with open(FILE, "r") as f:
                trades = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            trades = []

        data["timestamp"] = datetime.now().isoformat()
        trades.append(data)

        with open(FILE, "w") as f:
            json.dump(trades, f, indent=4)

    except Exception as e:
        print(f"Journal error: {e}")
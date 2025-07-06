# hansei_writer.py

import json
from datetime import datetime
import os

HANSEI_FILE = "hansei_log.json"

def log_trade(symbol, direction, entry_price, exit_price, result, notes=""):
    trade_data = {
        "timestamp": datetime.utcnow().isoformat(),
        "symbol": symbol,
        "direction": direction,
        "entry_price": entry_price,
        "exit_price": exit_price,
        "result": result,
        "notes": notes
    }

    # Lue aiempi data jos olemassa
    if os.path.exists(HANSEI_FILE):
        with open(HANSEI_FILE, "r") as file:
            try:
                data = json.load(file)
            except json.JSONDecodeError:
                data = []
    else:
        data = []

    # Lisää uusi merkintä
    data.append(trade_data)

    # Kirjoita takaisin tiedostoon
    with open(HANSEI_FILE, "w") as file:
        json.dump(data, file, indent=4)

    print(f"[HANSEI] Trade logged: {trade_data}")

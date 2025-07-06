import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from mcp_agent.hansei_writer import log_trade

# Tämä testikutsu kirjaa yhden esimerkkitreidin hansei_log.json -tiedostoon
def test_log_trade():
    log_trade(
        symbol="EURUSD",
        direction="BUY",
        entry_price=1.0860,
        exit_price=1.0901,
        result="WIN",
        notes="Testitreidi strategiatesteristä"git 
    )

# Suoritetaan testi heti kun tiedosto ajetaan
if __name__ == "__main__":
    test_log_trade()

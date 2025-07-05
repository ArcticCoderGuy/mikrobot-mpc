# test_parser.py
# Simple unit test for signal_parser

from mcp_agent.signal_parser import parse_signal

def test_parse_signal():
    raw = {
        "symbol": "eurusd",
        "direction": "buy",
        "entry_price": "1.0880",
        "sl": "1.0850",
        "tp": "1.0930",
        "timestamp": "2025-07-05T15:30:00Z"
    }

    parsed = parse_signal(raw)
    assert parsed["symbol"] == "EURUSD"
    assert parsed["direction"] == "BUY"

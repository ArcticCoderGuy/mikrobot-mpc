# signal_parser.py

def parse_signal(raw_signal):
    """
    Normalize a raw signal dictionary into a standard format.
    
    Args:
        raw_signal (dict): Incoming signal, possibly from email, webhook, etc.
        
    Returns:
        dict: Clean and validated signal with required fields.
    """

    # Extract and sanitize values — provide default fallback values if missing
    symbol = raw_signal.get("symbol", "").upper()             # e.g. "EURUSD"
    direction = raw_signal.get("direction", "").upper()       # e.g. "BUY" or "SELL"
    entry_price = float(raw_signal.get("entry_price", 0))     # Entry level for order
    stop_loss = float(raw_signal.get("sl", 0))                # Stop Loss
    take_profit = float(raw_signal.get("tp", 0))              # Take Profit
    timestamp = raw_signal.get("timestamp", "N/A")            # When the signal was generated

    # You could add validation here to ensure these values are non-zero etc.

    return {
        "symbol": symbol,
        "direction": direction,
        "entry_price": entry_price,
        "sl": stop_loss,
        "tp": take_profit,
        "timestamp": timestamp
    }

# decision_engine.py
# This module decides whether to execute a trade or not, based on filtering and ML (future)

def evaluate_signal(signal: dict) -> str:
    """
    Decides if a signal should be passed to the EA.
    Return values: "EXECUTE", "IGNORE"
    """
    # Dummy logic, to be replaced with rules or ML
    if signal.get("direction") in ["BUY", "SELL"]:
        return "EXECUTE"
    return "IGNORE"

def make_decision(signal: dict) -> str:
    """
    Dummy decision engine. Decides whether to 'EXECUTE', 'IGNORE', or 'LOG' the signal.
    Currently just executes all valid signals.
    """
    # Example logic: if direction is BUY or SELL, execute it
    if signal.get('direction') in ['BUY', 'SELL']:
        return "EXECUTE"
    return "IGNORE"


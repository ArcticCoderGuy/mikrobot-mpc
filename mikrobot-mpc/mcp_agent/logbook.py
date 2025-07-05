# logbook.py
# Responsible for logging trades or rejected signals

def log_signal(signal: dict, status: str):
    """
    Logs signal processing outcome. Status can be 'accepted', 'rejected', etc.
    """
    print(f"[LOG] Signal status: {status} | {signal}")

def log_event(event_type: str, message: str) -> None:
    """
    Logs an event with a simple print statement.
    Can be expanded to log into a file or external service.
    """
    print(f"[{event_type}] {message}")

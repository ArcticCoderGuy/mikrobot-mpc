def is_valid_signal(signal: dict) -> bool:
    """
    Dummy validation logic — replace with your own signal validation.
    Returns True if signal contains 'symbol' and 'direction'.
    """
    return 'symbol' in signal and 'direction' in signal

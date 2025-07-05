# main.py

# Import the dotenv loader to read environment variables from a .env file
from dotenv import load_dotenv
import os

# Import core components of the MCP agent
from mcp_agent.signal_parser import parse_signal          # Handles formatting and extracting relevant info from the signal
from mcp_agent.filter_engine import is_valid_signal       # Checks if the signal meets trading criteria
from mcp_agent.decision_engine import make_decision       # Decides whether to execute, ignore, or log the signal
from mcp_agent.relay_to_kafka import send_to_kafka        # Sends the final signal to a Kafka topic
from mcp_agent.logbook import log_event                   # Logs events for traceability and diagnostics

# Load Kafka topic from .env file or fallback to default
kafka_topic = os.getenv("KAFKA_TOPIC", "signal_eurusd")


def main():
    # Step 1: Load environment variables from the .env file into the system environment
    load_dotenv()

    print("✅ MCP Agent is starting...")

    # Step 2: Simulate receiving a raw signal (normally this would come from email, webhook, etc.)
    raw_signal = {
        "symbol": "EURUSD",                  # Currency pair
        "direction": "BUY",                  # Trade direction
        "entry_price": 1.0860,               # Suggested entry point
        "sl": 1.0832,                        # Stop loss
        "tp": 1.0910,                        # Take profit
        "timestamp": "2025-07-05T13:00:00Z"  # When the signal was generated
    }

    # Step 3: Parse and normalize the signal into a standard structure
    signal = parse_signal(raw_signal)

    # Step 4: Check if the signal passes the filter logic (e.g., time, symbol, R:R ratio)
    if not is_valid_signal(signal):
        log_event("FILTER", "Signal rejected by filter.")  # Log the rejection reason
        return  # Exit early if the signal is not valid

    # Step 5: Evaluate the signal and make a decision (e.g., execute, warn, skip)
    decision = make_decision(signal)

    if decision == "EXECUTE":
        # Step 6: If the decision is to execute, send the signal to Kafka for MT5 consumption
        send_to_kafka(signal, kafka_topic)
        log_event("INFO", "Signal sent to Kafka.")
    else:
        # If decision was not to execute, log the reason
        log_event("SKIPPED", f"Decision: {decision} — signal skipped.")


# Step 7: Only run this block if the file is executed directly (not imported as a module)
if __name__ == "__main__":
    main()

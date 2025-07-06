# 🤖 Mikrobot-MCP — Modular SignalBridge for MQL5

> “Plug-and-Play Trading Intelligence using MCP + Kafka + MQL5 + AI Interfaces”

---

## 🧠 What is Mikrobot-MCP?

Mikrobot-MCP is an **automated trading framework** built to process external trading signals (like TradingView), filter them using logic or AI, and **relay valid trades to MetaTrader 5 (MT5)** with precision. It uses a modular **MCP agent** to wrap logic, validation, and execution into a clean pipeline — and uses **Kafka** to ensure reliable signal transport between systems.

This is not a basic signal bot. This is the beginning of a **multi-agent trading mesh**, with clean I/O, risk-aware validation, and precision order routing.

---

## 🔧 Architecture

```mermaid
graph TD
    A[TradingView Signal (Email/Webhook)] --> B[MCP Python Agent]
    B --> C[Signal Filtering + Validation]
    C --> D[Kafka Topic]
    D --> E[MQL5 EA Listener]
    E --> F[MT5 Trade Execution]
    E --> G[Trade Feedback (TBD)]

/mikrobot-mpc/
├── main.py                    # MCP bootstrap logic
├── .env                       # Configurable environment vars
├── /mcp_agent/                # Modular agent components
│   ├── signal_parser.py       # Cleans incoming signal formats
│   ├── filter_engine.py       # Accept/reject logic
│   ├── decision_engine.py     # Final decision logic
│   ├── relay_to_kafka.py      # Kafka producer logic
│   └── logbook.py             # Logging helper
├── /kafka/                    # Optional: CLI tools
│   ├── producer.py
│   └── consumer.py
├── /tests/                    # Pytest-style signal parsing tests
├── requirements.txt
└── README.md

📦 What's built and working today (2025-07-05)
✅ MCP Python Agent

Reads raw signals (from email/webhook/API)

Parses and normalizes signal format

Filters based on strategy logic (e.g., Risk:Reward, instrument, direction)

Makes EXECUTE / SKIP decision using a decision_engine

Sends valid trades to Kafka with topic-based routing

Logs all activity to console (extensible to files/Telegram/DB)

✅ Kafka Integration

Signals routed per instrument (e.g., signal_eurusd)

Producer/Consumer logic implemented and testable

Clean JSON schema and topic management

✅ MQL5 EA Receiver (v0.1)

Reads signal JSON from Files/signal.json

Parses direction, SL, TP, entry

Executes market trade with minimal logic

Journal logging to verify execution

🔭 What’s coming next
🔄 Live Socket/Kafka Stream in EA
The current EA reads from a static file. Next: it will listen for signals directly via WebRequest, socket, or local file-watcher.

📈 Fully Coded Strategy:

H1 Break of Structure (BoS)

M15 Break-and-Retest

Entry with 0.6 pip confirmation

Built-in risk logic: TP/SL with R:R validation

Optional confirmation with ADX/TDFI indicators

💡 Planned Extensions:

✅ Telegram alerts

🧠 ML logic (Keras or Scikit backend)

📊 Dashboard/Trade history

☁️ Kafka distributed architecture for multi-symbol agents

🪄 Example Signal JSON
json
Kopioi
Muokkaa
{
  "symbol": "EURUSD",
  "direction": "BUY",
  "entry_price": 1.0860,
  "sl": 1.0832,
  "tp": 1.0910,
  "timestamp": "2025-07-05T13:00:00Z"
}
This gets routed to Kafka → picked up by EA → trade executed if valid.

🚀 How to Run
Clone the repo
git clone https://github.com/ArcticCoderGuy/mikrobot-mpc.git

Start Kafka locally or via Docker (support coming soon)

Launch MCP Agent

bash
Kopioi
Muokkaa
python main.py
Drop signal.json into your MT5 /Files directory
Run EA on chart (EURUSD H1 or M15)

🌍 Why this matters
This architecture separates signal quality from execution. It gives you:

Full control over what trades get through

Centralized filtering logic (Python is powerful!)

MT5 stays lightweight — no signal parsing there

Easy plugin system for future ML, Telegram, risk managers

It's the USB-C of trade signal routing — plug any logic in, route cleanly to execution

-------------------

Example Signal JSON


{
  "symbol": "EURUSD",
  "direction": "BUY",
  "entry_price": 1.0860,
  "sl": 1.0832,
  "tp": 1.0910,
  "timestamp": "2025-07-05T13:00:00Z"
}

🌍 Why this matters
This architecture separates signal quality from execution. It gives you:

Full control over what trades get through

Centralized filtering logic (Python is powerful!)

MT5 stays lightweight — no signal parsing there

Easy plugin system for future ML, Telegram, risk managers

🛠 Contributors
Markus Kaprio — Strategy Logic, MQL5 architecture

GPT-4o (SignalBridge v0.1) — Parsing & automation agent


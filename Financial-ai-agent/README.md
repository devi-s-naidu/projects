````markdown
# 📊 Financial AI Agent

An Agentic AI system that autonomously analyzes financial markets, generates technical insights, computes risk scores, and provides actionable trade recommendations via an interactive web dashboard.

---

## 🔹 Features

- Autonomous Market Analysis
  - NIFTY, BANKNIFTY, or any stock/index
  - EMA crossover trend detection
  - RSI & MACD technical indicators
  - Volatility assessment

- Risk Scoring & Trade Recommendations
  - BUY / HOLD / SELL signals
  - Risk score (0–100) & level (Low / Medium / High)

- Interactive Web Dashboard
  - Dark professional UI
  - Responsive market cards
  - Interactive RSI & MACD charts (Chart.js)
  - User query input for dynamic analysis

- Agentic AI Architecture
  - Planning & reasoning
  - Tool calling (Yahoo Finance via `yfinance`)
  - Time-series + LLM synthesis ready

---

## 🛠 Tech Stack

| Layer           | Technology / Library        |
|-----------------|-----------------------------|
| Backend         | Python 3.10+, FastAPI       |
| AI & Analysis   | Pandas, TA-Lib (`ta`)       |
| Data Sources    | Yahoo Finance (`yfinance`)  |
| Frontend        | HTML, CSS, Chart.js         |
| Environment     | Virtualenv, Uvicorn         |

---

## ⚡ Setup Instructions

1. Clone the repository

```bash
git clone <repo-url>
cd financial-ai-agent
````

2. Create a virtual environment

```bash
python -m venv venv
```

3. Activate the environment

* Windows:

```bash
venv\Scripts\activate
```

* Linux / Mac:

```bash
source venv/bin/activate
```

4. Install dependencies

```bash
pip install -r requirements.txt
```

5. Set OpenAI API Key (optional for LLM reasoning)

Create a `.env` file:

```env
OPENAI_API_KEY=your_openai_api_key_here
```

6. Run the web dashboard

```bash
uvicorn web_app:app --reload
```

7. Open browser at:

```
http://127.0.0.1:8000
```

---

## 🖥 Project Structure

```
financial-ai-agent/
│
├── agent/
│   ├── agent.py
│   ├── executor.py
│   ├── planner.py
│   ├── reasoner.py
│   └── trade_logic.py
│
├── tools/
│   ├── market_data.py
│   ├── indicators.py
│
├── memory/
│   └── state.py
│
├── web/
│   ├── templates/index.html
│   └── static/style.css
│
├── web_app.py
├── config.py
├── main.py
├── requirements.txt
└── README.md
```

---

## 📈 How It Works

1. User Input
   Enter a query (e.g., “Analyze NIFTY & BANKNIFTY for next 7 days”).

2. Agent Planning
   Agent decides which tools to call (data fetch, indicators, reasoning).

3. Tool Execution

   * Fetch historical market data via Yahoo Finance
   * Compute technical indicators: RSI, MACD, EMA, ATR

4. Reasoning & Analysis

   * Determine trend, momentum, volatility
   * Compute risk score and trade recommendation

5. Web Rendering

   * Dynamic cards with charts
   * BUY / HOLD / SELL + risk score displayed

---

## 🎯 Key Highlights

* Fully autonomous agent with modular architecture
* Professional dashboard with interactive technical charts
* Real-time insights using up-to-date market data
* Extensible for multi-agent or LLM-based reasoning

---


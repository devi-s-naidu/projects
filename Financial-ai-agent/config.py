import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

DEFAULT_SYMBOLS = {
    "NIFTY": "^NSEI",
    "BANKNIFTY": "^NSEBANK"
}

LOOKBACK_DAYS = 180

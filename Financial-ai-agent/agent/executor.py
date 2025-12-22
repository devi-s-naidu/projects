from tools.market_data import fetch_market_data
from tools.indicators import add_indicators
from tools.sentiment import mock_news_sentiment
from config import DEFAULT_SYMBOLS

def execute_tools(plan):
    results = {}

    for name, symbol in DEFAULT_SYMBOLS.items():
        df = fetch_market_data(symbol)
        df = add_indicators(df)

        results[name] = {
            "data": df,
            "sentiment": mock_news_sentiment(name)
        }

    return results

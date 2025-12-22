def mock_news_sentiment(symbol):
    # Replace with real NewsAPI / GDELT later
    return {
        "sentiment": "Neutral",
        "confidence": 0.55,
        "summary": f"No major negative or positive news impacting {symbol}"
    }

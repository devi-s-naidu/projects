import numpy as np

def analyze_market(df):
    latest = df.iloc[-1]

    trend = "Bullish" if latest["ema_20"] > latest["ema_50"] else "Bearish"
    momentum = "Strong" if latest["rsi"] > 60 else "Weak"
    volatility = "High" if latest["volatility"] > df["volatility"].mean() else "Normal"

    chart_data = {
        "dates": df.index.strftime("%Y-%m-%d").tolist()[-30:],
        "rsi": df["rsi"].round(2).tolist()[-30:],
        "macd": df["macd"].round(2).tolist()[-30:],
    }

    return {
        "trend": trend,
        "momentum": momentum,
        "volatility": volatility,
        "rsi": round(latest["rsi"], 2),
        "charts": chart_data
    }

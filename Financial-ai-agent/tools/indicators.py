import ta
import pandas as pd

def add_indicators(df):
    close = pd.Series(df["Close"].values.flatten(), index=df.index)
    high = pd.Series(df["High"].values.flatten(), index=df.index)
    low = pd.Series(df["Low"].values.flatten(), index=df.index)

    df["rsi"] = ta.momentum.RSIIndicator(close).rsi()
    df["macd"] = ta.trend.MACD(close).macd()
    df["ema_20"] = ta.trend.EMAIndicator(close, 20).ema_indicator()
    df["ema_50"] = ta.trend.EMAIndicator(close, 50).ema_indicator()
    df["volatility"] = ta.volatility.AverageTrueRange(
        high, low, close
    ).average_true_range()

    df.dropna(inplace=True)
    return df

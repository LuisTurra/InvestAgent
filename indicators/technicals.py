from ta.trend import MACD
from ta.trend import EMAIndicator
from ta.momentum import RSIIndicator
from ta.volatility import AverageTrueRange

import numpy as np


def calculate_indicators(df):

    close = df["Close"]
    high = df["High"]
    low = df["Low"]

    rsi = RSIIndicator(close).rsi()

    ema20 = EMAIndicator(close, window=20).ema_indicator()

    ema50 = EMAIndicator(close, window=50).ema_indicator()

    macd = MACD(close)

    atr = AverageTrueRange(
        high,
        low,
        close
    ).average_true_range()

    volatility = close.pct_change().std() * np.sqrt(252)

    return {
        "price": float(close.iloc[-1]),
        "rsi": float(rsi.iloc[-1]),
        "ema20": float(ema20.iloc[-1]),
        "ema50": float(ema50.iloc[-1]),
        "macd": float(macd.macd().iloc[-1]),
        "signal": float(macd.macd_signal().iloc[-1]),
        "atr": float(atr.iloc[-1]),
        "volatility": float(volatility)
    }
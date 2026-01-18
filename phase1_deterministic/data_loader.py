import yfinance as yf
import pandas as pd

def load_data(symbol="^GSPC", start="2015-01-01", end="2023-01-01"):
    data = yf.download(symbol, start=start, end=end)
    return data["Close"]

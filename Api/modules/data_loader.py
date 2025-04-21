import os
import pandas as pd
import yfinance as yf
from datetime import datetime

def load_data(ticker: str, start: str, end: str = None) -> pd.DataFrame:
    """Load OHLCV data via yfinance."""
    if end is None:
        end = datetime.today().strftime('%Y-%m-%d')
    df = yf.download(ticker, start=start, end=end, progress=False)
    df = df[['Open','High','Low','Close','Volume']].dropna()
    return df

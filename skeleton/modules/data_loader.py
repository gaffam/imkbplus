import os
import pandas as pd

def load_data(ticker: str, start_date: str, end_date: str = None) -> pd.DataFrame:
    """
    Load OHLCV data for a given ticker between dates.
    To be implemented: multiple sources, caching, error handling.
    """
    raise NotImplementedError("load_data function needs implementation")

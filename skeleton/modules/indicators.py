import pandas as pd

def calculate_sma(series: pd.Series, period: int) -> pd.Series:
    """Calculate Simple Moving Average"""
    raise NotImplementedError("calculate_sma needs implementation")

def calculate_bollinger(series: pd.Series, period: int, std_dev: float):
    """Calculate Bollinger Bands"""
    raise NotImplementedError("calculate_bollinger needs implementation")

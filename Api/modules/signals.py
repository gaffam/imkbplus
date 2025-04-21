import pandas as pd
from modules.data_loader import load_data

def generate_bollinger_signals(df: pd.DataFrame, params: dict) -> pd.DataFrame:
    """Compute simple Bollinger Band signals."""
    period = params.get('bb_period', 20)
    std_dev = params.get('std_dev', 2)
    m = df['Close'].rolling(window=period).mean()
    s = df['Close'].rolling(window=period).std()
    df['Upper'] = m + std_dev * s
    df['Lower'] = m - std_dev * s
    df['Signal'] = 0
    df.loc[df['Close'] < df['Lower'], 'Signal'] = 1
    df.loc[df['Close'] > df['Upper'], 'Signal'] = -1
    return df

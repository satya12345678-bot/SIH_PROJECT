import pandas as pd

def bollinger_bands(data: pd.Series, window: int = 20, num_std_dev: int = 3):
    moving_avg = data.rolling(window=window).mean()
    rolling_std = data.rolling(window=window).std()
    upper_band = moving_avg + (rolling_std * num_std_dev)
    lower_band = moving_avg - (rolling_std * num_std_dev)
    return moving_avg, upper_band, lower_band
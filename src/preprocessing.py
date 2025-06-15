import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def preprocess_for_lstm(data: pd.DataFrame, feature_col: str = 'Price', window_size: int = 30):
    """
    Scale the feature column and create sequences for LSTM input.
    """
    scaler = MinMaxScaler(feature_range=(0, 1))
    scaled_data = scaler.fit_transform(data[[feature_col]])

    X, y = [], []
    for i in range(window_size, len(scaled_data)):
        X.append(scaled_data[i - window_size:i, 0])
        y.append(scaled_data[i, 0])

    import numpy as np
    X, y = np.array(X), np.array(y)
    X = X.reshape((X.shape[0], X.shape[1], 1))

    return X, y, scaler

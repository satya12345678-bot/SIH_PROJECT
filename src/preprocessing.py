import pandas as pd
import numpy as np
from typing import Tuple

# Only import these if you use them
from sklearn.preprocessing import MinMaxScaler
from sklearn.impute import SimpleImputer

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

    X, y = np.array(X), np.array(y)
    X = X.reshape((X.shape[0], X.shape[1], 1))

    return X, y, scaler

def drop_columns(df, columns):
    return df.drop(columns, axis=1)

def impute_numeric(df, numeric_columns):
    imputer = SimpleImputer(strategy='mean')
    df[numeric_columns] = imputer.fit_transform(df[numeric_columns])
    return df

def impute_categorical(df, categorical_columns):
    imputer = SimpleImputer(strategy='most_frequent')
    df[categorical_columns] = imputer.fit_transform(df[categorical_columns])
    return df

def get_column_types(df):
    numeric_columns = df.select_dtypes(include=[np.number]).columns.tolist()
    categorical_columns = df.select_dtypes(exclude=[np.number]).columns.tolist()
    return numeric_columns, categorical_columns

def load_data(train_path: str, test_path: str) -> Tuple[pd.DataFrame, pd.DataFrame]:
    train_df = pd.read_csv(train_path)
    test_df = pd.read_csv(test_path)
    return train_df, test_df

# Remove the following lines from this module; they should be in your main script, not in preprocessing.py
# train_df, test_df = load_data("../notebooks/Train.csv", "../notebooks/Test.csv")
# Index = test_df['Index']
# test_df = test_df.drop(['Index'], axis=1)

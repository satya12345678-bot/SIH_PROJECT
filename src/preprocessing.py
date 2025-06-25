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

def filter_commodity(df: pd.DataFrame, place: str) -> pd.DataFrame:
    return df[df['Commodity'] == place]

def group_and_average(df: pd.DataFrame) -> pd.DataFrame:
    df = df.groupby('Date', as_index=False)['Average'].mean()
    df['Date'] = pd.to_datetime(df['Date'])
    df.set_index('Date', inplace=True)
    return df

def fill_missing(df: pd.DataFrame) -> pd.DataFrame:
    return df.ffill()

def split_train_test(df: pd.DataFrame, split_date: str):
    df_train = df[df.index < split_date]
    df_test = df[df.index >= split_date]
    return df_train, df_test

def window_train(series, window_size, batch_size, shuffle_buffer, tf):
    dataset = tf.data.Dataset.from_tensor_slices(series)
    dataset = dataset.window(window_size + 1, shift=1, stride=1, drop_remainder=True)
    dataset = dataset.flat_map(lambda w: w.batch(window_size + 1))
    dataset = dataset.map(lambda w: (w[:-1], w[-1]))
    dataset = dataset.shuffle(shuffle_buffer)
    dataset = dataset.batch(batch_size).prefetch(1)
    return dataset

def window_test(series, window_size, batch_size, tf):
    dataset = tf.data.Dataset.from_tensor_slices(series)
    dataset = dataset.window(window_size, shift=1, stride=1, drop_remainder=True)
    dataset = dataset.flat_map(lambda w: w.batch(window_size))
    dataset = dataset.batch(batch_size).prefetch(1)
    return dataset

# Remove the following lines from this module; they should be in your main script, not in preprocessing.py
# train_df, test_df = load_data("../notebooks/Train.csv", "../notebooks/Test.csv")
# Index = test_df['Index']
# test_df = test_df.drop(['Index'], axis=1)

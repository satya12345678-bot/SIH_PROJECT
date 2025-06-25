import os
import numpy as np
import pandas as pd
import tensorflow as tf

from data_loader import load_data, load_kalimati_dataset
from preprocessing import (drop_columns, filter_commodity, group_and_average,
                           fill_missing, split_train_test, window_train, window_test,
                           get_column_types)
from model import train_catboost, predict
from submission import create_submission
from arima import difference_series, fit_arima, forecast_arima
from lstm import build_lstm_model
from bollinger import bollinger_bands

# Update these paths as per your actual data location
train_path = "../notebooks/Train.csv"
test_path = "../notebooks/Test.csv"
FILE_IN = "../data/raw/kalimati_tarkari_dataset.csv"

PLACE = "NV"
SPLIT_DATE = "2020-05-01"
WINDOW_SIZE = 10
BATCH_SIZE = 32
SHUFFLE_BUFFER = 3000

# Load and preprocess data
train_df, test_df = load_data(train_path, test_path)
df = load_kalimati_dataset(FILE_IN)

# Drop columns if they exist
for col in ['GpuNumberOfExecutionUnits']:
    if col in train_df.columns:
        train_df = drop_columns(train_df, [col])
    if col in test_df.columns:
        test_df = drop_columns(test_df, [col])

numeric_columns, categorical_columns = get_column_types(train_df)

train_df = impute_numeric(train_df, numeric_columns)
train_df = impute_categorical(train_df, categorical_columns)
test_df = impute_numeric(test_df, numeric_columns)
test_df = impute_categorical(test_df, categorical_columns)

X = train_df.drop(['FPS'], axis=1)
y = train_df['FPS']

cat_features = [col for col in [
    'CpuName', 'CpuMultiplierUnlocked', 'GpuName', 'GpuArchitecture',
    'GpuBus nterface', 'GpuDirectX', 'GpuMemoryType', 'GpuOpenCL',
    'GpuOpenGL', 'GpuShaderModel', 'GpuVulkan', 'GameName', 'GameSetting',
    'Dataset'
] if col in X.columns]

# Train model
model = train_catboost(X, y, cat_features)

# Prepare test data
if 'Index' in test_df.columns:
    Index = test_df['Index']
    test_df = test_df.drop(['Index'], axis=1)
else:
    Index = range(len(test_df))

y_test = predict(model, test_df)
create_submission(Index, y_test)

df = filter_commodity(df, PLACE)
df = group_and_average(df)
df = fill_missing(df)
df_train, df_test = split_train_test(df, SPLIT_DATE)

# ARIMA
data = difference_series(df_train['Average'], k_diff=1)
arima_model = fit_arima(data, order=(1, 0, 1))
forecast = forecast_arima(arima_model, steps=len(df_test),
                          last_observed_value=df['Average'].iloc[-1])

# LSTM
X_train = df_train['Average'].values
X_test = df_test['Average'].values
ds_train = window_train(X_train, WINDOW_SIZE, BATCH_SIZE, SHUFFLE_BUFFER, tf)
ds_test = window_test(np.concatenate((X_train[-WINDOW_SIZE:], X_test[:-1])),
                      WINDOW_SIZE, BATCH_SIZE, tf)

model = build_lstm_model(WINDOW_SIZE)
model.compile(loss=tf.keras.losses.Huber(), optimizer=tf.keras.optimizers.Adam())
model.fit(ds_train, epochs=2)  # Use more epochs in practice

forecasts = model.predict(ds_test).squeeze()

# Bollinger Bands
result = pd.DataFrame({'date': df_test.index, 'average': forecasts})
result.set_index('date', inplace=True)
moving_avg, upper_band, lower_band = bollinger_bands(result['average'])

print("Pipeline complete.")
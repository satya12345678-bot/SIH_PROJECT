import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Lambda, Conv1D, MaxPooling1D, Bidirectional, LSTM, Dense

def build_lstm_model(window_size):
    model = Sequential([
        Lambda(lambda x: tf.expand_dims(x, axis=-1), input_shape=[window_size]),
        Conv1D(filters=64, kernel_size=3, activation='relu'),
        MaxPooling1D(pool_size=2),
        Conv1D(filters=64, kernel_size=3, activation='relu'),
        MaxPooling1D(pool_size=2),
        Bidirectional(LSTM(32, return_sequences=True)),
        Bidirectional(LSTM(32)),
        Dense(1),
        Lambda(lambda x: x * 100.0)
    ])
    return model
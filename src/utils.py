import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error

def plot_forecasts(true, pred, title='Forecast vs Actual'):
    """
    Plot predicted vs actual values.
    """
    plt.figure(figsize=(12,6))
    plt.plot(true, label='Actual')
    plt.plot(pred, label='Predicted')
    plt.title(title)
    plt.xlabel('Time')
    plt.ylabel('Value')
    plt.legend()
    plt.show()

def rmse(y_true, y_pred):
    return np.sqrt(mean_squared_error(y_true, y_pred))

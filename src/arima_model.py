import pandas as pd
import statsmodels.api as sm
from pmdarima import auto_arima

def train_arima_model(data: pd.Series):
    """
    Automatically find the best ARIMA model using AIC.
    """
    model = auto_arima(data, seasonal=False, trace=True)
    return model

def forecast_arima(model, periods: int):
    """
    Forecast using ARIMA model.
    """
    return model.predict(n_periods=periods)

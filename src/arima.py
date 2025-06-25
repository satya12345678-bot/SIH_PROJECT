import pandas as pd
from statsmodels.tsa.statespace.tools import diff
from statsmodels.tsa.arima.model import ARIMA

def difference_series(series, k_diff=1):
    return diff(series, k_diff=k_diff)

def fit_arima(data, order=(1,0,1)):
    model = ARIMA(data, order=order)
    return model.fit()

def forecast_arima(model_fit, steps, last_observed_value):
    forecast = model_fit.forecast(steps=steps)
    forecast_original_scale = forecast.cumsum() + last_observed_value
    return forecast_original_scale
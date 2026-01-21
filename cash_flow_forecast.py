
import pandas as pd

def rolling_forecast(df, window=3):
    df['Forecast'] = df['Net_Cash'].rolling(window).mean()
    return df

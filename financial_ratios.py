
import pandas as pd

def profit_margin(df):
    df['Profit_Margin_%'] = (df['Net_Income'] / df['Revenue']) * 100
    return df

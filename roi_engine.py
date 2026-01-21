
import pandas as pd

def calculate_roi(df):
    df['ROI_%'] = ((df['Returns'] - df['Investment_Cost']) / df['Investment_Cost']) * 100
    return df

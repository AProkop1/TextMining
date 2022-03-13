import csv
import pandas as pd


def get_data_csv(path: str) -> str:
    df = pd.read_csv(path, skipinitialspace=True, usecols=['title'])
    return df.to_string()

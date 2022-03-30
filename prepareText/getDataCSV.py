import pandas as pd


def get_data_csv(path: str, column: str) -> str:
    df = pd.read_csv(path, skipinitialspace=True, usecols=[column])
    return df.to_string()
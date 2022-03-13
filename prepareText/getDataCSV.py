import csv
import pandas as pd


def get_data_csv(path: str) -> str:
    df = pd.read_csv(path, skipinitialspace=True, usecols=['title'])
    # rows = []
    # with open(path, 'r') as file:
    #     csvreader = csv.reader(file)
    #     # header = next(csvreader)
    #     for row in csvreader:
    #         rows.append(row['title'])
    # s = " "
    # str_result = ""
    # for x in rows:
    #     str_result += s.join(x)
    return df.to_string()

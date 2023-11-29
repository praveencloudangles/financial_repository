print("data loading---------------")
import pandas as pd


def data_loading():
    df = pd.read_csv("PS_20174392719_1491204439457_log.csv")
    return df

data_loading()
import boto3
import pandas as pd


def data_loading():
    client = boto3.client('s3')

    path = "https://mlops-storage1.s3.amazonaws.com/PS_20174392719_1491204439457_log.csv"

    df = pd.read_csv(path)
    print(df.head())

    return df
data_loading()

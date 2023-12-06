import boto3
import pandas as pd


def data_loading():
    client = boto3.client('s3')

    path = "risk_dataset.csv"

    df = pd.read_csv(path)
    print(df.head())
    return df
data_loading()

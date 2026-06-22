import pandas as pd


def load_data():
    df = pd.read_csv("weather.csv")
    return df


def cleandata(df):
    df = df.drop_duplicates()

    df = df.dropna()

    df['Date'] = pd.to_datetime(df['Date'])

    return df


def heighest_temp(df):
    return df['Temperature'].max()


def lowest_temp(df):
    return df['Temperature'].min()


def average_humidity(df):
    return df['Humidity'].mean()


def average_tem(df):
    return df['Temperature'].mean()


def total_rainfall(df):
    total = df["Rainfall"].sum()
    return total

def average_moving(df):
    df['MA7']=df["Temperature"].rolling(7).mean()
    return df


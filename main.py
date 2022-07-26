from lib2to3.pgen2.pgen import DFAState
import pandas as pd
from dataframe.extract import extract_from_csv
from dataframe.transform import transform_meetdatum, transform_stroom, transform_teruglevering, drop_columns
from view.plot import plot_meterstanden_bar

def create_dataframe_from_csv():
    df = extract_from_csv()
    df = drop_columns(df)
    df = transform_meetdatum(df, start_date = '2022-05-26')
    df = transform_stroom(df)
    df = transform_teruglevering(df)
    df = df.iloc[1: , :]
    df['Teruglevering_mean'] = df['Teruglevering_diff'].mean()
    df['Stroom_mean'] = df['Stroom_diff'].mean()
    return df

def select_maximum(df, column):
    maxidx = df[column].idxmax()
    maximmum = df.loc[maxidx]
    print(f"Max {column}: {maximmum}")
    return maximmum

def select_minimum(df, column):
    minidx = df[column].idxmin()
    minimun = df.loc[minidx]
    print(f"Min {column}: {minimun}")
    return minimun

df = create_dataframe_from_csv()
print(f"Aantal records {len(df)}")
df.to_csv('data/transformed.csv', index=False)
df.set_index('Datum')
print(df)

plot_meterstanden_bar(df)
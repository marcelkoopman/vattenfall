from lib2to3.pgen2.pgen import DFAState
import pandas as pd
import matplotlib.pyplot as plt
from dataframe.extract import extract_from_csv
from dataframe.transform import transform_meetdatum, transform_stroom, transform_teruglevering, drop_columns

def create_dataframe_from_csv():
    df = extract_from_csv()
    df = drop_columns(df)
    df = transform_meetdatum(df, start_date = '2022-05-26')
    df = transform_stroom(df)
    df = transform_teruglevering(df)
    df = df.iloc[1: , :]
    # df.info()

    # 
    # df['pct_stroom'] = df['Stroom'].pct_change()
    # df['pct_teruglevering'] = df['Teruglevering'].pct_change()
    # df['diff_stroom'] = df['Stroom'].diff().abs()
    # df['diff_teruglevering'] = df['Teruglevering'].diff().abs()
    # df['median_teruglevering'] = df['diff_teruglevering'].median()
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
x = df['Datum']
plt.plot(x, df['Stroom_diff'], label='Stroomverbruik')
plt.plot(x, df['Teruglevering_diff'], label='Teruglevering')
plt.plot(x, df['Teruglevering_mean'], label='Teruglevering gemiddelde')
plt.plot(x, df['Stroom_mean'], label='Stroomverbruik gemiddelde')
plt.legend()
plt.show()
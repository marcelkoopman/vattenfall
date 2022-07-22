import pandas as pd
import matplotlib.pyplot as plt

from dataframe.extract import extract_from_csv
from dataframe.transform import transform_meetdatum, transform_stroom, transform_teruglevering

def jaar_verbruik_2021_kwh():
    return 2216

def jaar_teruglevering_2021_kwh():
    return 1513;

def create_dataframe_from_csv():
    df = extract_from_csv()
    df = transform_meetdatum(df, start_date = '2022-05-26')
    df = transform_stroom(df)
    df = transform_teruglevering(df)
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

df = create_dataframe_from_csv()
select_maximum(df, "Teruglevering_diff")
x = df['Datum']
plt.plot(x, df['Stroom_diff'], label='Stroomverbruik')
plt.plot(x, df['Teruglevering_diff'], label='Teruglevering')
plt.plot(x, df['Teruglevering_mean'], label='Teruglevering gemiddelde')
plt.plot(x, df['Stroom_mean'], label='Stroomverbruik gemiddelde')
plt.legend()
plt.show()
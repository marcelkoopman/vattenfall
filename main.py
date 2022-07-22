import pandas as pd
import matplotlib.pyplot as plt

from dataframe.extract import extract_from_csv
from dataframe.transform import transform_meetdatum, transform_stroom, transform_teruglevering

def create_dataframe_from_csv():
    df = extract_from_csv()
    df = transform_meetdatum(df)
    df = transform_stroom(df)
    df = transform_teruglevering(df)
    df.info()

    # df['change'] = df['Teruglevering'] - df['Stroom']   
    # df['pct_stroom'] = df['Stroom'].pct_change()
    # df['pct_teruglevering'] = df['Teruglevering'].pct_change()
    # df['diff_stroom'] = df['Stroom'].diff().abs()
    # df['diff_teruglevering'] = df['Teruglevering'].diff().abs()
    # df['median_teruglevering'] = df['diff_teruglevering'].median()
    # df['mean_teruglevering'] = df['diff_teruglevering'].mean()
    # df['mean_stroom'] = df['diff_stroom'].mean()
    return df

def select_maximum(df):
    maxidx = df['diff_stroom'].idxmax()
    maximmum = df.loc[maxidx]

df = create_dataframe_from_csv().head(10)
# select_maximum(df)
# df.info()
x = df['Datum']
# plt.plot(x, df['change'], label='Efficiency')
plt.plot(x, df['Teruglevering'], label='Teruglevering')

plt.legend()
plt.show()
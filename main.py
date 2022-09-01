import pandas as pd
from dataframe.extract import extract_from_csv
from dataframe.transform import transform_meetdatum, transform_stroom, transform_teruglevering, drop_columns
from view.plot import plot_meterstanden_line
import numpy as np
import logging

def create_dataframe_from_csv():
    df = extract_from_csv()
    df = drop_columns(df)
    # df = transform_meetdatum(df, start_date = '2022-05-26')
    df = transform_meetdatum(df, start_date = '2022-08-01')
    df = transform_stroom(df)
    df = transform_teruglevering(df)
    df = df.iloc[1: , :]
    df['Teruglevering_mean'] = df['Teruglevering_diff'].mean()
    df['Stroom_mean'] = df['Stroom_diff'].mean()
    return df

def select_maximum(df, column):
    maxidx = df[column].idxmax()
    maximum = df.loc[maxidx]
    logging.info(f"Max {column}: {maximum}")
    return maximum

def select_minimum(df, column):
    minidx = df[column].idxmin()
    minimun = df.loc[minidx]
    logging.info(f"Min {column}: {minimun}")
    return minimun

def main():
    logging.basicConfig(format='%(asctime)s %(message)s', level = logging.INFO)
    logging.info("Inlezen meterstanden.csv...")
    df = create_dataframe_from_csv()
    logging.info(f"Aantal records {len(df)}")
    transformed_file = 'transformed.csv'
    df.to_csv(f'data/{transformed_file}', index=False)
    logging.info(f"Zie {transformed_file}")
    df.set_index('Datum')
    logging.info(df)
    plot_meterstanden_line(df)

if __name__ == '__main__':
    main()
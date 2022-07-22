import pandas as pd
import matplotlib.pyplot as plt
import locale
import logging
from dataframe.csv_parser import parse_csv
from dataframe.date_parser import parse_and_sort_on_dates

locale.setlocale(locale.LC_ALL, "nl_NL")
logger = logging.getLogger('log')
logger.setLevel(logging.INFO)
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)

def create_dataframe_from_csv():
    df = parse_csv().head(30)
    df = parse_and_sort_on_dates(df)
    print(f"{len(df)} gesorteerd")

    # df['Stroom'] = df['Stroom 1 (kWh)'] + df['Stroom 2 (kWh)']
    # df['Teruglevering'] = df['Teruglevering 1 (kWh)'] + df['Teruglevering 2 (kWh)']
    # df['change'] = df['Teruglevering'] - df['Stroom']
    # df['Meetdatum'] = df['Meetdatum'].str.replace(".", "", 1, regex=False)
    # df['Datum'] = pd.to_datetime(df['Meetdatum'], format='%d %b %Y')
    # df = df.drop("Meetdatum", axis='columns')
    # df = df.sort_values(by=['Datum'], ascending = True)
    
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
    logger.info(f'max stroom {maximmum}')

logger.info("Parsing CSV")
df = create_dataframe_from_csv().head(10)
logger.info("Dataframe created")
# select_maximum(df)
# df.info()
x = df['Datum']
# plt.plot(x, df['change'], label='Efficiency')
plt.plot(x, df['Teruglevering 1 (kWh)'], label='Teruglevering 1 (kWh)')

plt.legend()
plt.show()
import pandas as pd

def parse_and_sort_on_dates(df):
    df['Meetdatum'] = df['Meetdatum'].str.replace(".", "", regex=False)
    df['Datum'] = pd.to_datetime(df['Meetdatum'], format='%d %b %Y')
    df = df.sort_values(by=['Datum'], ascending = True)
    return df.drop('Meetdatum', axis='columns')    
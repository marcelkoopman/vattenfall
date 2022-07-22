import pandas as pd
import locale
locale.setlocale(locale.LC_ALL, "nl_NL")

def transform_meetdatum(df):
    df['Meetdatum'] = df['Meetdatum'].str.replace(".", "", regex=False)
    df['Datum'] = pd.to_datetime(df['Meetdatum'], format='%d %b %Y')
    df = df.sort_values(by=['Datum'], ascending = False)
    return df.drop('Meetdatum', axis='columns')    

def transform_stroom(df):
    df['Stroom'] = df['Stroom 1 (kWh)'] + df['Stroom 2 (kWh)']
    return df.drop(['Stroom 1 (kWh)','Stroom 2 (kWh)'], axis='columns')

def transform_teruglevering(df):
    df['Teruglevering'] = df['Teruglevering 1 (kWh)'] + df['Teruglevering 2 (kWh)']
    return df.drop(['Teruglevering 1 (kWh)','Teruglevering 2 (kWh)'], axis='columns')
   
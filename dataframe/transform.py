import pandas as pd
import datetime as dt
import locale
locale.setlocale(locale.LC_ALL, "nl_NL")

def transform_meetdatum(df, start_date):
    df['Meetdatum'] = df['Meetdatum'].str.replace(".", "", regex=False)
    df['Datum'] = pd.to_datetime(df['Meetdatum'], format='%d %b %Y')
    df = df.sort_values(by=['Datum'], ascending = False)
    mask = df['Datum']>=start_date
    df = df[mask]
    return df.drop('Meetdatum', axis='columns')    

def drop_columns(df):
    return df.drop(['Gas 1 (m³)', 'Opmerkingen'], axis='columns')

def transform_stroom(df):
    df['Stroom'] = df['Stroom 1 (kWh)'] + df['Stroom 2 (kWh)']
    df['Stroom_diff'] = df['Stroom'].diff().abs()
    return df.drop(['Stroom 1 (kWh)','Stroom 2 (kWh)', 'Stroom'], axis='columns')

def transform_teruglevering(df):
    df['Teruglevering'] = df['Teruglevering 1 (kWh)'] + df['Teruglevering 2 (kWh)']
    df['Teruglevering_diff'] = df['Teruglevering'].diff().abs()
    return df.drop(['Teruglevering 1 (kWh)','Teruglevering 2 (kWh)', 'Teruglevering'], axis='columns')

   
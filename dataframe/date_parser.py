import pandas as pd

def parse_and_sort_on_dates(df):
    df['Meetdatum'] = df['Meetdatum'].str.replace(".", "", regex=False)
    print(f"1 {len(df)}")
    df['Datum'] = pd.to_datetime(df['Meetdatum'], format='%d %b %Y')
    print(f"2 {len(df)}")
    df = df.sort_values(by=['Datum'], ascending = True)
    print(f"3 {len(df)}")
    return df
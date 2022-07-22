import pandas as pd

def extract_from_csv():
    df = pd.read_csv("data/mijn-meterstanden.csv", encoding = "ISO-8859-1")
    print(f"{len(df)} records ingelezen")
    return df

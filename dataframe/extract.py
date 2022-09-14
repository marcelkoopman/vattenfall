import pandas as pd

def extract_from_csv():
    return pd.read_csv("data/mijn-meterstanden.csv", encoding = "ISO-8859-1", thousands=".")
import pandas as pd
import locale

locale.setlocale(locale.LC_ALL, "nl_NL")


def transform_meetdatum(df, start_date):
    df["Meetdatum"] = df["Meetdatum"].str.replace(".", "", regex=False)
    df["Datum"] = pd.to_datetime(df["Meetdatum"], format="%d %b %Y")
    df = df.sort_values(by=["Datum"], ascending=False)
    mask = df["Datum"] >= start_date
    df = df[mask]
    return df.drop("Meetdatum", axis="columns")


def drop_columns(df):
    return df.drop(["Gas 1 (m³)", "Opmerkingen"], axis="columns")


def transform_stroom(df):
    stroom1 = df["Stroom 1 (kWh)"].astype(float)
    stroom2 = df["Stroom 2 (kWh)"].astype(float)
    df["Stroom"] = stroom1 + stroom2
    df["Stroom_diff"] = df["Stroom"].diff().abs()
    df = df.drop(["Stroom 1 (kWh)", "Stroom 2 (kWh)", "Stroom"], axis="columns")
    return df


def transform_teruglevering(df):
    terug1 = df["Teruglevering 1 (kWh)"].astype(float)
    terug2 = df["Teruglevering 2 (kWh)"].astype(float)
    df["Teruglevering"] = terug1 + terug2
    df["Teruglevering_diff"] = df["Teruglevering"].diff().abs()
    df = df.drop(
        ["Teruglevering 1 (kWh)", "Teruglevering 2 (kWh)", "Teruglevering"],
        axis="columns",
    )
    return df

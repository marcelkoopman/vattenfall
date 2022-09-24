import matplotlib.pyplot as plt


def plot_meterstanden_line(df):
    plt.rcdefaults()
    datum = df["Datum"]
    stroom = df["Stroom_diff"]
    terug = df["Teruglevering_diff"]

    fig, ax = plt.subplots(figsize=(9, 9))
    ax.plot(datum, stroom)
    ax.plot(datum, terug)

    ax.fill_between(
        datum,
        stroom,
        terug,
        where=(terug >= stroom),
        interpolate=True,
        color="green",
        alpha=0.25,
        label="Positief",
    )

    ax.fill_between(
        datum,
        stroom,
        terug,
        where=(stroom > terug),
        interpolate=True,
        color="red",
        alpha=0.25,
        label="Negatief",
    )
    ax.legend()
    plt.show()

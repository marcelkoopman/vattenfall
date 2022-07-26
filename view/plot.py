import pandas as pd
import matplotlib.pyplot as plt

def plot_meterstanden_bar(df):
    plt.rcdefaults()
    fig, ax = plt.subplots()
    x = df['Datum']
    ax.barh(x, df['Teruglevering_diff'], color='yellow')
    ax.barh(x, df['Stroom_diff'],  color='blue')
    ax.invert_yaxis()  
    ax.yaxis_date()
    ax.legend()
    plt.show()
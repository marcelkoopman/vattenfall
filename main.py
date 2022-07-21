import pandas as pd
import matplotlib.pyplot as plt
import locale
locale.setlocale(locale.LC_ALL, "nl_NL")

df = pd.read_csv("data/mijn-meterstanden.csv", encoding = "ISO-8859-1").head(30)

df['Stroom'] = df['Stroom 1 (kWh)'] + df['Stroom 2 (kWh)']
df['Teruglevering'] = df['Teruglevering 1 (kWh)'] + df['Teruglevering 2 (kWh)']
df['change'] = df['Teruglevering'] - df['Stroom']
df['Meetdatum'] = df['Meetdatum'].str.replace(".", "")
df['Datum'] = pd.to_datetime(df['Meetdatum'], format='%d %b %Y')
df = df.sort_values(by=['Datum'], ascending = True)
print(df)
# df.info()
df = df.query('Stroom>0')
df['pct_stroom'] = df['Stroom'].pct_change()
df['pct_teruglevering'] = df['Teruglevering'].pct_change()
df['diff_stroom'] = df['Stroom'].diff().abs()
df['diff_teruglevering'] = df['Teruglevering'].diff().abs()
df['median_teruglevering'] = df['diff_teruglevering'].median()
df['mean_teruglevering'] = df['diff_teruglevering'].mean()
df['mean_stroom'] = df['diff_stroom'].mean()

maxidx = df['diff_stroom'].idxmax()
maximmum = df.loc[maxidx]
# print(f'max stroom {maximmum}')
#  print(df[['pct_teruglevering', 'mean_teruglevering', 'Teruglevering']])
# print(df[['mean_teruglevering', 'mean_stroom']])
# df.info()
x = df['Meetdatum']
# print(df)
# plt.plot(x, df['Stroom'], label="Stroomverbruik")
# plt.plot(x, df['diff_teruglevering'], label="Teruglevering")
plt.plot(x, df['change'], label='Efficiency')
# plt.plot(x, df['Teruglevering'], label="Teruglevering")
# plt.plot(x, df['Gas 1 (m³)'], label="Gasverbruik")
# plt.plot_date(x, df['Gas 1 (m³)'])
# plt.plot_date(x, df['Stroom'])

plt.legend()
plt.show()
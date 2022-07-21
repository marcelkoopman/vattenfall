import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("data/mijn-meterstanden.csv", encoding = "ISO-8859-1")
df['Stroom'] = df['Stroom 1 (kWh)'] + df['Stroom 2 (kWh)']
df['Teruglevering'] = df['Teruglevering 1 (kWh)'] + df['Teruglevering 2 (kWh)']
df['pct_stroom'] = df['Stroom'].pct_change()
df['pct_teruglevering'] = df['Teruglevering'].pct_change()
df['median_teruglevering'] = df['Teruglevering'].median()
df['mean_teruglevering'] = df['Teruglevering'].mean()
df['mean_stroom'] = df['Stroom'].mean()
df['diff_stroom'] = df['Stroom'].diff().abs()
maxidx = df['diff_stroom'].idxmax()
maximmum = df.loc[maxidx]
print(f'max stroom {maximmum}')
print(df[['median_teruglevering', 'mean_teruglevering', 'Teruglevering']])
print(df[['Stroom', 'diff_stroom']])
# df.info()
x = df['Meetdatum']
# print(df)
plt.plot(x, df['diff_stroom'], label="Stroomverbruik")
# plt.plot(x, df['pct_teruglevering'], label="Teruglevering")
# plt.plot(x, df['Teruglevering'], label="Teruglevering")
# plt.plot(x, df['Gas 1 (m³)'], label="Gasverbruik")
# plt.plot_date(x, df['Gas 1 (m³)'])
# plt.plot_date(x, df['Stroom'])

plt.legend()
plt.show()
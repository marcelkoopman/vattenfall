import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("data/mijn-meterstanden.csv", encoding = "ISO-8859-1")
df['Stroom'] = df['Stroom 1 (kWh)'] + df['Stroom 2 (kWh)']
df['Teruglevering'] = df['Teruglevering 1 (kWh)'] + df['Teruglevering 2 (kWh)']
df.info()
x = df['Meetdatum']
# plt.plot(x, df['Stroom'], label="Stroomverbruik")
# plt.plot(x, df['Teruglevering'], label="Teruglevering")
plt.plot(x, df['Gas 1 (m³)'], label="Gasverbruik")
plt.legend()
plt.show()
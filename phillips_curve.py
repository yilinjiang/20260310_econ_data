import pandas as pd
from fredapi import Fred
import matplotlib.pyplot as plt

# 1. Initialize with your key
fred = Fred(api_key='d3ae93c7c7e385809521ece65dde30d2')

# 2. Pull Data: Unemployment Rate (UNRATE) and Consumer Price Index (CPIAUCSL)
unemp = fred.get_series('UNRATE')
cpi = fred.get_series('CPIAUCSL')

# 3. Data Transformation: Calculate Inflation (Year-over-Year % change)
inflation = cpi.pct_change(periods=12) * 100

# 4. Merge into a DataFrame
df = pd.DataFrame({'Unemployment': unemp, 'Inflation': inflation}).dropna()

# 5. Filter for a specific era (e.g., Post-2010 to see modern dynamics)
df_modern = df.loc['2010-01-01':]

# 6. The "Soundness" Moment: Plotting
plt.figure(figsize=(10, 6))
plt.scatter(df_modern['Unemployment'], df_modern['Inflation'], alpha=0.5)
plt.title('The Modern Phillips Curve (Post-2010)')
plt.xlabel('Unemployment Rate (%)')
plt.ylabel('Inflation Rate (YoY %)')
plt.grid(True)
plt.show()

print(f"Data points analyzed: {len(df_modern)}")
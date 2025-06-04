import pandas as pd
import matplotlib.pyplot as plt

# Load cumulative return data
df = pd.read_csv('max_sharpe_cum_returns.csv', index_col=0, parse_dates=True)

# Plot cumulative returns
plt.figure(figsize=(10, 6))
plt.plot(df.index, df['cumulative_return'], label='Max Sharpe Portfolio', color='blue')
plt.xlabel('Date')
plt.ylabel('Cumulative Return')
plt.title('Cumulative Returns of Max Sharpe Portfolio')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig('../plots/cumulative_returns.png')
plt.close()
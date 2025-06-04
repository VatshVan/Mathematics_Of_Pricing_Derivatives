# efficient_frontier.py
import pandas as pd
import matplotlib.pyplot as plt

# Load efficient frontier data
df = pd.read_csv('efficient_frontier.csv')

# Plot efficient frontier
plt.figure(figsize=(8, 6))
sc = plt.scatter(df['risk'], df['return'], c=df['sharpe'], cmap='viridis', edgecolor='k')
plt.colorbar(sc, label='Sharpe Ratio')
plt.xlabel('Risk (Standard Deviation)')
plt.ylabel('Expected Return')
plt.title('Efficient Frontier')
plt.grid(True)
plt.tight_layout()
plt.savefig('../plots/efficient_frontier.png')
plt.close()
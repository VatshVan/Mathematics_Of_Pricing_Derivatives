import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

DATA_PATH = '../Data/Historical_Data.csv'
PLOTS_DIR = '../plots'
os.makedirs(PLOTS_DIR, exist_ok=True)

data = pd.read_csv(DATA_PATH, parse_dates=True, index_col=0)
returns = data.pct_change().dropna()
mean_returns = returns.mean() * 252
cov_matrix = returns.cov() * 252

np.random.seed(42)
num_portfolios = 500
results = np.zeros((3, num_portfolios))
weights_array = np.zeros((num_portfolios, len(returns.columns)))
tickers = returns.columns

for i in range(num_portfolios):
    weights = np.random.random(len(tickers))
    weights /= np.sum(weights)
    weights_array[i] = weights
    port_return = np.sum(mean_returns * weights)
    port_std = np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights)))
    results[0,i] = port_std
    results[1,i] = port_return
    results[2,i] = port_return / port_std

max_sharpe_idx = np.argmax(results[2])
weights_max_sharpe = weights_array[max_sharpe_idx]

plt.figure(figsize=(10,6))
plt.bar(tickers, weights_max_sharpe)
plt.xticks(rotation=45, ha='right')
plt.ylabel('Weight')
plt.title('Weight Composition - Max Sharpe Portfolio')
plt.tight_layout()
plt.savefig(os.path.join(PLOTS_DIR, 'weight_composition.png'))
plt.close()
print(f"Weight composition plot saved to {PLOTS_DIR}/weight_composition.png")

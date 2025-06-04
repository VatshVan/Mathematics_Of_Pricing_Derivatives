
# weight_composition.py
import pandas as pd
import matplotlib.pyplot as plt
import os

# Create plots folder if it doesn't exist
# os.makedirs('../plots', exist_ok=True)

# Load portfolio weights
df = pd.read_csv('max_sharpe_weights.csv', index_col=0)

# Plot weight composition
plt.figure(figsize=(10, 6))
plt.bar(df.index, df['weight'], color='teal')
plt.xticks(rotation=45, ha='right')
plt.ylabel('Weight')
plt.title('Weight Composition of Max Sharpe Portfolio')
plt.tight_layout()
plt.savefig('../plots/weight_composition.png')
plt.close()
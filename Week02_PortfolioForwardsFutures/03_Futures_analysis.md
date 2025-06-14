
# 03. Futures & Pricing Models

## 3.1 Overview

Futures contracts are standardized, exchange-traded agreements to buy or sell an asset at a predetermined price on a future date. Unlike forwards, futures involve **daily mark-to-market (MTM)** and require **margin posting**.

* **Key Features:**

  * Standardized contracts
  * Exchange-traded
  * Daily settlement (MTM)
  * Margin requirements (Initial & Maintenance)

* **Payoff at Maturity:**

  ```math
  \text{Payoff}(S_T) = S_T - F_t
  ```

## 3.2 Futures Pricing: Cost-of-Carry Model

* **Futures Price Formula:**

$$
F_t = S_t \cdot e^{(r - q)(T - t)}
$$

  * $S_t$ = Spot price at time $t$
  * $r$ = Risk-free rate
  * $q$ = Continuous dividend yield
  * $T - t$ = Time to maturity

* **Basis:**

$$
\text{Basis} = F_t - S_t
$$


  * Basis converges to zero at expiry.

* **Contango:** Futures > Spot

* **Backwardation:** Futures < Spot

## 3.3 Data Acquisition & Preprocessing

* **Data Source:** Manually download spot & futures price CSVs from the exchange or Yahoo Finance.

* **Files:**

  * `data/NIFTY_spot.csv`
  * `data/NIFTY_futures.csv`

**Steps:**

```python
import pandas as pd

spot = pd.read_csv('data/NIFTY_spot.csv', parse_dates=['Date'], index_col='Date')['Close']
futures = pd.read_csv('data/NIFTY_futures.csv', parse_dates=['Date'], index_col='Date')['Close']

df = pd.DataFrame({'Spot': spot, 'Futures': futures}).dropna()
df.head()
```

## 3.4 Implementation Details

### 3.4.1 Theoretical Futures Price & Basis

```python
import numpy as np

r = 0.05  # risk-free rate
q = 0.00  # assume zero dividend yield
T = pd.to_datetime('2025-06-30')  # futures expiry

df['Tau'] = (T - df.index).days / 365
df['F_theo'] = df['Spot'] * np.exp((r - q) * df['Tau'])
df['Basis'] = df['Futures'] - df['F_theo']
```

### 3.4.2 Plot Spot, Futures & Theoretical Futures

```python
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))
plt.plot(df.index, df['Spot'], label='Spot Price')
plt.plot(df.index, df['Futures'], label='Market Futures')
plt.plot(df.index, df['F_theo'], label='Theoretical Futures', linestyle='--')
plt.title('Spot vs. Futures vs. Theoretical Futures')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.savefig('assets/futures_price_plot.png')
plt.show()
```

![Futures Price Plot](assets/futures_price_plot.png)

### 3.4.3 Basis Plot

```python
plt.figure(figsize=(8, 4))
plt.plot(df.index, df['Basis'])
plt.axhline(0, color='black', lw=0.5)
plt.title('Basis Over Time')
plt.xlabel('Date')
plt.ylabel('Basis')
plt.savefig('assets/futures_basis_plot.png')
plt.show()
```

![Futures Basis Plot](assets/futures_basis_plot.png)

### 3.4.4 Mark-to-Market (MTM) Simulation

```python
contract_size = 75  # NIFTY lot size
df['Delta_PnL'] = (df['Futures'].diff()) * contract_size
df['Cumulative_PnL'] = df['Delta_PnL'].cumsum()

plt.figure(figsize=(10, 5))
plt.plot(df.index, df['Cumulative_PnL'], label='MTM P&L')
plt.title('Mark-to-Market P&L Simulation')
plt.xlabel('Date')
plt.ylabel('Cumulative P&L')
plt.legend()
plt.savefig('assets/futures_mtm_pnl.png')
plt.show()
```

![Futures MTM PnL Plot](assets/futures_mtm_pnl.png)

---

## 3.5 Self-Analysis Summary

* Compared theoretical futures to market prices using cost-of-carry model.
* Tracked **basis behavior** and verified convergence near expiry.
* Simulated **MTM P\&L** and visualized daily P\&L accumulation.
* Observed contract dynamics in both **contango** and **backwardation** phases.

---

## 3.6 Resources

* **Video:** Pricing and Valuation of Futures Contracts (CFA Level I)
* **Video:** What Is Mark-to-Market | MTM | Futures | CFA Level I
* **Notebook:** `notebooks/03_futures_analysis.ipynb`

---

If you like this structure, I can generate the corresponding `.ipynb` for you next.
Shall I proceed?

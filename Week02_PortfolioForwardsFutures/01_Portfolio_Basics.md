# 01. Portfolio Basics

## 1.1 Overview

This section covers the essentials of Modern Portfolio Theory (MPT) applied to a seven‐stock universe:  
`AMZN`, `AAPL`, `TSLA`, `NVDA`, `MSFT`, `META`, `GOOGL`  
We analyze historical price data, compute returns, covariances, and then optimize for various objectives (Sharpe ratio, maximum return under risk constraints, minimum volatility).

We analyze historical price data, compute returns, covariances, and then optimize for various objectives (Sharpe ratio, maximum return under risk constraints, minimum volatility).

## 1.2 Data Acquisition & Preprocessing

- **Data Source**: `yfinance` Python library  
- **Ticker List**:
  - `AMZN` (Amazon)
  - `AAPL` (Apple)
  - `TSLA` (Tesla)
  - `NVDA` (NVIDIA)
  - `MSFT` (Microsoft)
  - `META` (Meta Platforms)
  - `GOOGL` (Alphabet)

For each ticker:
1. Download daily adjusted close prices over a chosen date range.
2. Compute daily log returns:
   $$ r_{t} = \ln\Bigl(\tfrac{P_{t}}{P_{t-1}}\Bigr) $$
3. Clean missing data (if any) by forward-filling or dropping early rows.

## 1.3 Return & Risk Metrics

- **Expected Return Vector** $(\mu)$:  
  $$
    \mu_{i} = \frac{1}{T} \sum_{t=1}^{T} r_{i,t}
  $$
- **Covariance Matrix** $(\Sigma)$:  
  $$
    \Sigma_{ij} = \frac{1}{T-1} \sum_{t=1}^{T} \bigl(r_{i,t} - \bar{r}_{i}\bigr)\bigl(r_{j,t} - \bar{r}_{j}\bigr)
  $$
- **Portfolio Return** $(R_p)$:  
  $$
    R_{p} = w^\top \mu
  $$
- **Portfolio Variance** $(\sigma_{p}^{2})$:  
  $$
    \sigma_{p}^{2} = w^\top \Sigma \, w
  $$
- **Portfolio Standard Deviation** $(\sigma_{p})$:  
  $$
    \sigma_{p} = \sqrt{\,w^\top \Sigma \, w\,}
  $$
  
Here, $w = [w_{1}, w_{2}, \ldots, w_{7}]^\top$ are portfolio weights (with $\sum_{i=1}^{7} w_{i} = 1$ and $w_{i} \ge 0$).

## 1.4 Optimization Objectives

### 1.4.1 Sharpe Ratio Maximization  
Maximize
$$
  \mathrm{Sharpe}(w) \;=\; \frac{\,w^\top \mu \;-\; r_{f}\,}{\sqrt{\,w^\top \Sigma \, w\,}}
$$
subject to  
$$
  \sum_{i=1}^{7} w_{i} = 1, \quad w_{i} \ge 0.
$$
- $r_{f}$ is the risk-free rate (e.g., 2%).

**Notebook**: [`sharpe_maximum_MPT.ipynb`](./notebooks/sharpe_maximum_MPT.ipynb)  
**Key steps**:
1. Define objective = $-\mathrm{Sharpe}(w)$ (for minimization).
2. Use `scipy.optimize.minimize` with constraints (weights sum to 1, nonnegativity).
3. Plot efficient frontier by varying feasible weight combinations.

### 1.4.2 Return Maximization under Risk Constraint  
Maximize
$$
  w^\top \mu
$$
subject to  
$$
  w^\top \Sigma \, w \;\le\; \sigma_{\max}^{2}, 
  \quad \sum_{i=1}^{7} w_{i} = 1, 
  \quad w_{i} \ge 0.
$$
- $\sigma_{\max}$ is a chosen volatility cap.

**Notebook**: [`returns_max_MPT.ipynb`](./notebooks/returns_max_MPT.ipynb)  
**Key steps**:
1. Specify $\sigma_{\max}$ (e.g., 0.02 daily).
2. Use `scipy.optimize.minimize` with inequality constraint on variance.
3. Generate return-risk tradeoff curve by varying $\sigma_{\max}$.

### 1.4.3 Minimum Volatility Portfolio  
Minimize
$$
  w^\top \Sigma \, w
$$
subject to  
$$
  \sum_{i=1}^{7} w_{i} = 1,\quad w_{i} \ge 0.
$$
– Purely a risk-parity approach (no explicit return target).

**Notebook**: [`std_dev_min_MPT.ipynb`](./notebooks/std_dev_min_MPT.ipynb)  
**Key steps**:
1. Define objective = $w^\top \Sigma \, w$.
2. Apply weight constraints as above.
3. Compare resulting weights to Sharpe-maximizing solution.

## 1.5 Visualizations

- **Efficient Frontier Plot**: Risk ($\sigma_{p}$) vs. Return ($R_{p}$), highlighting each optimized portfolio.  
- **Weight Composition**: Bar charts showing allocation per ticker for each optimized solution.  
- **Cumulative Returns**: Time series comparison of each portfolio’s historical performance.

*(When generated, save all plots into `assets/` and embed as needed.)*

---

> **Note**: As you add Forwards and Futures content, revisit this file for cross-references (e.g., hedging with futures in a portfolio context).

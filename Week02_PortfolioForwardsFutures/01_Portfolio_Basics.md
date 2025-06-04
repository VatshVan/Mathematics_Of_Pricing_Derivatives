# 01. Portfolio Basics

## 1.1 Overview

This section covers the essentials of Modern Portfolio Theory (MPT) applied to a seven‐stock universe:  
`AMZN`, `AAPL`, `TSLA`, `NVDA`, `MSFT`, `META`, `GOOGL`  
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
  <div align="center">

  $$\mu_{i} = \frac{1}{T} \sum_{t=1}^{T} r_{i,t}$$
</div>
  
- **Covariance Matrix** $$(\Sigma)$$:

<div align="center">

$$\Sigma_{ij} = \frac{1}{T-1} \sum_{t=1}^{T} \bigl(r_{i,t} - \bigl(r_{i}\bigr)\bigl(r_{j,t}\bigr) - \bar{r}_{j}\bigr)$$

</div>


- **Portfolio Return** $(R_p)$:

<div align="center">

  $$R_{p} = w^\top \mu$$

</div>

- **Portfolio Variance** $(\sigma_{p}^{2})$:  
  
<div align="center">

  $$\sigma_{p}^{2} = w^\top \Sigma \, w$$

</div>
  
- **Portfolio Standard Deviation** $(\sigma_{p})$:  

<div align="center">

  $$\sigma_{p} = \sqrt{\,w^\top \Sigma \, w\,}$$

</div>

Here, $w = [w_{1}, w_{2}, \ldots, w_{7}]^\top$ are portfolio weights (with $\sum_{i=1}^{7} w_{i} = 1$ and $w_{i} \ge 0$).

## 1.4 Optimization Objectives

### 1.4.1 Sharpe Ratio Maximization  
Maximize

<div align="center">

  $$\mathrm{Sharpe}(w) \\;=\\; \frac{\\,w^\top \mu \\;-\\; r_{f}\\,}{\sqrt{\\,w^\top \Sigma \\, w\\,}}$$

</div>

subject to 

<div align="center">

  $$\sum_{i=1}^{7} w_{i} = 1, \quad w_{i} \ge 0.$$

</div>

- $r_{f}$ is the risk-free rate (e.g., 2%).

**Notebook**: [`sharpe_maximum_MPT.ipynb`](./notebooks/sharpe_maximum_MPT.ipynb)  
**Key steps**:
1. Define objective = $-\mathrm{Sharpe}(w)$ (for minimization).
2. Use `scipy.optimize.minimize` with constraints (weights sum to 1, nonnegativity).
3. Plot efficient frontier by varying feasible weight combinations.

### 1.4.2 Return Maximization under Risk Constraint  
Maximize $$w^\top \mu$$ subject to 
<div align = ""center>

  $$w^\top \Sigma \, w \;\le\; \sigma_{\max}^{2}, 
  \quad \sum_{i=1}^{7} w_{i} = 1, 
  \quad w_{i} \ge 0.$$

</div>

- $\sigma_{\max}$ is a chosen volatility cap.

**Notebook**: [`returns_max_MPT.ipynb`](./notebooks/returns_max_MPT.ipynb)  
**Key steps**:
1. Specify $\sigma_{\max}$ (e.g., 0.02 daily).
2. Use `scipy.optimize.minimize` with inequality constraint on variance.
3. Generate return-risk tradeoff curve by varying $\sigma_{\max}$.

### 1.4.3 Minimum Volatility Portfolio  
Minimize $$w^\top \Sigma \, w$$ subject to  

<div align = "center">
  
$$\sum_{i=1}^{7} w_{i} = 1,\quad w_{i} \ge 0.$$

</div>

- Purely a risk-parity approach (no explicit return target).

**Notebook**: [`std_dev_min_MPT.ipynb`](./notebooks/std_dev_min_MPT.ipynb)  
**Key steps**:
1. Define objective = $w^\top \Sigma \, w$.
2. Apply weight constraints as above.
3. Compare resulting weights to Sharpe-maximizing solution.

## 1.5 Visualizations

- **Efficient Frontier Plot**: Risk ($\sigma_{p}$) vs. Return ($R_{p}$), highlighting each optimized portfolio.  
- **Weight Composition**: Bar charts showing allocation per ticker for each optimized solution.  
- **Cumulative Returns**: Time series comparison of each portfolio’s historical performance.

<!--*(When generated, save all plots into `assets/` and embed as needed.)*-->

## 1.6 Code Implementation

All implementation code resides in the `notebooks/` directory. The following Jupyter notebooks demonstrate the full workflows:

- **`sharpe_maximum_MPT.ipynb`**  
  - Fetches historical price data via `yfinance`.  
  - Computes daily log returns, expected return vector ($\mu$), and covariance matrix ($\Sigma$).  
  - Implements Sharpe ratio maximization:  
    ```python
    # Objective: negative Sharpe ratio
    def neg_sharpe(weights, mu, Sigma, rf):
        port_return = weights.dot(mu)
        port_vol = np.sqrt(weights.T @ Sigma @ weights)
        return -(port_return - rf) / port_vol
    ```
  - Uses `scipy.optimize.minimize` with weight constraints to find optimal $w^*$.  
  - Plots the resulting efficient frontier.

- **`returns_max_MPT.ipynb`**  
  - Similar data preprocessing steps as above.  
  - Implements return maximization under a volatility cap $\sigma_{\max}$:  
    ```python
    # Constraints: portfolio variance ≤ sigma_max^2
    constraints = (
        {'type': 'eq', 'fun': lambda w: np.sum(w) - 1},
        {'type': 'ineq', 'fun': lambda w: sigma_max**2 - w.T @ Sigma @ w}
    )
    ```
  - Solves for weights $w^*$ maximizing $w^\top \mu$ given the variance constraint.  
  - Generates the return‐risk tradeoff by varying $\sigma_{\max}$.

- **`std_dev_min_MPT.ipynb`**  
  - Data loading and preprocessing as above.  
  - Implements minimum‐variance objective:  
    ```python
    # Objective: portfolio variance
    def portfolio_var(weights, Sigma):
        return weights.T @ Sigma @ weights
    ```
  - Applies weight constraints (sum to 1, nonnegativity) to minimize variance.  
  - Compares resulting weights and risk level with Sharpe‐maximizing portfolio.

Each notebook is fully reproducible and includes explanatory Markdown cells, code cells, and visualization outputs. To run them:

1. Navigate to the `notebooks/` folder.
2. Launch Jupyter Lab or Notebook:  
   ```bash
   cd notebooks
   jupyter notebook

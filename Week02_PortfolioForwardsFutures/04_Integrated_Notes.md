# 📘 Week 2 Integrated Notes

**Portfolio, Forwards, and Futures – Summary and Self-Analysis**

---

## 1. Portfolio Optimization: Risk-Return Tradeoff

### 📂 Overview

Applied **Modern Portfolio Theory (MPT)** to a 7-stock universe:

* `AMZN`, `AAPL`, `TSLA`, `NVDA`, `MSFT`, `META`, `GOOGL`

### 📊 Key Learnings

* Portfolio return:

  $$
  R_p = w^\top \mu
  $$
* Portfolio variance:

$$
\sigma_p^2 = w^\top \Sigma w
$$

  
* Sharpe Ratio:

$$
\text{Sharpe}(w) = \frac{w^\top \mu - r_f}{\sqrt{w^\top \Sigma w}}
$$


### 🔍 Analysis

* Constructed portfolios by:

  * Maximizing Sharpe Ratio
  * Maximizing returns under volatility constraints
  * Minimizing portfolio variance
* Visualized **efficient frontiers, weight compositions, and cumulative returns.**
* Self-analysis included sensitivity to stock selections and correlation effects.

### ✅ Key Takeaways

* Lower correlation between stocks improves diversification.
* Sharpe-optimal portfolios are more balanced than return-maximizing portfolios.

---

## 2. Forwards: Pricing and Arbitrage

### 📂 Overview

Explored **OTC forward contracts** using:

* **Continuous dividend yield model:**

$$
F_0 = S_0 \cdot e^{(r - q) T}
$$
  
* **Discrete dividend adjustment:**

$$
F_0 = (S_0 - \text{PV(div)}) \cdot e^{r T}
$$

### 📊 Key Learnings

* Calculated forward prices using both continuous and discrete dividend models.
* Built **payoff tables** under multiple price scenarios.
* Identified **arbitrage strategies:**

  * Cash-and-carry
  * Reverse carry

### 🔍 Analysis

* Verified payoff sensitivity across spot price scenarios.
* Visualized forward payoff diagrams.
* Compared theoretical forward prices with market prices to validate arbitrage opportunities.

### ✅ Key Takeaways

* Forward pricing is sensitive to dividend assumptions.
* Arbitrage conditions can be practically modeled and validated.

---

## 3. Futures: Pricing, Basis, and MTM Simulation

### 📂 Overview

Studied **futures contracts and daily MTM processes.**

* Futures price:

$$
F_t = S_t \cdot e^{(r - q)(T - t)}
$$

* Basis:

$$
\text{Basis} = F_t - S_t
$$


### 📊 Key Learnings

* Compared **theoretical vs. market futures prices.**
* Simulated **mark-to-market (MTM) P\&L** using daily price changes.
* Tracked **basis convergence** as expiry approached.

### 🔍 Analysis

* Observed both **contango and backwardation** market phases.
* Basis plots confirmed theoretical convergence behavior.
* MTM simulations helped understand P\&L tracking over contract duration.

### ✅ Key Takeaways

* MTM margining is a critical risk management component.
* Basis can temporarily diverge but must converge by expiry.

---

## 📦 Self-Analysis Summary

* Built a comprehensive understanding of **portfolios, forwards, and futures.**
* Transitioned from theory to **practical implementation** using Python and real data.
* Developed strong skills in **data cleaning, scenario analysis, visualization, and arbitrage modeling.**
* Gained confidence in identifying real-world trading opportunities using pricing models.

---

## 📚 Resources

* Portfolio Optimization: CFA Level I Videos, Python tutorials
* Forwards: CFA Level II Videos, FinQuiz Pro tutorials
* Futures: CFA Level I Videos, MTM tutorials
* Practical Datasets: Manually sourced from NSE India

---

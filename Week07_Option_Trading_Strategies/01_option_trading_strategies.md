# Option Trading Strategies

---

## Purpose of Option Strategies

Options can be combined into **structured positions** to:
- Speculate on **market direction** (bullish/bearish)
- Profit from **volatility expectations**
- Limit **risk and loss**
- **Cap gains** for better-defined outcomes

These combinations are called **option strategies**. Most involve multiple options at different strikes or types (call/put), creating unique **payoff profiles**.

---

## Basics: Payoff of a Single Option

- **Long Call**: $$\( \max(S_T - K, 0) - \text{Premium} \)$$
- **Long Put**: $$\( \max(K - S_T, 0) - \text{Premium} \)$$
- **Short Call**: $$\( -\max(S_T - K, 0) + \text{Premium} \)$$
- **Short Put**: $$\( -\max(K - S_T, 0) + \text{Premium} \)$$

All complex strategies build on these.

---

## 1. Vertical Spreads

### A. Bull Call Spread

**Construction**:
- Buy 1 Call at Strike $$\( K_1 \)$$
- Sell 1 Call at Strike $$\( K_2 > K_1 \)$$

**Net Premium**: $$\( \text{Debit} \)$$

**Payoff**:
$$\begin{cases}
0, & S_T \leq K_1 \\
S_T - K_1, & K_1 < S_T < K_2 \\
K_2 - K_1, & S_T \geq K_2
\end{cases}
- \text{Net Premium}$$

**Limited Loss, Limited Profit**  
Used when mildly bullish.

---

### B. Bear Put Spread

**Construction**:
- Buy 1 Put at $$\( K_2 \)$$
- Sell 1 Put at $$\( K_1 < K_2 \)$$

**Net Premium**: $$\( \text{Debit} \)$$

**Payoff**: Profit if market goes **down**

---

## 2. Volatility Strategies

### A. Long Straddle

**Construction**:
- Buy 1 ATM Call + 1 ATM Put  
  (both at strike $$\( K \)$$)

**Payoff**:
$$
\max(S_T - K, 0) + \max(K - S_T, 0) - \text{Premium}
$$

**Unlimited profit in either direction**  
High cost

Used when **expecting big moves**, regardless of direction

---

### B. Long Strangle

**Construction**:
- Buy 1 OTM Call @ $$\( K_2 \)$$
- Buy 1 OTM Put @ $$\( K_1 \)$$

**Cheaper than straddle** but needs larger movement to profit  
Used for volatility plays at lower cost

---

## 3. Butterfly Spread (Neutral Strategy)

**Construction**:
- Buy 1 Call @ $$\( K_1 \)$$
- Sell 2 Calls @ $$\( K_2 \)$$
- Buy 1 Call @ $$\( K_3 \)$$

Where $$\( K_1 < K_2 < K_3 \)$$, typically $$\( K_2 \)$$ is ATM

**Payoff**:
$$
\text{Maximum at } S_T = K_2
$$

Limited risk & reward  
Profits if stock **stays near middle strike**

---

## 4. Iron Condor (Range-Bound Strategy)

**Construction**:
- Sell 1 OTM Put @ $$\( K_1 \)$$, Buy 1 Put @ $$\( K_0 \)$$
- Sell 1 OTM Call @ $$\( K_2 \)$$, Buy 1 Call @ $$\( K_3 \)$$

**Combination**:  
= Bull Put Spread + Bear Call Spread

Max profit when **stock stays between \( K_1 \) and \( K_2 \)**  
Loses only if stock moves **too far in either direction**

Used in **low-volatility environments**

---

## 5. Max Profit/Loss Summary

| Strategy        | Max Profit            | Max Loss             | Breakevens                   |
|----------------|------------------------|-----------------------|------------------------------|
| Bull Call      | $$\( K_2 - K_1 - \text{net premium} \)$$ | $$\( \text{net premium} \)$$     | $$\( K_1 + \text{net premium} \)$$ |
| Bear Put       | \( K_2 - K_1 - \text{net premium} \) | \( \text{net premium} \)     | \( K_2 - \text{net premium} \)$$ |
| Straddle       | Unlimited               | Total premium         | $$\( K ± \text{premium} \)$$     |
| Strangle       | Unlimited               | Total premium         | $$\( K_1 - \text{put prem}, K_2 + \text{call prem} \)$$ |
| Iron Condor    | Net premium received    | \( \text{spread} - \text{premium} \) | 2 breakeven points between spreads |

---

## 6. Visual Payoff Summary (to be plotted in notebook)

Each strategy produces a **distinct payoff diagram**, showing:
- Region of profits/losses
- Flat, capped, or V-shaped structures
- Risk/reward trade-off clearly visible

---

## 7. Strategy Selection Table

| Strategy       | View on Price | View on Volatility | Risk     | Reward   |
|----------------|---------------|---------------------|----------|----------|
| Bull Call      | Mild Bullish  | Neutral             | Limited  | Limited  |
| Bear Put       | Mild Bearish  | Neutral             | Limited  | Limited  |
| Long Straddle  | Neutral       | High                | High     | Unlimited|
| Long Strangle  | Neutral       | High                | Medium   | Unlimited|
| Iron Condor    | Sideways      | Low                 | Limited  | Limited  |
| Butterfly      | Sideways      | Low                 | Limited  | Limited  |

---

## Key Insights

- **Premium paid/received** is critical to breakeven
- **Volatility and direction** expectations determine choice
- **Visual payoff** reveals risk profile — easier to reason about

---


Simulate and plot each strategy over a range of underlying prices in:

`notebooks/01_option_trading_strategies.ipynb`


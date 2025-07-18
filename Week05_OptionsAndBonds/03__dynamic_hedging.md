# Dynamic Hedging and Delta Neutral Strategies

---

## 1. What is Dynamic Hedging?

Dynamic hedging is a trading technique used to hedge the risk of an option position by **continuously rebalancing** the position in the underlying asset. It ensures that the overall portfolio remains **delta-neutral** as the market evolves.

---

## 2. The Need for Dynamic Adjustments

- **Delta (Δ)** of an option changes with:
  - Stock price
  - Time decay
  - Volatility shifts
- A hedge constructed at time $$\( t_0 \)$$ will become **ineffective** over time unless adjusted.

---

## 3. Delta-Neutral Portfolio

To hedge a **short call**, one would:
- Buy $$\( \Delta \)$$ shares of the underlying
- This ensures the **portfolio value changes ≈ 0** for small changes in stock price

Let:
- $$\( V(S, t) \)$$: Option value
- $$\( \Pi = -V + \Delta S \)$$: Portfolio value

Choose $$\( \Delta = \frac{\partial V}{\partial S} \)$$

Then the portfolio becomes **locally riskless** and earns the **risk-free rate**:
$$
d\Pi = r \Pi dt
$$

This is the logic that leads to the Black-Scholes PDE.

---

## 4. Discrete-Time Simulation

In reality:
- You can’t rebalance continuously
- Traders rebalance at discrete time steps (every hour/day)

Simulation involves:
1. Compute **option delta** at each step
2. Adjust holdings in stock to match new delta
3. Track **PnL** from:
   - Changes in option value
   - Gains/losses in stock
   - Interest on cash position

---

## 5. Practical Risks

| Issue                  | Impact                            |
|------------------------|-----------------------------------|
| **Gap Risk**           | Price jumps between rebalances    |
| **Transaction Costs**  | Frequent rebalancing costs        |
| **Gamma Risk**         | Second-order sensitivity ignored  |
| **Volatility Misestimation** | Delta relies on σ estimate |

---

## 6. Summary

Dynamic hedging provides:
- A **practical method** to replicate options
- A deep insight into **risk management**
- A foundation for **BSM pricing** via replication

But also introduces:
- Slippage
- Costs
- Sensitivity to volatility and jump risk

---

## Simulate delta hedging of a call option using Black-Scholes ∆ and show hedging error vs number of rebalances.

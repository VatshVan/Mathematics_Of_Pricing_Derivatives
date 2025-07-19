# Continuous-Time Models in Derivative Pricing

---

## Motivation

As we refine the time step $$\( \Delta t \to 0 \)$$, binomial models converge to **continuous-time stochastic processes**.

The most foundational is the **Black-Scholes-Merton framework**, which models the asset price via a **Geometric Brownian Motion (GBM)**.

---

## 1. Geometric Brownian Motion (GBM)

$$dS_t = \mu S_t \, dt + \sigma S_t \, dW_t$$

Where:
- $$\( S_t \)$$: asset price at time \( t \)
- $$\( \mu \)$$: drift (expected return)
- $$\( \sigma \)$$: volatility
- $$\( W_t \)$$: standard Brownian motion (Wiener process)

Solution:
$$S_t = S_0 \exp\left[ \left(\mu - \frac{1}{2} \sigma^2\right)t + \sigma W_t \right]$$

---

## 2. No-Arbitrage and Risk-Neutral World

In a risk-neutral measure $$\( \mathbb{Q} \)$$, drift becomes $$\( r \)$$:

$$dS_t = r S_t \, dt + \sigma S_t \, dW_t^{\mathbb{Q}}$$

The price of a derivative becomes:

$$V_t = \mathbb{E}^{\mathbb{Q}} \left[ e^{-r(T - t)} \cdot \text{Payoff}(S_T) \mid \mathcal{F}_t \right]$$

This is the **risk-neutral valuation formula**.

---

## 3. Black-Scholes PDE

Using **Ito’s Lemma**, we derive a partial differential equation:

$$
\frac{\partial V}{\partial t} + r S \frac{\partial V}{\partial S} + \frac{1}{2} \sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} = r V
$$

Boundary condition:
- For a call: $$\( V(T, S) = \max(S - K, 0) \)$$

Solving this PDE yields the **Black-Scholes formula**.

---

## 4. Risk-Neutral Pricing via Martingales

The discounted asset price under $$\( \mathbb{Q} \)$$ is a **martingale**:

$$
\tilde{S}_t = e^{-rt} S_t \Rightarrow \mathbb{E}^{\mathbb{Q}}[\tilde{S}_T \mid \mathcal{F}_t] = \tilde{S}_t
$$

Hence, derivative price:

$$V_t = e^{-r(T - t)} \mathbb{E}^{\mathbb{Q}}[\text{Payoff}]$$

---

## 5. Black-Scholes Closed Form

For a European Call:

$$C = S_0 \Phi(d_1) - K e^{-rT} \Phi(d_2)$$

Where:
- $$\( d_1 = \frac{\ln(S_0/K) + (r + \sigma^2/2) T}{\sigma \sqrt{T}} \)$$
- $$\( d_2 = d_1 - \sigma \sqrt{T} \)$$

This comes from solving the PDE or computing the expectation directly using GBM.

---

## 6. Interpretation

| Concept                  | Continuous Model Counterpart     |
|--------------------------|----------------------------------|
| Tree                    | Brownian Motion Path              |
| Risk-neutral probability | Change of measure (via Girsanov) |
| Backward induction      | PDE or expectation               |

---

## 7. Discrete → Continuous Transition

| Feature      | Binomial Model     | BSM Model                        |
|--------------|--------------------|----------------------------------|
| Time         | Discrete \( \Delta t \) | Continuous \( dt \)                |
| Price Move   | \( u, d \)          | GBM + Brownian motion            |
| Risk-Neutral | Explicit \( p \)    | Girsanov transform               |
| Pricing      | Backward Induction  | PDE / expectation under \( \mathbb{Q} \) |

---

## Summary

- GBM forms the foundation of continuous-time finance
- Black-Scholes model comes from martingale pricing + Ito calculus
- Risk-neutral pricing remains central in both discrete and continuous worlds

---

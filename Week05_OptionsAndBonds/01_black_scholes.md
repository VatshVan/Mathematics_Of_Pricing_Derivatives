# 13 — Black-Scholes Pricing Model

---

## 1. Introduction

The **Black-Scholes-Merton (BSM) model** is a cornerstone of modern financial theory. It provides a **closed-form solution** to price European-style call and put options under a set of well-defined assumptions.

Developed in 1973 by Fischer Black, Myron Scholes and later extended by Robert Merton, the model revolutionized financial markets by introducing a **no-arbitrage, replication-based framework** for derivative pricing.

---

## 2. Assumptions

For the BSM model to hold, the following assumptions are made:

- The underlying asset price follows **Geometric Brownian Motion (GBM)**.
- No arbitrage opportunities exist.
- Markets are **frictionless** (no transaction costs or taxes).
- Trading is **continuous** and **infinitely divisible**.
- The **risk-free rate (r)** is constant and known.
- **Volatility (σ)** is constant and known.
- The asset pays **no dividends** during the life of the option.
- The option is **European-style**, i.e., exercisable only at expiration.

---

## 3. Asset Price Dynamics

The price of the underlying asset Sₜ evolves according to the stochastic differential equation:

$$
dS_t = \mu S_t dt + \sigma S_t dW_t
$$


- $$\( \mu \)$$: drift (expected return under real-world measure \( \mathbb{P} \))
- $$\( \sigma \)$$: volatility
- $$\( dW_t \)$$: increment of a Wiener process (Brownian motion)

---

## 4. Risk-Neutral Valuation

To price derivatives, we shift to a **risk-neutral measure** $$\( \mathbb{Q} \)$$ where the expected return on all assets is the **risk-free rate (r)**:

$$
dS_t = r S_t dt + \sigma S_t dW_t^{\mathbb{Q}}
$$

In this measure, the price of a derivative is the **discounted expected payoff**:

$$
V_t = \mathbb{E}^{\mathbb{Q}} \left[ e^{-r(T - t)} \cdot \text{Payoff}(S_T) \mid \mathcal{F}_t \right]
$$

---

## 5. Derivation Sketch: Replicating Portfolio and PDE

Using **delta hedging**, we construct a self-financing portfolio:

$$
\Pi = V - \Delta S
$$

where $$\( \Delta = \frac{\partial V}{\partial S} \)$$  is the hedge ratio.

Using Itô’s Lemma and risk-neutral no-arbitrage conditions, we derive the **Black-Scholes partial differential equation (PDE)**:

$$
\frac{\partial V}{\partial t} + \frac{1}{2} \sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} + r S \frac{\partial V}{\partial S} - r V = 0
$$

Solving this PDE with terminal condition $$\( V(S_T) = \max(S_T - K, 0) \)$$ (for call) leads to the BSM formula.

---

## 6. Black-Scholes Formulas

Let:

$$
d_1 = \frac{\ln\left(\frac{S}{K}\right) + \left( r + \frac{\sigma^2}{2} \right) T}{\sigma \sqrt{T}}, \quad
d_2 = d_1 - \sigma \sqrt{T}
$$

Then:

- **European Call Option**:

$$
C = S N(d_1) - K e^{-rT} N(d_2)
$$

- **European Put Option**:

$$
P = K e^{-rT} N(-d_2) - S N(-d_1)
$$

Where $$\( N(x) \)$$ is the cumulative distribution function (CDF) of the standard normal distribution.

---

## 7. Interpretation

| Term | Financial Meaning |
|------|-------------------|
| $$\( d_1 \)$$ | Proxy for moneyness + time value |
| $$\( N(d_1) \)$$ | Risk-neutral probability that the option finishes in-the-money |
| $$\( d_2 \)$$ | Adjusted moneyness |
| $$\( N(d_2) \)$$ | Probability the call will be exercised |

The call option value is interpreted as the **present value of expected gain**, under risk-neutral measure.

---

## 8. Greeks: Sensitivities

Greeks describe how the option price responds to small changes in input parameters.

| Greek | Formula | Meaning |
|-------|---------|---------|
| **Delta (Δ)** | $$\( N(d_1) \)$$ | Sensitivity to underlying price |
| **Gamma (Γ)** | $$\( \frac{N'(d_1)}{S \sigma \sqrt{T}} \)$$ | Rate of change of delta |
| **Vega** | $$\( S N'(d_1) \sqrt{T} \)$$ | Sensitivity to volatility |
| **Theta (Θ)** | $$\( - \frac{S N'(d_1) \sigma}{2 \sqrt{T}} - rK e^{-rT} N(d_2) \)$$ | Sensitivity to time (decay) |
| **Rho (ρ)** | $$\( K T e^{-rT} N(d_2) \)$$ | Sensitivity to interest rate |

> $$\( N'(d_1) \)$$ : standard normal PDF

---

## 9. Visual Behavior

- **Delta** is close to 1 for deep ITM calls, 0 for OTM.
- **Gamma** peaks at ATM and declines on both sides.
- **Theta** is negative — options lose value over time.
- **Vega** increases with T and peaks at ATM.
- **Rho** is more impactful for long-term options.

You can plot Greeks with respect to:
- Stock Price (S)
- Volatility (σ)
- Time to Expiry (T)

---

## 10. Real-World Applications

- Option valuation in financial markets
- **Implied volatility estimation**
- **Hedging portfolios** using ∆-neutral or ∆Γ-neutral strategies
- **Trading strategies** like straddles, spreads
- Risk management tools for Greeks exposure

---

## 11. Limitations

- Assumes constant volatility and interest rate
- No early exercise (European only)
- No dividends
- No jumps in price (purely continuous)

Extensions include:
- Black-Scholes with Dividends
- American Option Approximations
- Stochastic Volatility Models (e.g. Heston)

---

## 12. Summary

The BSM model provides elegant, powerful insight into **option pricing under uncertainty**. It enables both theoretical valuation and practical hedging, and forms the mathematical base of most modern derivatives pricing engines.

# Discrete Time Models: Binomial Option Pricing

---

## Motivation

Continuous-time models (like Black-Scholes) assume perfect, frictionless markets and require advanced calculus.

Binomial models provide:
- A **simple**, **intuitive** way to price options
- A **discrete-time approximation** to Black-Scholes
- Flexibility to price **American options** (early exercise)

---

## 1. Binomial Tree Basics

### Single-period Binomial Model:
Assume:
- Current stock price: $$\( S_0 \)$$
- In 1 period:
  - Price moves up to $$\( S_u = u \cdot S_0 \)$$
  - Or down to $$\( S_d = d \cdot S_0 \)$$
- Risk-free interest rate: $$\( r \)$$

Risk-neutral probability:

$$p = \frac{e^{r \Delta t} - d}{u - d}$$

Option value at time 0:
$$C_0 = e^{-r \Delta t} \cdot \left[ p \cdot C_u + (1 - p) \cdot C_d \right]$$

---

## 2. Multi-Period Binomial Tree

Build a **recombining tree** of stock prices:
- Each node has 2 branches: up/down
- Use backward induction to compute option value at each node

At maturity:

$$C_T(i) = \max(0, S_T(i) - K) \quad \text{(for call)}$$

At earlier steps:

$$C_t(i) = \max( \text{exercise value}, \; e^{-r \Delta t} \cdot [p \cdot C_{t+1}^{up} + (1 - p) \cdot C_{t+1}^{down}] )$$

---

## 3. Cox-Ross-Rubinstein (CRR) Model

Popular parameterization:
- $$\( u = e^{\sigma \sqrt{\Delta t}} \)$$
- $$\( d = \frac{1}{u} = e^{-\sigma \sqrt{\Delta t}} \)$$
- Ensures no arbitrage and recombining structure

$$p = \frac{e^{r \Delta t} - d}{u - d}$$

As $$\( N \to \infty \)$$, CRR prices → Black-Scholes

---

## 4. European vs American Options

- **European**: Can only be exercised at maturity
- **American**: Can be exercised anytime

Binomial models naturally support American pricing:
$$C_t(i) = \max( \text{exercise value}, \text{continuation value} )$$

---

## 5. Algorithm Summary

1. Build terminal prices at $$\( T \)$$
2. Compute option payoff at leaf nodes
3. Work backward using risk-neutral expectation
4. At each step:
   - For American: take max(payoff, continuation)
   - For European: use continuation only

---

## 6. Extensions

- Put-Call Parity:
  $$C - P = S - K e^{-rT}$$

- Delta Hedging:
  $$\Delta = \frac{C_u - C_d}{S_u - S_d}$$

- Greeks approximation via finite differences

---

## 7. Use Cases

- Academic derivation
- American options
- Barrier/early-exercise models
- Teaching risk-neutral thinking

---

## Code a binomial tree pricing engine for Euro + American options

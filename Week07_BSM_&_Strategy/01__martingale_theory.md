# Martingale Theory in Continuous Time

---

## Objective

Introduce **martingales** in continuous-time stochastic processes and show how they form the **foundation of modern option pricing** under the **risk-neutral measure**.

This leads to:
- Pricing via expected values
- No-arbitrage condition
- Black-Scholes derivation via martingales

---

## 1. What is a Martingale?

A process $$\( M_t \)$$ is a **martingale** with respect to filtration $$\( \mathcal{F}_t \)$$ if:

$$\mathbb{E}[M_t | \mathcal{F}_s] = M_s \quad \text{for all } s < t$$

**Interpretation**:  
→ Future expected value = current value (no drift, fair game)

---

## 2. Stock Prices Are *Not* Martingales

In the real-world probability measure $$\( \mathbb{P} \)$$, the asset follows:

$$dS_t = \mu S_t dt + \sigma S_t dW_t^\mathbb{P}$$

Here, $$\( \mu \neq r \)$$, so:

$$\mathbb{E}^\mathbb{P}[S_t | \mathcal{F}_s] \neq S_s$$

Not a martingale.

---

## 3. Risk-Neutral Measure $$\( \mathbb{Q} \)$$

We **change measure** from $$\( \mathbb{P} \to \mathbb{Q} \)$$ using **Girsanov’s Theorem**:

Under $$\( \mathbb{Q} \)$$, the drift changes:

$$dS_t = r S_t dt + \sigma S_t dW_t^\mathbb{Q}$$

This makes the **discounted stock price** a **martingale**:

$$\tilde{S}_t = e^{-rt} S_t \quad \Rightarrow \quad \mathbb{E}^\mathbb{Q}[\tilde{S}_T | \mathcal{F}_t] = \tilde{S}_t$$

This satisfies **no-arbitrage** conditions.

---

## 4. Pricing via Martingales

The price $$\( V_t \)$$ of any contingent claim $$\( H(S_T) \)$$ is:

$$V_t = e^{-r(T - t)} \mathbb{E}^\mathbb{Q}[H(S_T) | \mathcal{F}_t]$$

This is the **fundamental pricing equation** under risk-neutral martingale framework.

For a European call option:

$$V_0 = e^{-rT} \mathbb{E}^\mathbb{Q}[\max(S_T - K, 0)]$$

---

## 5. Black-Scholes Derivation via Martingale Method

Steps:
1. Assume stock follows $$\( dS_t = r S_t dt + \sigma S_t dW_t^\mathbb{Q} \)$$
2. Solve SDE for $$\( S_T \)$$: lognormal
3. Plug into the expectation for $$\( \max(S_T - K, 0) \)$$
4. Use change of variable to derive closed-form BSM formula

---

## 6. Replication via Martingales

The martingale representation theorem tells us:

> Any martingale can be written as a stochastic integral.

This underpins:
- Hedging strategies (replicate payoff via dynamic position)
- Completeness of the Black-Scholes market

---

## 7. Summary Table

| Concept                     | Meaning                                  |
|----------------------------|------------------------------------------|
| Martingale                 | No drift in expectation                  |
| Risk-neutral measure $$\( \mathbb{Q} \)$$ | Asset grows at risk-free rate          |
| Girsanov’s Theorem         | Changes drift from $$\( \mu \) to \( r \)$$ |
| Pricing Formula            | $$\( V_t = e^{-r(T - t)} \mathbb{E}^\mathbb{Q}[H] \)$$ |
| Replication Theorem        | Hedge = stochastic integral              |

---

## Applications

- Pricing all European-style options
- Basis for Monte Carlo simulation
- Theoretical base for PDE methods

---

##
Implement pricing via risk-neutral expectations using:

`notebooks/01_martingale_pricing.ipynb`

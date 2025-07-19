# Black-Scholes PDE Derivation (Delta Hedging)

---

## Objective

Derive the **Black-Scholes Partial Differential Equation (PDE)** by:
- Modeling asset dynamics as a stochastic differential equation (SDE)
- Using **Itô’s Lemma** on the option price function
- Constructing a **riskless hedged portfolio**
- Applying **no-arbitrage** conditions

---

## 1. Asset Price Model (GBM)

We assume stock follows:

$$dS_t = \mu S_t dt + \sigma S_t dW_t$$

Let $$\( V(S, t) \)$$ be the value of a European option.

---

## 2. Itô’s Lemma Applied to $$\( V(S, t) \)$$

$$dV = \left( \frac{\partial V}{\partial t} + \mu S \frac{\partial V}{\partial S} + \frac{1}{2} \sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} \right) dt + \sigma S \frac{\partial V}{\partial S} dW_t$$

---

## 3. Construct Hedged Portfolio

We hold:
- Long 1 option worth $$\( V \)$$
- Short $$\( \Delta = \frac{\partial V}{\partial S} \)$$ shares of the stock

Then portfolio value:

$$\Pi = V - \Delta S$$

Change in value:

$$d\Pi = dV - \Delta dS$$

Substitute expressions:

$$d\Pi = \left( \frac{\partial V}{\partial t} + \frac{1}{2} \sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} \right) dt$$

**No $$\( dW_t \)$$** → riskless

---

## 4. Apply No-Arbitrage Condition

Riskless portfolio should earn risk-free rate:

$$d\Pi = r \Pi dt = r (V - \Delta S) dt$$

Equating both expressions for $$\( d\Pi \)$$:

$$\frac{\partial V}{\partial t} + \frac{1}{2} \sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} = r \left( V - S \frac{\partial V}{\partial S} \right)$$

---

## 5. Final Black-Scholes PDE

$$\frac{\partial V}{\partial t} + r S \frac{\partial V}{\partial S} + \frac{1}{2} \sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} - r V = 0$$

Boundary condition (European call):

$$V(S, T) = \max(S - K, 0)$$

---

## 6. Closed-Form Solution (for European Call)

$$C(S, t) = S \cdot N(d_1) - K e^{-r(T - t)} N(d_2)$$

where

$$d_1 = \frac{\ln(S/K) + (r + \frac{1}{2}\sigma^2)(T - t)}{\sigma \sqrt{T - t}}, \quad$$
$$d_2 = d_1 - \sigma \sqrt{T - t}$$

---

## Summary

| Concept           | Meaning                         |
|------------------|---------------------------------|
| Hedged Portfolio | Riskless using \( \Delta \)-hedging |
| Itô’s Lemma      | Required to derive \( dV \)      |
| BSM PDE          | Ensures no-arbitrage pricing     |
| Boundary         | European payoff at maturity      |

---

## Next

Martingale-based derivation in:

📘 `03b_black_scholes_martingale.md`

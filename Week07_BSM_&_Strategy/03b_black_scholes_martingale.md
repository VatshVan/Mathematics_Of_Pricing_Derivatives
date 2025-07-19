# Black-Scholes Pricing via Martingale Framework

---

## Objective

Derive the Black-Scholes option pricing formula by:
- Modeling the stock under the **risk-neutral measure** $$\( \mathbb{Q} \)$$
- Using the **expected value** of discounted future payoffs
- Solving the integral via **lognormal properties**

This approach avoids PDEs and is based on the **martingale pricing principle**.

---

## 1. Setup: Risk-Neutral Stock Dynamics

Under risk-neutral measure $$\( \mathbb{Q} \)$$, stock follows:

$$dS_t = r S_t dt + \sigma S_t dW_t^{\mathbb{Q}}$$

Solution of this SDE:

$$S_T = S_t \exp\left[ \left( r - \frac{1}{2} \sigma^2 \right)(T - t) + \sigma (W_T^\mathbb{Q} - W_t^\mathbb{Q}) \right]$$

---

## 2. Fundamental Pricing Equation

By the **martingale pricing theorem**, the fair price of a European call is:

$$C_t = e^{-r(T - t)} \mathbb{E}^{\mathbb{Q}}[ \max(S_T - K, 0) \mid \mathcal{F}_t ]$$

---

## 3. Change of Measure → Lognormal Distribution

Since $$\( \log(S_T) \)$$ is normally distributed:

$$\log(S_T) \sim \mathcal{N}\left( \log(S_t) + \left( r - \frac{1}{2} \sigma^2 \right)(T - t),\; \sigma^2 (T - t) \right)$$

Use standard normal variable:

$$Z \sim \mathcal{N}(0,1), \quad$$
$$S_T = S_t \cdot e^{(r - \frac{1}{2}\sigma^2)(T - t) + \sigma \sqrt{T - t} Z}$$

---

## 4. Computing the Expected Payoff

We evaluate:

$$C_t = e^{-r(T - t)} \mathbb{E}^\mathbb{Q} \left[ \max(S_T - K, 0) \right]$$

Break it into integrals using cumulative distribution:

$$C_t = S_t N(d_1) - K e^{-r(T - t)} N(d_2)$$

Where:

$$d_1 = \frac{\log(S_t/K) + (r + \frac{1}{2} \sigma^2)(T - t)}{\sigma \sqrt{T - t}}, \quad$$
$$d_2 = d_1 - \sigma \sqrt{T - t}$$

---

## 5. Final Black-Scholes Formula

$$C_t = S_t N(d_1) - K e^{-r(T - t)} N(d_2)$$

$$P_t = K e^{-r(T - t)} N(-d_2) - S_t N(-d_1)$$

---

## 6. Why This Works

- The **discounted payoff** is a **martingale** under \( \mathbb{Q} \)
- This ensures **no arbitrage**
- Closed-form solution avoids solving PDEs
- Easily extends to Monte Carlo simulations

---

## Summary

| Concept                     | Meaning |
|-----------------------------|---------|
| Risk-Neutral Measure $$\( \mathbb{Q} \)$$ | Changes drift to $$\( r \)$$ |
| Martingale Pricing          | Present value = expected discounted payoff |
| $$\( \log(S_T) \)$$             | Normally distributed |
| Result                      | Closed-form Black-Scholes formula |

---

## Applications

- Monte Carlo simulations
- Path-dependent option pricing
- Pricing exotic options via expectations

---

##
Combine theory with code in:

`notebooks/03_black_scholes_derivations.ipynb`

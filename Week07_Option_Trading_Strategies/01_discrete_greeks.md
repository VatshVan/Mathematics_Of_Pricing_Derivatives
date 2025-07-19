# Greeks in Discrete-Time Models (Binomial Trees)

---

## Objective

In continuous-time models (e.g., Black-Scholes), Greeks are derived via partial derivatives.

But in **discrete-time models**, like the **Binomial Tree**, we approximate Greeks using **finite differences** from the price lattice.

This allows:
- Estimating risk sensitivities (Δ, Γ, Θ)
- Understanding how an option’s price reacts to market inputs
- Comparing discrete vs continuous interpretations

---

## 1. Delta (Δ) — Sensitivity to Stock Price

$$
\Delta = \frac{V_u - V_d}{S_u - S_d}
$$

Where:
- $$\( V_u \)$$: option value at the up node
- $$\( V_d \)$$: value at the down node
- $$\( S_u, S_d \)$$: corresponding stock prices

**Interpretation**:  
Delta tells how much the option price changes with a ₹1 change in underlying price.

For a European call:
- $$\( \Delta \in (0, 1) \)$$
- High near expiry if ITM
- Near 0 if deep OTM

---

## 2. Gamma (Γ) — Sensitivity of Delta to Stock Price

$$
\Gamma = \frac{\Delta_{+} - \Delta_{-}}{(S_{+} - S_{-}) / 2}
$$

Where:
- $$\( \Delta_{+}, \Delta_{-} \)$$ = Delta at upper/lower branches
- $$\( S_{+}, S_{-} \)$$ = Underlying prices at respective levels

**Gamma peaks near ATM**  
- Tells how fast delta is changing
- High Gamma means option is sensitive to small movements

---

## 3. Theta (Θ) — Sensitivity to Time

$$
\Theta = \frac{V(t + \Delta t) - V(t)}{\Delta t}
$$

Where:
- $$\( V(t) \)$$: option value now
- $$\( V(t + \Delta t) \)$$: value 1 step forward in tree

Theta is typically **negative** for long options.

---

## 4. Key Characteristics in Binomial Models

| Greek  | Approximation Method         | Behavior           |
|--------|------------------------------|--------------------|
| Delta  | Difference across stock path | Smooth at deep ITM/OTM |
| Gamma  | Second-order finite diff     | Spikes at ATM      |
| Theta  | Time difference in price     | Decays toward expiry |

---

## 5. Implementation Steps

1. Build binomial tree of stock prices
2. Build option value tree (backward induction)
3. Use top 2–3 levels to estimate:
   - Δ from first step
   - Γ from second step
   - Θ from value decay

---

## 6. Compare to Black-Scholes Greeks

You can compare:
- Discrete Delta vs BSM Delta
- Discrete Γ, Θ vs continuous counterparts

As time steps $$\( N \to \infty \)$$, the values **converge** to Black-Scholes Greeks.

---

## Insights

- Delta hedging can be approximated in binomial models
- Gamma is hard to hedge — requires nonlinear rebalancing
- Theta helps quantify time decay losses
- Useful for American option behavior too (non-analytic)

---

## 

I've implemented these calculations in:

`notebooks/21_discrete_greeks.ipynb`


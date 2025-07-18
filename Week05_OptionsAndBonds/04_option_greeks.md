# Option Greeks: Sensitivities in Black-Scholes

---

## What Are Greeks?

Greeks measure how the **value of an option** changes in response to small changes in market parameters:

| Greek   | Measures Sensitivity to...       |
|---------|----------------------------------|
| Delta   | Stock price \( S \)              |
| Gamma   | Delta (second-order sensitivity) |
| Theta   | Time to expiry \( T \)           |
| Vega    | Volatility \( \sigma \)          |
| Rho     | Interest rate \( r \)            |

---

## ∆ Delta

$$
\Delta = \frac{\partial V}{\partial S}
$$

- For calls: \( 0 < \Delta < 1 \)
- For puts: \( -1 < \Delta < 0 \)
- Tells you how much the option price changes for a ₹1 move in the stock

---

## Γ Gamma

$$
\Gamma = \frac{\partial^2 V}{\partial S^2}
$$

- Measures how fast Delta changes
- High Gamma → unstable Delta → more rebalancing
- Peaks at-the-money (ATM) near expiry

---

## Θ Theta

$$
\Theta = \frac{\partial V}{\partial t}
$$

- Measures time decay
- For long options: usually **negative**
- Greatest near expiry & ATM

---

## ν Vega

$$
\nu = \frac{\partial V}{\partial \sigma}
$$

- Sensitivity to volatility
- High for ATM, long-dated options
- Important for **implied vol trading**

---

## ρ Rho

$$
\rho = \frac{\partial V}{\partial r}
$$

- Change in option value due to interest rates
- Calls: positive ρ  
- Puts: negative ρ

---

## Interpretation Summary

| Greek | What It Tells You                          |
|-------|---------------------------------------------|
| ∆     | Hedge ratio, directional sensitivity        |
| Γ     | Risk of Delta changing, rehedging need      |
| Θ     | Cost of time passage                        |
| ν     | Volatility exposure                         |
| ρ     | Interest rate exposure                      |

---

## Visualize each Greek across price, time, and volatility

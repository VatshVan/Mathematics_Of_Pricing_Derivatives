# Option Trading Strategies: Spreads, Straddles, Condors

---

## Objective

Design structured option strategies that:
- Express directional or neutral views
- Control risk using defined payoff ranges
- Utilize Greeks to manage exposure

---

## 1. Bull Call Spread (Moderately Bullish)

- **Buy** 1 ATM call (e.g., strike = ₹100)
- **Sell** 1 OTM call (e.g., strike = ₹110)

### Payoff:
$$\text{Max Profit} = K_2 - K_1 - \text{Net Premium}, \quad$$
$$\text{Max Loss} = \text{Net Premium}$$

- Lower cost than outright call
- Profit only if price rises past breakeven

---

## 2. Bear Put Spread (Moderately Bearish)

- **Buy** 1 ATM put (e.g., strike = ₹110)
- **Sell** 1 OTM put (e.g., strike = ₹100)

### Payoff:
$$\text{Max Profit} = K_1 - K_2 - \text{Net Premium}, \quad$$
$$\text{Max Loss} = \text{Net Premium}$$

- Good for limited downside view

---

## 3. Long Straddle (Volatility Play)

- **Buy** 1 ATM call
- **Buy** 1 ATM put (same strike)

### Payoff:

$$\text{Max Profit} \to \infty, \quad$$
$$\text{Max Loss} = \text{Total Premium}$$

- Profitable in large price moves either way
- High cost, needs significant volatility

---

## 4. Long Butterfly Spread (Neutral View)

- **Buy** 1 lower strike call (K1)
- **Sell** 2 ATM calls (K2)
- **Buy** 1 higher strike call (K3)

### Payoff:
- Max profit at K2
- Limited upside/downside risk
- Ideal for range-bound market

---

## 5. Iron Condor (Wide Range-Bound Strategy)

- Combine **bull put** and **bear call** spreads:
  - **Sell** 1 put (K1)
  - **Buy** 1 lower put (K0)
  - **Sell** 1 call (K2)
  - **Buy** 1 higher call (K3)

### Payoff:
- Max profit = Net credit (if price remains between K1 and K2)
- Limited loss if breached on either side
- Profits from **low volatility** and **time decay**

---

## 6. Greeks & Strategic Use

| Strategy        | Delta | Gamma | Theta | Vega | Use Case                         |
|----------------|-------|-------|-------|------|----------------------------------|
| Bull Call       | +     | +     | –     | +    | Moderately bullish               |
| Bear Put        | –     | +     | –     | +    | Moderately bearish               |
| Straddle        | ±     | High  | –     | High | Volatility explosion             |
| Butterfly       | 0     | +     | +     | Low  | Low-volatility + range-bound     |
| Iron Condor     | 0     | Low   | +     | Low  | Income from stable markets       |

---

## Strategy Selection Logic

- **Direction Expected?** → Choose vertical spreads  
- **Volatility Forecast?** → Straddle/strangle (high) or condor (low)  
- **Risk Aversion?** → Pick defined-risk strategies like spreads  
- **Time Decay Favorable?** → Prefer short options (Theta positive)

---

## Summary

- Option strategies offer **leverage with defined risk**
- Spread constructions can tailor **risk/reward curves**
- Strategy selection should align with **market view + volatility**
- Simulation and Greek exposure help in **strategy tuning**

---

##
Proceed to:
`notebooks/04_option_strategy_comparison.ipynb`  
To simulate payoffs, breakevens and visualize all the strategies in action.

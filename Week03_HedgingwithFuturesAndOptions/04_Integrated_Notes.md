# 📚 Week 3 Integrated Notes

**Hedging with Futures & Options – Summary and Self-Analysis**

---

## 1. Hedging with Futures

### 📂 Overview

Futures contracts provide an effective way to hedge portfolio exposure against adverse price movements by locking in future prices through standardized exchange-traded contracts.

### 📊 Key Concepts

* **Optimal Hedge Ratio:**

  $$
  h^* = \frac{\sigma_S}{\sigma_F} \rho_{SF}
  $$

* **Short Hedge:** Protects a long position from price drops.

* **Long Hedge:** Protects a short position from price rises.

* **Basis Risk:** Futures prices and spot prices may not always move perfectly together.

### 🔍 Practical Analysis

* Used **historical spot and futures data** to calculate the optimal hedge ratio.
* Simulated a **futures-based hedge** by sizing futures contracts proportional to exposure.
* Visualized **cumulative hedged P\&L** over time.

### ✅ Key Takeaways

* Hedge effectiveness depends heavily on correlation and volatility.
* Futures hedging introduces basis risk but requires no upfront premium.
* Proper hedge sizing is critical to avoid under or over-hedging.

---

## 2. Options: Basics and Hedging

### 📂 Overview

Options offer more **flexible risk management tools** compared to futures by providing asymmetric payoffs and limited downside exposure.

### 📊 Key Strategies

* **Long Call Option:** Potential for unlimited gains with limited loss (premium paid).
* **Long Put Option:** Downside protection with limited cost (premium paid).
* **Protective Put:** Long asset + long put → limits downside loss.
* **Covered Call:** Long asset + short call → generates income but caps upside.

### 🔍 Practical Analysis

* Built **scenario-based payoff tables** for call and put options.
* Visualized option payoffs using combined diagrams.
* Simulated **protective put** and **covered call** strategies to observe their impact on portfolio risk.

### ✅ Key Takeaways

* Options provide **downside protection and income generation** flexibility.
* Protective puts limit losses but involve premium costs.
* Covered calls offer limited upside in exchange for premium income.
* Options allow **customized risk profiles** not possible with futures.

---

## 3. Futures vs. Options Hedging – Self-Analysis

| Feature            | Futures Hedging         | Options Hedging                   |
| ------------------ | ----------------------- | --------------------------------- |
| Upfront Cost       | No premium              | Premium required for options      |
| Flexibility        | Fixed exposure          | Flexible payoff structures        |
| Risk               | Full downside exposure  | Limited downside (protective put) |
| Basis Risk         | Exists                  | Not applicable                    |
| Margin Requirement | Required                | Depends on position               |
| Best Use           | High correlation assets | Uncertain/volatile markets        |

---

## 📦 Self-Analysis Summary

* Gained hands-on experience with **futures and options pricing and simulations.**
* Developed ability to size hedges, simulate payoffs, and visualize risk exposures.
* Compared the **trade-offs** between cost, flexibility, and protection in futures vs. options hedging.
* Built complete Jupyter simulations for both strategies using real and hypothetical datasets.

---

## 📚 Resources

* Futures Hedging: [Hedging with Futures | CFA Level I](https://www.youtube.com/watch?v=VuAQ9X8PTyU)
* Options Basics: [Option Hedging Basics | CFA Level I](https://www.youtube.com/watch?v=zJKp44Aokgs)
* Protective Puts & Covered Calls: [CFA Level I Video](https://www.youtube.com/watch?v=GlNCLk1B7DI)
* Practical Simulations:

  * `notebooks/futures_hedging.ipynb`
  * `notebooks/options.ipynb`

---

All option pricing and payoff data was generated using manual simulations and scenario tables.

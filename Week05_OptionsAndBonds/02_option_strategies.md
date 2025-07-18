# Advanced Option Trading Strategies

---

## 1. Introduction

While single options (calls/puts) are powerful on their own, combining them in structured ways allows traders to:

- Express directional and volatility views
- Control risk and reward
- Construct **defined payoff** profiles
- Hedge exposure more efficiently

These combinations are called **option strategies** — and are core to trading, hedging and risk management in practice.

---

## 2. Key Strategy Types

We broadly classify multi-leg strategies into:

| Type               | View            | Instruments Involved         |
|--------------------|------------------|-------------------------------|
| **Spreads**        | Directional     | Buy and sell same type (call/put) |
| **Straddles**      | Volatility      | Long call + long put (same K) |
| **Strangles**      | Volatility      | Long call + long put (diff K) |
| **Butterflies**    | Neutral (Low Vol) | 3 or 4 legs with symmetry |
| **Condors**        | Neutral (Wider) | Wider version of butterflies |
| **Covered / Synthetic** | Income or protection | Involves stock positions |

---

## 3. Strategy Examples

---

### A. Bull Call Spread

- **Buy 1 call (lower strike)**  
- **Sell 1 call (higher strike)**  
- Net debit strategy

**View:** Moderately bullish  
**Payoff:**

$$\text{Max Gain} = K_2 - K_1 - \text{Net Premium}, \quad$$
$$\text{Max Loss} = \text{Net Premium}$$

---

### B. Bear Put Spread

- **Buy 1 put (higher strike)**  
- **Sell 1 put (lower strike)**  
- Net debit strategy

**View:** Moderately bearish

---

### C. Long Straddle

- **Buy 1 call and 1 put (same strike)**

**View:** High volatility expected, direction unknown  
**Breakeven:**  
$$
S = K \pm (\text{Total Premium Paid})
$$

---

### D. Long Strangle

- **Buy 1 OTM call**  
- **Buy 1 OTM put**  
- Cheaper than straddle

**View:** Same as straddle, but more cost-efficient

---

### E. Butterfly Spread (Call)

- **Buy 1 call (low strike)**  
- **Sell 2 calls (mid strike)**  
- **Buy 1 call (high strike)**  
- Net debit, limited risk and reward

**View:** Expecting no large move in asset

---

### F. Iron Condor

- **Sell OTM call + buy further OTM call**  
- **Sell OTM put + buy further OTM put**

Combines bull put and bear call spreads  
**View:** Market stays in a tight range

---

## 4. Components of a Payoff Simulator

For each leg:
- Identify **option type (call/put)**
- Track **strike price (K)**
- Track **premium paid/received**
- Add up total payoff over price grid

---

## 5. Python Payoff Calculation (High-Level)

We have use:
- `np.maximum` for option intrinsic value
- Vectorized payoff logic
- Total payoff = sum of legs
- Break-even = price(s) where total payoff = 0

---

## 6. Risks and Considerations

| Risk | Impact |
|------|--------|
| Implied Volatility | Affects option prices |
| Bid-Ask Spread | Can widen in multi-leg trades |
| Slippage | Execution mismatch |
| Early Exercise | For American options |
| Margin | Multi-leg strategies might need margin even if net debit |

---

## 7. Summary

Advanced strategies give traders:
- More **targeted exposure**
- Greater **risk control**
- Useful tools for **volatility plays**

> They form the building blocks of professional trading desks and risk-managed portfolios.

In code, these are just **payoff shapes**, but in practice, they represent powerful market views.

---

Implement `strategies.py` with payoff calculators and simulate payoff charts in `01_option_trading_strategy.ipynb`.

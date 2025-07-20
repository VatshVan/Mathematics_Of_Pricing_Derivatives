# Premium Bounds and Option Valuation

## 1. Introduction

In a no-arbitrage financial market, **option premiums** must lie within specific **theoretical bounds**. These bounds ensure that the price of an option is consistent with the absence of arbitrage opportunities.

We study here:
- Upper and lower bounds for call and put options
- Put-Call Parity relationship
- Numerical illustrations
- Common arbitrage scenarios

---

## 2. Bounds for European Options

### European Call Option

Let:
- $$\( S_0 \)$$: Current stock price
- $$\( K \)$$: Strike price
- $$\( r \)$$: Risk-free interest rate
- $$\( T \)$$: Time to maturity (in years)

#### Lower Bound:

$$C \geq \max(0, S_0 - K e^{-rT})$$

#### Upper Bound:

$$C \leq S_0$$

### European Put Option

#### Lower Bound:

$$P \geq \max(0, K e^{-rT} - S_0)$$

#### Upper Bound:

$$P \leq K e^{-rT}$$

---

## 3. Put-Call Parity

For European options with same $$\( S_0, K, T \)$$:


$$C - P = S_0 - K e^{-rT}$$

Or rearranged:

$$C = P + S_0 - K e^{-rT}$$

This means the value of a European call can be **fully replicated** using:
- A European put
- Long stock
- Short zero-coupon bond

---

## 4. Why Bounds Matter

If the price of a call or put is **outside these bounds**, an arbitrage trader can:
- Construct a **risk-free profit strategy**
- Exploit mispricing via synthetic replication
- Force the market toward equilibrium

---

## 5. Example: Numeric Illustration

Suppose:
- $$\( S_0 = 100 \)$$
- $$\( K = 100 \)$$
- $$\( r = 5\% \)$$
- $$\( T = 1 \)$$
- $$\( C = 15 \)$$
- $$\( P = 5 \)$$

We compute bounds:

- Lower bound for call: $$\( 100 - 100 e^{-0.05} \approx 4.88 \)$$
- Upper bound for call: $$\( 100 \)$$

Here, $$\( C = 15 \in [4.88, 100] \)$$

Parity check:

$$C - P = 15 - 5 = 10, \quad S_0 - K e^{-rT} \approx 4.88$$

Violation detected ⇒ potential arbitrage.

---

## 6. Arbitrage Scenarios

If call premium > upper bound:
- Sell the overpriced call
- Hedge with underlying
- Lock-in risk-free gain

If put-call parity fails:
- Long cheap side (e.g., call)
- Short expensive side (e.g., synthetic call)
- Profit without exposure

---

## 7. Python Tools for Verification

Use functions:
- `check_bounds_call(S, K, r, T, C)`
- `check_bounds_put(S, K, r, T, P)`
- `check_put_call_parity(S, K, r, T, C, P)`

All in: `src/valuation_utils.py`

---

## 8. Summary

| Option Type | Lower Bound                    | Upper Bound         |
|-------------|--------------------------------|----------------------|
| Call        | $$\( \max(0, S - K e^{-rT}) \)$$    | $$\( S \)$$              |
| Put         | $$\( \max(0, K e^{-rT} - S) \)$$    | $$\( K e^{-rT} \)$$      |

Put-Call Parity ensures **consistency** between call and put prices.  
Any deviation creates an **arbitrage opportunity**.

---

This topic forms the **valuation foundation** before exploring models like:
- Binomial Trees
- Black-Scholes
- Greeks
- Real-time trading strategies

# Topic 3: Cash Flow Streams

## 3.1 Definition

A **cash flow stream** is a series of payments made over time. It is central to pricing nearly all financial instruments.

## 3.2 Types of Cash Flows

- **Fixed**: Fixed coupons from bonds.
- **Floating**: Interest rates linked to benchmarks (e.g., LIBOR, SOFR).
- **Contingent**: Dependent on future states (e.g., option payoffs).
- **Perpetual**: Payments with infinite time horizons.

## 3.3 Present Value (PV) of Cash Flows

Given a cash flow $$\( CF_t \)$$ at time $$\( t \)$$, and discount rate $$\( r \)$$:

$$
PV = \sum_{t=1}^{T} \frac{CF_t}{(1 + r)^t}
$$

For continuous compounding:

$$
PV = \sum_{t=1}^{T} CF_t \cdot e^{-rt}
$$

## 3.4 Financial Significance

- All asset pricing models discount future cash flows to their present value.
- Option pricing models compute **expected discounted payoffs**.
- Bond valuation is essentially the present value of a known cash flow stream.

> **Insight**: Cash flow modeling connects static instruments like bonds to path-dependent instruments like options via time-value principles.

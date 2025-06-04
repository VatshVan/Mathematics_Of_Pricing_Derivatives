# Topic 4: Bond Mathematics

## 4.1 Bond Pricing

A bond is valued as the present value of future coupon payments and the final principal repayment. 

Given:
- Face Value = ₹1000  
- Annual Coupon = ₹80  
- Maturity = 3 years  
- Yield to Maturity (YTM) = 6%

### Formula:
$$
\text{Price} = \frac{80}{1.06} + \frac{80}{(1.06)^2} + \frac{1080}{(1.06)^3} = ₹1054.30
$$

## 4.2 Duration Concepts

### Macaulay Duration:
Weighted average time until cash flows are received:
<img 
  src="https://latex.codecogs.com/png.image?\dpi{150} \bg_white D_{mac}=\frac{\sum_{t=1}^{n}t\cdot\frac{CF_t}{(1+y)^t}}{Price}" 
  alt="Macaulay Duration Formula" 
  style="max-width: 100%; height: auto;" 
/>


### Modified Duration:
Measures price sensitivity to yield changes:

D_mod = D_Mac/(1 + y)

> If Modified Duration = 2.59, then a 1% increase in YTM causes a ~2.59% drop in price.

## 4.3 Practical Use

- Portfolio immunization
- Interest rate risk management
- Building duration-matched portfolios

> **Insight**: Duration is the foundation for convexity, interest rate derivatives, and dynamic hedging.

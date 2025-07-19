# Continuous-Time Models: SDEs, GBM, and Itô Calculus

---

## Objective

Model asset prices continuously using stochastic calculus.  
Build up to Black-Scholes through:

- Stochastic Differential Equations (SDEs)
- Geometric Brownian Motion (GBM)
- Itô’s Lemma: stochastic chain rule
- Lognormal returns

---

## 1. Geometric Brownian Motion (GBM)

GBM is the most common model for asset prices:

$$dS_t = \mu S_t dt + \sigma S_t dW_t$$

Where:
- $$\( S_t \)$$: asset price
- $$\( \mu \)$$: drift (expected return)
- $$\( \sigma \)$$: volatility
- $$\( W_t \)$$: standard Brownian motion (Wiener process)

Non-negative prices  
Lognormal distribution  
Continuous paths

---

## 2. Solving the SDE

Use Itô calculus to solve:

$$S_t = S_0 \exp\left[\left(\mu - \frac{1}{2}\sigma^2\right)t + \sigma W_t \right]$$

→ $$\( \log(S_t) \sim \mathcal{N} \left( \log(S_0) + (\mu - \frac{1}{2}\sigma^2)t,\; \sigma^2 t \right) \)$$

Hence:
- Returns are **lognormally** distributed
- $$\( \mathbb{E}[S_T] = S_0 e^{\mu T} \)$$
- Under $$\( \mathbb{Q} \), \( \mu \to r \)$$

---

## 3. Itô’s Lemma

The **chain rule** of stochastic calculus.

If $$\( f(S_t, t) \)$$ is a twice differentiable function, then:

$$df = \left( \frac{\partial f}{\partial t} + \mu S \frac{\partial f}{\partial S} + \frac{1}{2} \sigma^2 S^2 \frac{\partial^2 f}{\partial S^2} \right) dt + \sigma S \frac{\partial f}{\partial S} dW_t$$

Essential for:
- Deriving Black-Scholes PDE
- Computing option Greeks
- Risk modeling

---

## 4. Why Use GBM?

| Reason | Explanation |
|--------|-------------|
| Positivity | $$\( S_t > 0 \)$$ always |
| Lognormal returns | Matches empirical returns |
| Tractability | Closed-form BSM formula possible |
| Risk-neutral drift | Replace $$\( \mu \to r \)$$ easily |

---

## 5. Practical Simulation (Discretized GBM)

Simulate in code using:

$$S_{t+\Delta t} = S_t \cdot \exp\left[ \left(\mu - \frac{1}{2} \sigma^2\right) \Delta t + \sigma \sqrt{\Delta t} \cdot Z \right]$$

Where $$\( Z \sim \mathcal{N}(0, 1) \)$$

Used for:
- Monte Carlo option pricing
- Portfolio simulations
- Stress testing

---

## 6. Key Concepts

| Term              | Meaning |
|-------------------|---------|
| Brownian Motion   | Continuous random walk |
| SDE               | Differential with random term |
| Itô Process       | Includes \( dW_t \) term |
| GBM               | Exponential of Brownian motion |
| Itô’s Lemma       | Tool to handle stochastic chain rule |

---

## Summary

- GBM is standard model for asset prices in continuous time
- Itô’s Lemma is essential to derive BSM and Greeks
- All continuous-time pricing builds on this foundation

---

##
Code simulation of GBM paths and visualize key properties in:

`notebooks/23_continuous_time_models.ipynb`

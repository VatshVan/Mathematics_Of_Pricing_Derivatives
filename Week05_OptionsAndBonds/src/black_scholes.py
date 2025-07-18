import numpy as np
from scipy.stats import norm

def black_scholes_price(S, K, T, r, sigma, option_type="call"):
    '''
    Calculate the Black-Scholes price of a European option.
    S: Current stock price
    K: Strike price
    T: Time to expiry in years
    r: Risk-free interest rate (annualized)
    sigma: Volatility of the underlying stock (annualized)
    option_type: 'call' for call option, 'put' for put option
    Returns the option price.
    '''
    if T <= 0 or sigma <= 0 or S <= 0:
        return 0.0

    d1 = (np.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)

    if option_type == "call":
        price = S * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)
    elif option_type == "put":
        price = K * np.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)
    else:
        raise ValueError("option_type must be 'call' or 'put'")
    
    return price

def black_scholes_delta(S, K, T, r, sigma, option_type="call"):
    '''
    Calculate the delta of a European option using the Black-Scholes model.
    S: Current stock price
    K: Strike price
    T: Time to expiry in years
    r: Risk-free interest rate (annualized)
    sigma: Volatility of the underlying stock (annualized)
    option_type: 'call' for call option, 'put' for put option
    Returns the delta of the option.
    '''
    if T <= 0 or sigma <= 0 or S <= 0:
        return 0.0

    d1 = (np.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))

    if option_type == "call":
        return norm.cdf(d1)
    elif option_type == "put":
        return norm.cdf(d1) - 1

def black_scholes_greeks(S, K, T, r, sigma, option_type="call"):
    '''
    Calculate the Greeks of a European option using the Black-Scholes model.
    S: Current stock price
    K: Strike price
    T: Time to expiry in years
    r: Risk-free interest rate (annualized)
    sigma: Volatility of the underlying stock (annualized)
    option_type: 'call' for call option, 'put' for put option
    Returns a dictionary with delta, gamma, vega, theta, and rho.
    '''
    if T <= 0 or sigma <= 0 or S <= 0:
        return dict(delta=0, gamma=0, vega=0, theta=0, rho=0)

    d1 = (np.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)

    delta = black_scholes_delta(S, K, T, r, sigma, option_type)
    gamma = norm.pdf(d1) / (S * sigma * np.sqrt(T))
    vega = S * norm.pdf(d1) * np.sqrt(T)

    if option_type == "call":
        theta = (-S * norm.pdf(d1) * sigma / (2 * np.sqrt(T))) - r * K * np.exp(-r * T) * norm.cdf(d2)
        rho = K * T * np.exp(-r * T) * norm.cdf(d2)
    else:
        theta = (-S * norm.pdf(d1) * sigma / (2 * np.sqrt(T))) + r * K * np.exp(-r * T) * norm.cdf(-d2)
        rho = -K * T * np.exp(-r * T) * norm.cdf(-d2)

    return {
        "delta": delta,
        "gamma": gamma,
        "vega": vega / 100,
        "theta": theta / 365,
        "rho": rho / 100
    }

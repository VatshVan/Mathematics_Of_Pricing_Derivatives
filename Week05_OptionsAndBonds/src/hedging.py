import numpy as np
from black_scholes import black_scholes_price, black_scholes_delta

def simulate_delta_hedge(
    S_path,
    K,
    T,
    r,
    sigma,
    option_type="call",
    rebalance_times=50
):
    '''
    S_path: Simulated path of stock prices (array)
    T: Total time in years (e.g., 1.0)
    rebalance_times: Number of hedge adjustments (discrete steps)
    '''
    n = len(S_path)
    dt = T / (rebalance_times - 1)
    time_grid = np.linspace(0, T, rebalance_times)

    cash = 0.0
    portfolio_value = []
    deltas = []

    for i in range(rebalance_times):
        S = S_path[i]
        t = time_grid[i]
        tau = T - t

        delta = black_scholes_delta(S, K, tau, r, sigma, option_type)
        deltas.append(delta)

        if i == 0:
            # On the first step, buy the option and set initial cash
            option_price = black_scholes_price(S, K, tau, r, sigma, option_type)
            cash = option_price - delta * S
        else:
            # Adjust the portfolio based on delta
            d_delta = delta - deltas[i - 1]
            cash -= d_delta * S

        # Update portfolio value
        cash *= np.exp(r * dt)
        portfolio_value.append(delta * S + cash)

    # Final portfolio value and option payoff
    if option_type == "call":
        option_payoff = max(S_path[-1] - K, 0)
    else:
        option_payoff = max(K - S_path[-1], 0)

    hedge_error = portfolio_value[-1] - option_payoff

    return {
        "portfolio_values": np.array(portfolio_value),
        "deltas": np.array(deltas),
        "cash": cash,
        "hedge_error": hedge_error,
        "option_payoff": option_payoff,
        "stock_final": S_path[-1],
    }

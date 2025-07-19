import numpy as np
import matplotlib.pyplot as plt

def call_payoff(S, K, premium=0):
    return np.maximum(S - K, 0) - premium

def put_payoff(S, K, premium=0):
    return np.maximum(K - S, 0) - premium

def bull_call_spread(S, K1, K2, premium1, premium2):
    return call_payoff(S, K1, premium1) - call_payoff(S, K2, premium2)

def bear_put_spread(S, K1, K2, premium1, premium2):
    return put_payoff(S, K2, premium1) - put_payoff(S, K1, premium2)

def long_straddle(S, K, call_premium, put_premium):
    return call_payoff(S, K, call_premium) + put_payoff(S, K, put_premium)

def long_butterfly(S, K1, K2, K3, premium1, premium2, premium3):
    return (call_payoff(S, K1, premium1)
            - 2 * call_payoff(S, K2, premium2)
            + call_payoff(S, K3, premium3))

def iron_condor(S, K0, K1, K2, K3, premium0, premium1, premium2, premium3):
    return (put_payoff(S, K1, premium1) - put_payoff(S, K0, premium0)
            - call_payoff(S, K2, premium2) + call_payoff(S, K3, premium3))

def breakeven_points(strategy, S_range, *args, tol=1e-2):
    payoffs = strategy(S_range, *args)
    zero_crossings = np.where(np.abs(payoffs) < tol)[0]
    return S_range[zero_crossings]

def plot_payoff(S_range, payoff, label, color='blue', scenarios=None):
    """
    Plot payoff diagram with optional scenario lines
    """
    plt.figure(figsize=(9, 4.5))
    plt.plot(S_range, payoff, label=label, color=color, linewidth=2)
    plt.axhline(0, color='black', linestyle='--', alpha=0.6)

    if scenarios:
        for s_price in scenarios:
            plt.axvline(s_price, linestyle='--', color='gray', alpha=0.6)
            plt.text(s_price, np.min(payoff), f'₹{s_price:.0f}', fontsize=8, ha='center', va='bottom')

    plt.title(f"{label} Payoff at Expiry")
    plt.xlabel("Stock Price at Expiry")
    plt.ylabel("Profit / Loss")
    plt.grid(True, linestyle=':')
    plt.legend()
    plt.tight_layout()
    plt.xticks(np.arange(np.min(S_range), np.max(S_range) + 1, 5))
    plt.yticks(np.arange(np.min(payoff), np.max(payoff) + 1, 5))
    plt.xlim(np.min(S_range)-np.mean(S_range)/100, np.max(S_range)+np.mean(S_range)/100)
    plt.ylim(np.min(payoff)-np.mean(payoff)/10, np.max(payoff)+np.mean(payoff)/10)
    plt.savefig(f"{label.replace(' ', '_').lower()}_payoff.png", dpi=300)
    plt.show()

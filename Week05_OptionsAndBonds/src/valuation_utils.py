import numpy as np
import matplotlib.pyplot as plt

def call_bounds(S, K, r, T):
    lower = max(0, S - K * np.exp(-r * T))
    upper = S
    return lower, upper

def put_bounds(S, K, r, T):
    lower = max(0, K * np.exp(-r * T) - S)
    upper = K * np.exp(-r * T)
    return lower, upper

def check_call_bounds(S, K, r, T, C):
    lower, upper = call_bounds(S, K, r, T)
    return lower <= C <= upper, (lower, upper)

def check_put_bounds(S, K, r, T, P):
    lower, upper = put_bounds(S, K, r, T)
    return lower <= P <= upper, (lower, upper)

def check_put_call_parity(S, K, r, T, C, P, tol=1e-2):
    lhs = C - P
    rhs = S - K * np.exp(-r * T)
    return abs(lhs - rhs) <= tol, (lhs, rhs)

def plot_option_bounds(S_vals, K, r, T, option_type="call"):
    lower_bounds = []
    upper_bounds = []

    for S in S_vals:
        if option_type == "call":
            l, u = call_bounds(S, K, r, T)
        else:
            l, u = put_bounds(S, K, r, T)
        lower_bounds.append(l)
        upper_bounds.append(u)

    plt.figure(figsize=(8, 4))
    plt.plot(S_vals, lower_bounds, label="Lower Bound")
    plt.plot(S_vals, upper_bounds, label="Upper Bound")
    plt.fill_between(S_vals, lower_bounds, upper_bounds, color="skyblue", alpha=0.2)
    plt.title(f"{option_type.capitalize()} Option Bounds")
    plt.xlabel("Stock Price (S)")
    plt.ylabel("Option Premium")
    plt.legend()
    plt.grid(True)
    plt.savefig(f"{option_type}_bounds.png")
    plt.show()
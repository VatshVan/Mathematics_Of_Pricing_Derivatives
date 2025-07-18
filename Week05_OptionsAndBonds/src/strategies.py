import numpy as np
import matplotlib.pyplot as plt

def call_payoff(S, K, premium, position='long'):
    '''
    Calculate the payoff for a call option.
    S: Stock price at expiry
    K: Strike price
    premium: Premium paid for the option
    position: 'long' for buying the option, 'short' for selling the option
    Assumes European options.
    '''
    payoff = np.maximum(S - K, 0) - premium
    return payoff if position == 'long' else -payoff

def put_payoff(S, K, premium, position='long'):
    '''
    Calculate the payoff for a put option.
    S: Stock price at expiry
    K: Strike price
    premium: Premium paid for the option
    position: 'long' for buying the option, 'short' for selling the option
    Assumes European options.
    '''
    payoff = np.maximum(K - S, 0) - premium
    return payoff if position == 'long' else -payoff

def plot_strategy(S, payoffs, labels, title="Option Strategy Payoff"):
    '''
    Plot the payoffs of an option strategy.
    S: Array of stock prices at expiry
    payoffs: List of payoffs for each leg of the strategy
    labels: Labels for each leg of the strategy
    title: Title of the plot
    '''
    total_payoff = np.sum(payoffs, axis=0)

    plt.figure(figsize=(10, 6))
    for payoff, label in zip(payoffs, labels):
        plt.plot(S, payoff, '--', label=f"{label} Leg")

    plt.plot(S, total_payoff, label="Net Payoff", linewidth=2, color='black')
    plt.axhline(0, color='gray', linewidth=0.5, linestyle='--')
    plt.title(title)
    plt.xlabel("Stock Price at Expiry")
    plt.ylabel("Profit / Loss")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(title.replace(" ", "_").lower() + ".png")
    plt.show()

# Options: Basics and Payoffs

## Option Contract Overview

- **Call Option**: Right to **buy** at strike price.
- **Put Option**: Right to **sell** at strike price.
- **Long** = Buyer of the contract
- **Short** = Seller (writer) of the contract

## European vs American Options

- **European**: Exercisable **only at expiry**
- **American**: Exercisable **any time until expiry**

## Moneyness

| Type   | Call               | Put                |
|--------|--------------------|--------------------|
| ITM    | \( S > K \)        | \( S < K \)        |
| ATM    | \( S = K \)        | \( S = K \)        |
| OTM    | \( S < K \)        | \( S > K \)        |

## Payoff Diagrams

- **Long Call**: \[ \max(S_T - K, 0) \]
- **Long Put**: \[ \max(K - S_T, 0) \]
- **Short Call**: \[ -\max(S_T - K, 0) \]
- **Short Put**: \[ -\max(K - S_T, 0) \]

## Profit = Payoff − Premium


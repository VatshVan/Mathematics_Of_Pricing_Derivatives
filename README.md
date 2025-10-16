# Mathematics of Derivative Pricing

[![License: GPL v2](https://img.shields.io/badge/License-GPL%20v2-blue.svg)](LICENSE)

A comprehensive implementation and exploration of the mathematical models and strategies that underpin modern financial derivative pricing. This project was developed as the final report for the Summer of Science Program at IIT Bombay.

This repository provides a rigorous journey from the foundational concepts of financial markets to the derivation and application of the Black-Scholes model. It combines theoretical derivations, financial intuition, and practical Python implementations to bridge the gap between theory and real-world application.

***

## 📚 Table of Contents
* [Key Topics & Concepts](#-key-topics--concepts)
* [Technical Stack](#-technical-stack)
* [Repository Structure](#-repository-structure)
* [Getting Started](#-getting-started)
* [Usage](#-usage)
* [Weekly Reports](#-weekly-reports)
* [License](#-license)
* [Acknowledgments](#-acknowledgments)
* [Contact](#-contact)

***

## 🔑 Key Topics & Concepts

This project provides a deep dive into the following areas of quantitative finance:

* [cite_start]**Financial Fundamentals**: Exploration of financial markets, interest rates, cash flow discounting, and bond mathematics [cite: 17-20].
* [cite_start]**Modern Portfolio Theory (MPT)**: Implementation of portfolio optimization to find the Efficient Frontier, maximize Sharpe Ratio, and construct minimum volatility portfolios [cite: 240-250, 290-292].
* [cite_start]**Forwards & Futures**: No-arbitrage pricing using cost-of-carry models, analysis of basis convergence, and simulation of Mark-to-Market (MTM) settlement [cite: 22, 635-641].
* [cite_start]**Hedging Strategies**: Calculation of the optimal hedge ratio and simulation of risk reduction using futures contracts and options (Protective Puts, Covered Calls)[cite: 802, 915, 941, 949].
* **Option Pricing Theory**:
    * [cite_start]**Premium Bounds & Put-Call Parity**: Establishing the theoretical price boundaries for options to prevent arbitrage[cite: 1087, 1091].
    * [cite_start]**The Option Greeks ($ \Delta, \Gamma, \Theta, \nu, \rho $)**: Calculating and visualizing key option sensitivities using the Black-Scholes model[cite: 1395].
    * [cite_start]**Dynamic Hedging**: Simulating a delta-neutral hedging strategy to replicate an option's payoff and analyzing hedging error [cite: 1219-1221].
* **Numerical Pricing Models**:
    * [cite_start]**Binomial Option Pricing**: Implementing the Cox-Ross-Rubinstein (CRR) model for both European and American options, and demonstrating its convergence to the Black-Scholes price [cite: 1568-1570, 1601].
    * [cite_start]**Continuous-Time Models**: Simulating asset price paths using Geometric Brownian Motion (GBM)[cite: 1955].
* **The Black-Scholes Model**:
    * [cite_start]**Derivation**: Step-by-step derivation of the Black-Scholes PDE via both the delta-hedging (no-arbitrage) argument and the Martingale pricing approach[cite: 2293, 2342].
    * [cite_start]**Implementation**: Pricing options using the closed-form formula, Monte Carlo simulations, and Finite Difference methods[cite: 3127, 3130].
* **Advanced Option Trading Strategies**:
    * [cite_start]Implementing and visualizing payoff diagrams for various strategies including **Vertical Spreads** (Bull Call, Bear Put), **Volatility Strategies** (Straddle, Strangle), and **Neutral Strategies** (Butterfly, Iron Condor) [cite: 2615-2619, 3136-3138].

***

## 🛠️ Technical Stack
* **Language**: Python 3.x
* **Libraries**:
    * **Numerical Analysis**: NumPy, SciPy
    * **Data Handling**: Pandas
    * **Symbolic Mathematics**: SymPy
    * **Visualization**: Matplotlib
* **Environment**: Jupyter Notebooks

***

## 📂 Repository Structure

The project is organized into weekly modules, each containing its own set of notebooks, scripts and reports.

```
.
├── 📂 Week01_FinancialFundamentals/
│   ├── 📂 scripts/
│   └── 📜 README.md
│
├── 📂 Week02_PortfolioForwardsFutures/
│   ├── 📂 notebooks/
│   ├── 📂 scripts/
│   └── 📜 README.md
│
├── 📂 Week03_HedgingwithFuturesAndOptions/
│   ├── 📂 notebooks/
│   ├── 📂 scripts/
│   └── 📜 README.md
│
├── 📂 Week05_OptionsAndBonds/
│   ├── 📂 notebooks/
│   ├── 📂 src/
│   └── 📜 README.md
│
├── 📂 Week06_Discretre_Time_Models/
│   ├── 📂 notebooks/
│   ├── 📂 scripts/
│   └── 📜 README.md
│
├── 📂 Week07_BSM_&_Strategy/
│   └── 📜 README.md
│
├── 📜 Week04_Midterm_Report_Derivative_Pricing.pdf
├── 📜 Final_Rport_Derivative_Pricing.pdf
├── 📜 LICENSE
├── 📜 README.md
└── 📜 requirements.txt
```

***

## 🚀 Getting Started

Follow these steps to set up the project locally.

### Prerequisites

* Python 3.8 or higher
* pip (Python package installer)

### Installation

1.  **Clone the repository:**
    ```sh
    git clone [https://github.com/your-username/mathematics-of-derivative-pricing.git](https://github.com/your-username/mathematics-of-derivative-pricing.git)
    cd mathematics-of-derivative-pricing
    ```
2.  **Install the required packages:**
    ```sh
    pip install -r requirements.txt
    ```

***

## 💻 Usage

The analysis and implementations are contained within Jupyter notebooks located in their respective weekly folders.

1.  **Launch Jupyter Lab:**
    ```sh
    jupyter lab
    ```
2.  **Navigate the notebooks:** Open the weekly folders (e.g., `Week02_PortfolioForwardsFutures/notebooks/`) to find and run the relevant notebooks. The markdown files in the `scripts/` or `src/` directories provide theoretical notes corresponding to the implementations.

***

## 📝 Weekly Reports

Each weekly folder contains a `README.md` file that serves as a progress report for that period, detailing the topics covered and milestones achieved.

* [**Week 01:** Financial Fundamentals](./Week01_FinancialFundamentals/README.md)
* [**Week 02:** Portfolio, Forwards & Futures](./Week02_PortfolioForwardsFutures/README.md)
* [**Week 03:** Hedging with Futures and Options](./Week03_HedgingwithFuturesAndOptions/README.md)
* [**Week 05:** Options and Bonds](./Week05_OptionsAndBonds/README.md)
* [**Week 06:** Discrete-Time Models](./Week06_Discretre_Time_Models/README.md)
* [**Week 07:** Black-Scholes Model & Trading Strategies](./Week07_BSM_&_Strategy/README.md)

***

## 📜 License

This project is licensed under the **GNU 2.0 License**. See the [LICENSE](LICENSE) file for more details.

***

## 🙏 Acknowledgments

This project would not have been possible without the guidance and support of:
* My mentors, **Ishan Jain** and **Kalp Rawat**, for their invaluable feedback and direction.
* The **Summer of Science Program** organized by the **MnP Club, IIT Bombay**, for providing this incredible learning opportunity.

***

## 📬 Contact

Vatsh Van

* **GitHub**: `https://github.com/VatshVan`
* **Email**: `vatshvan.iitb@gmail.com`
* **LinkedIn**: `https://linkedin.com/in/your-profile`

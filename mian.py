"""
Monte Carlo Option Pricing (European Call) with:
✅ Geometric Brownian Motion (GBM)
✅ Black–Scholes benchmark comparison
✅ Standard error & 95% confidence interval
✅ Price path & terminal distribution visualization

Author: M. Rama Krishna Reddy
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm


def black_scholes_call(S0, K, r, sigma, T):
    """
    Closed-form Black–Scholes price for a European call option.
    """
    d1 = (np.log(S0 / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)

    return S0 * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)


def mc_price_option(S0, K, r, sigma, T, M, I, seed=42):
    """
    Monte Carlo pricing of a European call option under GBM.
    """
    np.random.seed(seed)
    dt = T / M
    S = np.zeros((M + 1, I))
    S[0] = S0

    for t in range(1, M + 1):
        eps = np.random.standard_normal(I)
        S[t] = S[t - 1] * np.exp((r - 0.5 * sigma**2) * dt + sigma * eps * np.sqrt(dt))

    # Payoff
    payoff = np.maximum(S[-1] - K, 0.0)

    # Discounted price
    price_mc = np.exp(-r * T) * np.mean(payoff)

    # Standard error
    std_error = np.exp(-r * T) * np.std(payoff, ddof=1) / np.sqrt(I)

    # Confidence interval (95%)
    ci_low = price_mc - 1.96 * std_error
    ci_high = price_mc + 1.96 * std_error

    return price_mc, std_error, (ci_low, ci_high), S


def plot_results(S, K, S0):
    final_prices = S[-1]

    fig = plt.figure(figsize=(14, 6))
    ax_paths = plt.gca()

    ax_paths.plot(S[:, ::200], linewidth=0.8)
    ax_paths.set_title("Monte Carlo Simulation of GBM Price Paths")
    ax_paths.set_xlabel("Time Steps")
    ax_paths.set_ylabel("Price")
    ax_paths.axhline(K, color='r', linestyle='--', label='Strike Price')
    ax_paths.scatter(0, S0, c='black', marker='x', label='Initial Price')
    ax_paths.grid(True)
    ax_paths.legend()

    plt.tight_layout()
    plt.savefig("mc_gbm_paths.png", dpi=300)
    plt.show()

    # Histogram of terminal prices
    plt.figure(figsize=(7, 5))
    plt.hist(final_prices, bins=60, density=True, alpha=0.6)
    plt.axvline(K, color='r', linestyle='--', label='Strike Price')
    plt.title("Distribution of Terminal Stock Prices (S_T)")
    plt.xlabel("Price")
    plt.ylabel("Density")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.savefig("mc_terminal_dist.png", dpi=300)
    plt.show()


def main():
    # Parameters
    S0 = 100.0     # Initial stock price
    K = 105.0      # Strike price
    r = 0.05       # Risk-free rate
    sigma = 0.20   # Volatility
    T = 1.0        # Time to maturity (1 year)
    M = 1000       # Time steps
    I = 50_000     # Number of paths

    price_mc, std_error, ci, S = mc_price_option(S0, K, r, sigma, T, M, I)

    price_bs = black_scholes_call(S0, K, r, sigma, T)
    pct_diff = abs(price_mc - price_bs) / price_bs * 100

    print("\n===== European Call Option Pricing =====")
    print(f"Monte Carlo Price:       {price_mc:.4f}")
    print(f"Black–Scholes Price:     {price_bs:.4f}")
    print(f"Percent Deviation:       {pct_diff:.2f}%")
    print(f"Standard Error:          {std_error:.6f}")
    print(f"95% Confidence Interval: [{ci[0]:.4f}, {ci[1]:.4f}]")
    print("=======================================\n")

    plot_results(S, K, S0)


if __name__ == "__main__":
    main()

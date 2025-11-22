# 📈 Monte Carlo European Call Option Pricing (Python)

This project prices a **European Call Option** using a **Monte Carlo simulation** based on **Geometric Brownian Motion (GBM)** and validates the result against the **Black–Scholes closed-form formula**.

It includes:
✅ Price path visualization  
✅ Terminal price distribution  
✅ Standard error & 95% confidence interval  
✅ Percent deviation from Black–Scholes  

---

## ✅ 1. What This Project Does

- Simulates **50,000** possible future stock price paths
- Models stock dynamics using **stochastic GBM**
- Computes European call payoff at maturity
- Discounts expected payoff to estimate fair value
- Compares the result with **Black–Scholes theoretical price**
- Visualizes price paths and terminal price distribution

---

## ✅ 2. Inputs (Model Parameters)

| Parameter | Meaning | Example |
|----------|---------|---------|
| `S0`     | Initial stock price | 100.0 |
| `K`      | Strike price | 105.0 |
| `r`      | Risk-free interest rate (annual) | 0.05 |
| `sigma`  | Volatility (annual) | 0.20 |
| `T`      | Time to maturity (years) | 1.0 |
| `M`      | Number of time steps | 1000 |
| `I`      | Number of simulated paths | 50,000 |

These parameters can be modified to simulate different market scenarios.

---

## ✅ 3. Mathematical Model

### 📌 3.1 Geometric Brownian Motion (GBM)

Stock prices are modeled as:

$$
S_t = S_{t-1} \cdot \exp\left( (r - 0.5\sigma^2)\Delta t + \sigma \sqrt{\Delta t}\, Z_t \right)
$$

**Where:**
- \( r \) = risk-free rate  
- \( \sigma \) = volatility  
- \( \Delta t = \frac{T}{M} \) (time step)  
- \( Z_t \sim N(0, 1) \) (standard normal noise)

GBM introduces randomness, making each price path unique.

---

### 📌 3.2 European Call Payoff

At maturity \( T \):

$$
\text{Payoff} = \max(S_T - K, 0)
$$

If the stock finishes below the strike price, payoff = 0.

---

### 📌 3.3 Monte Carlo Price

The Monte Carlo estimated option price is:

$$
C_{MC} = e^{-rT} \cdot \mathbb{E}[\max(S_T - K, 0)]
$$

Meaning:
1. Simulate terminal price \( S_T \)
2. Compute payoff \( \max(S_T - K, 0) \)
3. Average across all paths
4. Discount to present value

---

### 📌 3.4 Standard Error & Confidence Interval

Standard error:

$$
SE = e^{-rT} \cdot \frac{\sigma_{\text{payoff}}}{\sqrt{I}}
$$

95% Confidence Interval:

$$
CI = C_{MC} \pm 1.96 \cdot SE
$$

This measures how statistically reliable the result is.

---

### 📌 3.5 Black–Scholes Benchmark

Closed-form price for a European call:

$$
C = S_0\,N(d_1) - K\,e^{-rT}\,N(d_2)
$$

Where:

$$
d_1 = \frac{\ln(S_0/K) + (r + 0.5\sigma^2)T}{\sigma\sqrt{T}}
$$

$$
d_2 = d_1 - \sigma\sqrt{T}
$$

\( N(x) \) is the cumulative normal distribution.

This gives the **theoretical fair price** for validation.

---

## ✅ 4. Outputs

When the script is executed, it prints:

===== European Call Option Pricing =====
- Monte Carlo Price: 7.9677
- Black–Scholes Price: 8.0214
- Percent Deviation: 0.67%
- Standard Error: 0.058843
- 95% Confidence Interval: [7.8523, 8.0830]

### ✅ Interpretation

- **0.67% deviation** → Monte Carlo estimate is highly accurate.
- The Black–Scholes price lies **within the confidence interval**, confirming statistical validity.

---

## ✅ 5. Visualizations

### 📌 GBM Price Paths
Shows how the stock may evolve over time — uncertainty increases as time progresses.

### 📌 Terminal Price Distribution

Histogram of \( S_T \):
- Right-skewed (typical for GBM)
- Strike price marked
- Only prices above strike contribute to payoff

Both plots help understand option behavior intuitively.

---

## ✅ 6. How to Run

### Install dependencies

pip install numpy matplotlib scipy

### Run the script

python monte_carlo_option_pricing.py


Generated images:
- `mc_gbm_paths.png`
- `mc_terminal_dist.png`

---

## ✅ 7. Key Takeaways

- Monte Carlo pricing is accurate and validated
- GBM realistically models stock movements
- Confidence intervals quantify uncertainty
- Visuals improve intuition
- Can be extended to:
  - Put options
  - Greeks (Delta, Gamma, Vega)
  - Multi-asset simulations
  - Variance reduction techniques

---

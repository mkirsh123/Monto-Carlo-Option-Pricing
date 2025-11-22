# 📈 Monte Carlo European Call Option Pricing (Python)

This project prices a **European Call Option** using a **Monte Carlo simulation** based on **Geometric Brownian Motion (GBM)** and validates the result against the **Black–Scholes closed-form formula**.

It also provides:
✅ Price path visualization  
✅ Terminal price distribution  
✅ Standard error & 95% confidence interval  
✅ Percent deviation from Black–Scholes  

---

## ✅ 1. What This Project Does

- Simulates **50,000** possible future stock price paths
- Models stock dynamics using **stochastic GBM**
- Computes European call payoff at maturity
- Discounts expected payoff to estimate fair price
- Compares result with **Black–Scholes theoretical price**
- Visualizes both price paths and terminal price distribution

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

These values can be modified to simulate different market conditions.

---

## ✅ 3. Mathematical Model

### 📌 3.1 Geometric Brownian Motion (GBM)

Stock prices are modeled as:

\[
S_t = S_{t-1} \cdot \exp\left((r - 0.5\sigma^2)\Delta t + \sigma \sqrt{\Delta t} Z_t \right)
\]

Where:

- \( r \) = risk-free rate  
- \( \sigma \) = volatility  
- \( \Delta t = \frac{T}{M} \)  
- \( Z_t \sim N(0,1) \) (standard normal noise)

GBM introduces randomness, making each price path unique.

---

### 📌 3.2 European Call Payoff

At maturity \( T \):

\[
\text{Payoff} = \max(S_T - K, 0)
\]

If the stock finishes below the strike price, payoff = 0.

---

### 📌 3.3 Monte Carlo Price

\[
C_{MC} = e^{-rT} \cdot \mathbb{E}[\max(S_T - K, 0)]
\]

Meaning:
1. Compute payoff for each simulated path  
2. Take the average  
3. Discount to present value  

---

### 📌 3.4 Standard Error & Confidence Interval

Standard error:

\[
SE = e^{-rT} \cdot \frac{\sigma_{\text{payoff}}}{\sqrt{I}}
\]

95% Confidence Interval:

\[
CI = C_{MC} \pm 1.96 \cdot SE
\]

This measures the statistical reliability of the estimate.

---

### 📌 3.5 Black–Scholes Benchmark

Closed-form price for a European call:

\[
C = S_0 N(d_1) - K e^{-rT} N(d_2)
\]

Where:

\[
d_1 = \frac{\ln(S_0/K) + (r + 0.5\sigma^2)T}{\sigma \sqrt{T}}
\]

\[
d_2 = d_1 - \sigma\sqrt{T}
\]

\( N(x) \) = cumulative normal distribution.

This gives the theoretical fair price.

---

## ✅ 4. Outputs

When the script is run, it prints:


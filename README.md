# FinSight Portfolio Optimization Engine

## Risk-Based Portfolio Optimization Using Modern Portfolio Theory

FinSight is a portfolio optimization engine designed to generate investment allocations based on an investor's risk profile and available capital.

The system uses **Modern Portfolio Theory (MPT)** to analyze historical stock data, generate possible portfolios, and select portfolios based on their **risk-adjusted return using the Sharpe Ratio**.

## Project Objective

The objective is to develop a system that can:

- Accept an investor's risk profile and investment capital
- Analyze historical stock price data
- Calculate expected return and portfolio risk
- Optimize portfolio allocation
- Calculate the Sharpe Ratio
- Generate portfolios for Conservative, Moderate, and Aggressive investors
- Display the results through an interactive Streamlit dashboard

## Risk Profiles

The system generates portfolios for three investor profiles:

| Profile | Equity Range |
|---|---:|
| Conservative | 10% – 40% |
| Moderate | 40% – 70% |
| Aggressive | 65% – 95% |

## Assets Used

The portfolio analysis uses historical data for:

- RELIANCE
- TCS
- HDFCBANK
- INFY
- ICICIBANK
- WIPRO
- BAJFINANCE
- HCLTECH

A cash allocation is also included to allow the portfolio to satisfy different equity exposure requirements.

## Methodology

1. Load historical stock price data.
2. Calculate daily stock returns.
3. Calculate annualized expected returns.
4. Calculate annualized portfolio risk.
5. Calculate the covariance matrix.
6. Generate multiple possible portfolio allocations.
7. Apply the equity allocation range for each risk profile.
8. Calculate the Sharpe Ratio for each portfolio.
9. Select the portfolio with the highest Sharpe Ratio within the applicable constraints.
10. Convert portfolio weights into investment amounts based on available capital.

## Portfolio Evaluation Metrics

### Expected Return

Expected return represents the estimated annual return of the portfolio based on historical data.

### Portfolio Risk

Portfolio risk represents the annualized volatility of the portfolio.

### Sharpe Ratio

The Sharpe Ratio measures the return earned above the risk-free rate relative to portfolio risk.

**Sharpe Ratio = (Portfolio Return − Risk-Free Rate) / Portfolio Risk**

A 6% annual risk-free rate is assumed for this project.

## Final Results

| Risk Profile | Expected Return | Risk | Sharpe Ratio |
|---|---:|---:|---:|
| Conservative | 8.72% | 1.89% | 1.44 |
| Moderate | 18.91% | 8.63% | 1.50 |
| Aggressive | 19.55% | 9.07% | 1.49 |

## Interactive Dashboard

The project includes a **Streamlit dashboard** that allows users to:

- Select a risk profile
- Enter investment capital
- View expected return
- View portfolio risk
- View Sharpe Ratio
- View asset allocation
- View investment amount for each asset
- Visualize portfolio allocation
- Compare expected return and risk

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Streamlit
- Google Colab
- GitHub

## Project Files

- `FinSight_Portfolio_Optimization.ipynb` — Portfolio analysis and optimization notebook
- `app.py` — Streamlit dashboard
- `finsight_portfolio_data.csv` — Historical stock price data
- `finsight_risk_profiles.csv` — Investor risk profile data

## How to Run the Dashboard

Install the required libraries:

```bash
pip install streamlit pandas numpy matplotlib

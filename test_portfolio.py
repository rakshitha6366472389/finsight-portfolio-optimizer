
from pathlib import Path

import numpy as np
import pandas as pd

DATA_FILE = Path(__file__).parent / "finsight_portfolio_data.csv"

def test_portfolio_data_exists():
    assert DATA_FILE.exists(), "Portfolio data CSV is missing"

def test_portfolio_data_and_metrics():
    df = pd.read_csv(DATA_FILE)

    assets = [
        "RELIANCE",
        "TCS",
        "HDFCBANK",
        "INFY",
        "ICICIBANK",
        "WIPRO",
        "BAJFINANCE",
        "HCLTECH",
    ]

    assert all(asset in df.columns for asset in assets)

    prices = df[assets].apply(pd.to_numeric, errors="coerce").dropna()

    assert len(prices) > 1
    assert (prices > 0).all().all()

    returns = prices.pct_change().dropna()

    weights = np.repeat(1 / len(assets), len(assets))

    annual_return = np.dot(returns.mean() * 252, weights)
    covariance = returns.cov() * 252
    annual_risk = np.sqrt(weights @ covariance.values @ weights)

    assert np.isfinite(annual_return)
    assert np.isfinite(annual_risk)
    assert annual_risk >= 0
    assert np.isclose(weights.sum(), 1.0)


import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="FinSight Portfolio Optimizer",
    page_icon="📊",
    layout="wide"
)

# -----------------------------
# Portfolio results
# -----------------------------

portfolio_data = {
    "Profile": ["Conservative", "Moderate", "Aggressive"],
    "Expected Return": [8.7213, 18.9103, 19.5541],
    "Risk": [1.8884, 8.6281, 9.0727],
    "Sharpe Ratio": [1.44, 1.50, 1.49],
    "Capital": [1000000, 250000, 5000000]
}

summary = pd.DataFrame(portfolio_data)

# -----------------------------
# Portfolio allocations
# -----------------------------

allocations = {
    "Conservative": {
        "RELIANCE": 0.004619,
        "TCS": 0.000410,
        "HDFCBANK": 0.003061,
        "INFY": 0.062313,
        "ICICIBANK": 0.040730,
        "WIPRO": 0.030214,
        "BAJFINANCE": 0.000207,
        "HCLTECH": 0.006149,
        "CASH": 0.852298
    },

    "Moderate": {
        "RELIANCE": 0.025688,
        "TCS": 0.014571,
        "HDFCBANK": 0.032510,
        "INFY": 0.219073,
        "ICICIBANK": 0.235040,
        "WIPRO": 0.017736,
        "BAJFINANCE": 0.031046,
        "HCLTECH": 0.122301,
        "CASH": 0.302037
    },

    "Aggressive": {
        "RELIANCE": 0.011776,
        "TCS": 0.006589,
        "HDFCBANK": 0.032056,
        "INFY": 0.292860,
        "ICICIBANK": 0.217697,
        "WIPRO": 0.003183,
        "BAJFINANCE": 0.052295,
        "HCLTECH": 0.071615,
        "CASH": 0.311929
    }
}

# -----------------------------
# Title
# -----------------------------

st.title("📊 FinSight Portfolio Optimizer")

st.write(
    "Portfolio optimization using Modern Portfolio Theory (MPT) "
    "for different investor risk profiles."
)

st.divider()

# -----------------------------
# User inputs
# -----------------------------

col1, col2 = st.columns(2)

with col1:
    profile = st.selectbox(
        "Select Risk Profile",
        ["Conservative", "Moderate", "Aggressive"]
    )

with col2:
    capital = st.number_input(
        "Investment Capital (₹)",
        min_value=10000,
        value=int(
            summary.loc[
                summary["Profile"] == profile,
                "Capital"
            ].iloc[0]
        ),
        step=10000
    )

# -----------------------------
# Selected portfolio
# -----------------------------

selected = summary[
    summary["Profile"] == profile
].iloc[0]

st.subheader("Portfolio Overview")

metric1, metric2, metric3 = st.columns(3)

with metric1:
    st.metric(
        "Expected Return",
        f"{selected['Expected Return']:.2f}%"
    )

with metric2:
    st.metric(
        "Risk",
        f"{selected['Risk']:.2f}%"
    )

with metric3:
    st.metric(
        "Sharpe Ratio",
        f"{selected['Sharpe Ratio']:.2f}"
    )

st.divider()

# -----------------------------
# Allocation
# -----------------------------

st.subheader("Recommended Asset Allocation")

allocation = pd.DataFrame(
    list(allocations[profile].items()),
    columns=["Asset", "Weight"]
)

allocation["Weight"] = allocation["Weight"] * 100
allocation["Investment"] = (
    allocation["Weight"] / 100
) * capital

allocation["Weight"] = allocation["Weight"].round(2)
allocation["Investment"] = allocation["Investment"].round(2)

st.dataframe(
    allocation,
    use_container_width=True,
    hide_index=True
)

# -----------------------------
# Allocation chart
# -----------------------------

st.subheader("Portfolio Allocation")

fig, ax = plt.subplots(figsize=(9, 5))

ax.bar(
    allocation["Asset"],
    allocation["Weight"]
)

ax.set_ylabel("Allocation (%)")
ax.set_xlabel("Asset")
ax.set_title(f"{profile} Portfolio Allocation")

plt.xticks(rotation=45)
plt.tight_layout()

st.pyplot(fig)

# -----------------------------
# Return vs Risk
# -----------------------------

st.subheader("Expected Return vs Risk")

fig2, ax2 = plt.subplots(figsize=(8, 5))

ax2.scatter(
    summary["Risk"],
    summary["Expected Return"],
    s=150
)

for _, row in summary.iterrows():
    ax2.annotate(
        row["Profile"],
        (row["Risk"], row["Expected Return"]),
        xytext=(8, 5),
        textcoords="offset points"
    )

ax2.set_xlabel("Risk (%)")
ax2.set_ylabel("Expected Return (%)")
ax2.set_title("Expected Return vs Risk")
ax2.grid(True)

st.pyplot(fig2)

# -----------------------------
# Footer
# -----------------------------

st.divider()

st.caption(
    "FinSight Portfolio Optimizer | "
    "Portfolio recommendations are generated using historical market data "
    "and a risk-adjusted optimization approach."
)

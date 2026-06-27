
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(layout="wide")
st.title("🚀 Crypto Portfolio Dashboard with Interest Signals")

st.markdown("""
This is your upgraded dashboard. It includes:
- Portfolio allocation pie chart
- BTC halving timeline
- (Placeholder) Signal overlays coming soon
""")

# Portfolio Data
portfolio = {
    "XRP": 11262.70,
    "BTC": 5249.61,
    "PEPE": 3382.90,
    "TRUMP": 1370.95,
    "SOL": 1334.66,
    "DOT": 309.51,
    "XLM": 285.79,
    "ADA": 280.28,
    "AVAX": 255.30,
    "HBAR": 180.59
}
tokens = list(portfolio.keys())
values = list(portfolio.values())

# Pie chart - Portfolio allocation
st.subheader("📊 Portfolio Allocation by Value (GBP)")
fig1, ax1 = plt.subplots()
ax1.pie(values, labels=tokens, autopct='%1.1f%%', startangle=90)
ax1.axis('equal')
st.pyplot(fig1)

# BTC Halving Event Marker (Simulated Price Line)
st.subheader("📅 BTC Price with Halving Event Markers (Placeholder)")
btc_prices = [400, 1000, 9000, 30000, 68000]  # Simulated past halving event prices
halving_years = ["2012", "2016", "2020", "2024*", "2028*"]

fig2, ax2 = plt.subplots()
ax2.plot(halving_years, btc_prices, marker='o')
ax2.set_ylabel("BTC Price (USD)")
ax2.set_title("BTC Halving Events and Price")
st.pyplot(fig2)

st.info("Next: Integrating Google Trends, GitHub, Twitter sentiment overlays...")

# RWA Inflow into XRPL (Placeholder)
st.subheader("🏦 RWA Inflow into XRPL (Placeholder)")
rwa_months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
rwa_inflow_usd_millions = [12, 18, 25, 40, 65, 90]  # Simulated cumulative RWA inflow

fig3, ax3 = plt.subplots()
ax3.plot(rwa_months, rwa_inflow_usd_millions, marker='o', color='green')
ax3.set_ylabel("Cumulative RWA Value on XRPL (USD millions)")
ax3.set_title("Real World Asset Tokenization Inflow on XRP Ledger")
st.pyplot(fig3)

st.caption("Simulated data. Replace with live XRPL issued-currency / RWA.xyz data when available.")

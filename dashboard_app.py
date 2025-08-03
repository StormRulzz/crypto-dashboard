
import streamlit as st
import matplotlib.pyplot as plt

st.title("Crypto Portfolio Dashboard")

st.write("Welcome to your crypto dashboard. This is a placeholder version. Full data integration pending.")

tokens = ["BTC", "ETH", "SOL"]
prices = [30000, 1900, 85]

fig, ax = plt.subplots()
ax.bar(tokens, prices)
st.pyplot(fig)

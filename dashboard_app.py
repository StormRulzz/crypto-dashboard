
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import tweepy
import os

st.set_page_config(layout="wide")
st.title("🚀 Crypto Portfolio Dashboard with Interest Signals")

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

# --- Portfolio Pie Chart ---
st.subheader("📊 Portfolio Allocation by Value (GBP)")
fig1, ax1 = plt.subplots()
ax1.pie(values, labels=tokens, autopct='%1.1f%%', startangle=90)
ax1.axis('equal')
st.pyplot(fig1)

# --- BTC Halving Timeline ---
st.subheader("📅 BTC Price with Halving Event Markers (Placeholder)")
btc_prices = [400, 1000, 9000, 30000, 68000]
halving_years = ["2012", "2016", "2020", "2024*", "2028*"]

fig2, ax2 = plt.subplots()
ax2.plot(halving_years, btc_prices, marker='o')
ax2.set_ylabel("BTC Price (USD)")
ax2.set_title("BTC Halving Events and Price")
st.pyplot(fig2)

# --- X (Twitter) Post Scanner ---
st.subheader("🐦 X.com Post Scanner")

st.info(
    "Uses the official X API v2 (free tier: 500 reads/month). "
    "Add your Bearer Token via the sidebar or set the `X_BEARER_TOKEN` environment variable."
)

bearer_token = st.sidebar.text_input(
    "X API Bearer Token",
    value=os.environ.get("X_BEARER_TOKEN", ""),
    type="password",
    help="Get yours at developer.twitter.com"
)

search_query = st.text_input(
    "Search query",
    value="BTC OR Bitcoin lang:en -is:retweet",
    help="X API v2 search syntax. Use -is:retweet to exclude retweets."
)
max_results = st.slider("Max posts to fetch", min_value=10, max_value=100, value=10, step=10)

if st.button("🔍 Scan X Posts"):
    if not bearer_token:
        st.error("Please enter your X API Bearer Token in the sidebar.")
    else:
        try:
            client = tweepy.Client(bearer_token=bearer_token, wait_on_rate_limit=False)
            with st.spinner("Fetching posts from X..."):
                response = client.search_recent_tweets(
                    query=search_query,
                    max_results=max_results,
                    tweet_fields=["created_at", "author_id", "public_metrics", "text"],
                )

            if not response.data:
                st.warning("No posts found for that query.")
            else:
                rows = []
                for tweet in response.data:
                    m = tweet.public_metrics or {}
                    rows.append({
                        "Text": tweet.text,
                        "Likes": m.get("like_count", 0),
                        "Retweets": m.get("retweet_count", 0),
                        "Replies": m.get("reply_count", 0),
                        "Created": str(tweet.created_at),
                    })
                df = pd.DataFrame(rows)
                st.success(f"Fetched {len(df)} posts.")
                st.dataframe(df, use_container_width=True)

                # Engagement bar chart
                fig3, ax3 = plt.subplots(figsize=(10, 3))
                ax3.bar(range(len(df)), df["Likes"], label="Likes")
                ax3.bar(range(len(df)), df["Retweets"], bottom=df["Likes"], label="Retweets")
                ax3.set_xlabel("Post #")
                ax3.set_ylabel("Engagement")
                ax3.set_title("Post Engagement")
                ax3.legend()
                st.pyplot(fig3)

        except tweepy.errors.Unauthorized:
            st.error("Invalid Bearer Token — check your credentials at developer.twitter.com.")
        except tweepy.errors.TooManyRequests:
            st.error("Rate limit hit. The free tier allows 500 reads/month.")
        except Exception as e:
            st.error(f"Error: {e}")

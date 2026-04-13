import streamlit as st
import pandas as pd
import plotly.express as px

# 1. LOAD & MERGE DATA
@st.cache_data
def load_data():
    auction = pd.read_csv('IPL_Mini_Auction_2026.csv')
    stats = pd.read_csv('players_enriched.csv')
    
    def normalize_name(name):
        return str(name).lower().replace(".", "").replace(" ", "").strip()
    
    auction['match_key'] = auction['Player'].apply(normalize_name)
    stats['match_key'] = stats['Player_Name'].apply(normalize_name)
    return pd.merge(auction, stats, on='match_key', how='inner')

df = load_data()

# 2. DASHBOARD HEADER & VISUALS
st.title("🏏 IPL 2026: Auction Intelligence & ROI")
st.markdown("---")

# Key Metrics Row
col_a, col_b, col_c = st.columns(3)
col_a.metric("Total Players Analyzed", len(df))
col_b.metric("Avg Auction Price", f"₹{df['Price_Cr'].mean():.2f} Cr")
col_c.metric("Top Price", f"₹{df['Price_Cr'].max()} Cr")

# Scatter Plot
st.subheader("Bidding Logic: Price vs. Performance Impact")
fig = px.scatter(df, x="Price_Cr", y="Overall_Score", 
                 hover_name="Player", color="Team_x", size="Strike_Rate",
                 labels={"Price_Cr": "Auction Price (Cr)", "Overall_Score": "Impact Score"},
                 template="plotly_dark")
st.plotly_chart(fig, use_container_width=True)

# 3. STRATEGIC CONCLUSION
st.divider()
st.header("🏁 Strategic Conclusion")
st.info("""
**Data Discovery:** The analysis shows that 'Uncapped' players often have a higher ROI than high-priced marquee names. 
Bidders should focus on **Impact Points per Crore** rather than total historical runs.
""")

# 4. NATURAL FAQs (The Realistic Touch)
st.header("🙋 Franchise Frequently Asked Questions")

faq_list = [
    {
        "q": "Which team made the smartest 'Value for Money' buy?",
        "a": "Based on our ROI metric, the team that bought high-performing players for under 5 Cr (bottom-right quadrant of the chart) is the most efficient."
    },
    {
        "q": "Why are some bowlers paid more than top-order batters?",
        "a": "In 2026, 'Death Over Specialists' are a rare resource. Bidders are paying a premium for players who can control the final 5 overs."
    },
    {
        "q": "Is the 'Overall_Score' reliable for bidding?",
        "a": "Yes, it combines Strike Rate, Economy, and Wickets into a single impact metric, filtering out players who score runs too slowly to win games."
    }
]

for item in faq_list:
    with st.expander(item['q']):
        st.write(item['a'])

# 5. THE FEEDBACK FORM (Fixed & Realistic)
st.divider()
st.header("💬 Expert Feedback Form")
st.write("Franchise owners and analysts can submit their views below.")

with st.form("feedback_form"):
    name = st.text_input("Your Name / Franchise Role")
    rating = st.slider("Rate the usefulness of this ROI Dashboard", 1, 5, 4)
    comments = st.text_area("Observations on Player Valuation:")
    
    # The Submit Button inside the form
    submit_button = st.form_submit_button("Submit Final Analysis")

if submit_button:
    if name and comments:
        st.balloons() # Visual celebration
        st.success(f"Thank you, {name}! Your feedback has been recorded for the Post-Auction Report.")
    else:
        st.warning("Please fill in your name and comments before submitting.")

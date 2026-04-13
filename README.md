🏏 IPL 2026 Auction Intelligence Dashboard
A data-driven web application built to analyze player performance versus auction valuation. This tool helps franchises identify "Value for Money" (ROI) players using advanced statistical merging.

🚀 Live Demo
https://auction-intelligence-dashboard.streamlit.app/

📊 Project Overview
This project was developed as part of my final year B.Sc. studies in Mathematics and Statistics. It bridges the gap between raw cricket statistics and financial decision-making in sports management.

Key Features:
Performance vs. Price Analysis: A dynamic scatter plot correlating Overall_Score with Auction Price (Cr).

Strategic Insights: Automated conclusions on high-ROI players and "Steal" buys.

Interactive Q&A: A dedicated section answering common franchise-owner questions.

Expert Feedback: An integrated form for stakeholders to provide qualitative input.

🛠️ Tech Stack
Language: Python

Data Manipulation: Pandas, NumPy

Visualization: Plotly Express

Web Framework: Streamlit

Deployment: Streamlit Community Cloud

📁 Dataset Details
The analysis is powered by three primary datasets:

IPL_Mini_Auction_2026.csv: Official bidding data.

players_enriched.csv: Detailed performance metrics and "Impact Scores".

ipl_2026_players.csv: Demographic and team-specific data.

⚙️ How to Run Locally
Clone the repository:

Bash
git clone https://github.com/Prachiii2810/IPL-Auction-Analysis-2026.git
Install dependencies:

Bash
pip install -r requirements.txt
Launch the app:

Bash
streamlit run app.py

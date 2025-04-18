import streamlit as st
import pandas as pd
import os

# File to save links
REELS_FILE = 'reels.csv'

# Load existing links if file exists
if os.path.exists(REELS_FILE):
    df = pd.read_csv(REELS_FILE)
    if 'watched' not in df.columns:
        df['watched'] = False
else:
    df = pd.DataFrame(columns=['link', 'watched'])

# ---- Settings ----
st.set_page_config(page_title="Sadia's Reel Manager", page_icon="🎬")

# ---- Force Dark Mode Styling ----
st.markdown(
    """
    <style>
    body {
        background-color: #0E1117;
        color: #FAFAFA;
    }
    .stApp {
        background-color: #0E1117;
        color: #FAFAFA;
    }
    header, footer, .css-18ni7ap.e8zbici2 { 
        background-color: #0E1117;
        color: #FAFAFA;
    }
    </style>
    """,
    unsafe_allow_html=True
)

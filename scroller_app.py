import streamlit as st
import pandas as pd
import os

# File to save links
REELS_FILE = 'reels.csv'

# Load existing links if file exists
if os.path.exists(REELS_FILE):
    df = pd.read_csv(REELS_FILE)
    reel_links = df['link'].tolist()
else:
    reel_links = []

# Title
st.title("💬 My Shared Reels Feed")

# Input for new reel link
new_link = st.text_input("Paste a new Instagram Reel link:")

def format_reel_link(link):
    clean_link = link.split('?')[0]
    if not clean_link.endswith('/'):
        clean_link += '/'
    return clean_link

if st.button("Add Reel"):
    if new_link:
        formatted_link = format_reel_link(new_link)
        reel_links.append(formatted_link)
        pd.DataFrame(reel_links, columns=['link']).to_csv(REELS_FILE, index=False)
        st.success("Reel added successfully!")
        st.rerun()

# Show all reels
st.header("🎥 Your Reels")

for link in reel_links:
    st.markdown(f"[📽️ Watch Reel]({link})", unsafe_allow_html=True)

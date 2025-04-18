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

if st.button("Add Reel"):
    if new_link:
        reel_links.append(new_link)
        pd.DataFrame(reel_links, columns=['link']).to_csv(REELS_FILE, index=False)
        st.success("Reel added successfully!")
        st.experimental_rerun()

# Show all reels
st.header("🎥 Your Reels")

for link in reel_links:
    # Embed the Instagram reel
    st.markdown(f"""
    <iframe src="{link}embed" width="400" height="700" frameborder="0" scrolling="no" allowtransparency="true"></iframe>
    """, unsafe_allow_html=True)

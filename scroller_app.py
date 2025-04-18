import streamlit as st
import pandas as pd
import os

# File to save links
REELS_FILE = 'reels.csv'

# Load existing links if file exists
if os.path.exists(REELS_FILE):
    df = pd.read_csv(REELS_FILE)
else:
    df = pd.DataFrame(columns=['link', 'watched'])

reel_links = df['link'].tolist()
watched_status = df['watched'].tolist()

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
        # Only add if not duplicate
        if formatted_link not in reel_links:
            new_row = pd.DataFrame({'link': [formatted_link], 'watched': [False]})
            df = pd.concat([df, new_row], ignore_index=True)
            df.to_csv(REELS_FILE, index=False)
            st.success("Reel added successfully!")
            st.rerun()
        else:
            st.warning("This reel already exists!")

# Show all reels
st.header("🎥 Your Reels")

for idx, (link, watched) in enumerate(zip(reel_links, watched_status)):
    cols = st.columns([8, 2])  # wider for link, smaller for button

    # Display Reel link
    with cols[0]:
        if watched:
            st.markdown(f"✅ [

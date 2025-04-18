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

# ---- Cute Intro Message ----
st.markdown("""
# 💌 Made with Love
This app was made to help my poor boyfriend keep up with his reel-watchin' duties (20 reels/hour minimum 😎).
""")

# ---- Add Reel Section ----
st.header("✨ For Sadia's Use!")

new_link = st.text_input("Paste a new Instagram Reel link:")

def format_reel_link(link):
    clean_link = link.split('?')[0]
    if not clean_link.endswith('/'):
        clean_link += '/'
    return clean_link

if st.button("Add Reel"):
    if new_link:
        formatted_link = format_reel_link(new_link)
        if formatted_link not in df['link'].values:
            new_row = pd.DataFrame({'link': [formatted_link], 'watched': [False]})
            df = pd.concat([df, new_row], ignore_index=True)
            df.to_csv(REELS_FILE, index=False)
            st.success("Reel added successfully!")
            st.rerun()
        else:
            st.warning("This reel already exists!")

# Divider
st.markdown("---")

# ---- Two Column Layout ----
left_col, right_col = st.columns([1, 3])  # 1/4 width for left, 3/4 for right

with left_col:
    st.header("🎯 Filters & Actions")
    show_only_unwatched = st.checkbox("Show only unwatched reels", value=False)

    if st.button("🧹 Clear All Watched Reels"):
        df = df[df['watched'] == False]
        df.to_csv(REELS_FILE, index=False)
        st.success("Cleared all watched reels!")
        st.balloons()
        st.rerun()

with right_col:
    # ---- Counter ----
    unwatched_count = df[df['watched'] == False].shape[0]
    # ---- Show Reels ----
    st.header(f"🎥 Samsul's Pending Reels ({unwatched_count})")

    if df.empty:
        st.info("No reels yet! Add some links above 👆")
    elif unwatched_count == 0:
        st.success("🥳 Good job baby! You're all caught up with the reels! 🎉")
    else:
        for idx, row in df.iterrows():
            link = row['link']
            watched = row['watched']

            if show_only_unwatched and watched:
                continue

            cols = st.columns([8, 2])

            with cols[0]:
                if watched:
                    st.markdown(f"✅ [Watched Reel]({link})", unsafe_allow_html=True)
                else:
                    st.markdown(f"[📽️ Watch Reel]({link})", unsafe_allow_html=True)

            with cols[1]:
                if not watched:
                    if st.button(f"Mark Watched {idx}"):
                        df.at[idx, 'watched'] = True
                        df.to_csv(REELS_FILE, index=False)
                        st.rerun()

import pandas as pd

# File
REELS_FILE = 'reels.csv'

# Helper to clean links
def format_reel_link(link):
    clean_link = link.split('?')[0]
    if not clean_link.endswith('/'):
        clean_link += '/'
    return clean_link

# Load file
df = pd.read_csv(REELS_FILE)

# Clean all links
df['link'] = df['link'].apply(format_reel_link)

# Save cleaned file
df.to_csv(REELS_FILE, index=False)

print("✅ reels.csv cleaned successfully!")

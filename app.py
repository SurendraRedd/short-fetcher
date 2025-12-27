import streamlit as st
import re
from googleapiclient.discovery import build

# --- APP CONFIG ---
st.set_page_config(page_title="Shorts Data Fetcher", layout="wide")

# --- SIDEBAR: API KEY & INSTRUCTIONS ---
with st.sidebar:
    st.title("Settings")
    api_key = st.text_input("Enter YouTube API Key", type="password", help="Get this from Google Cloud Console")
    
    with st.expander("🔑 How to get an API Key?"):
        st.markdown("""
        1. Go to [Google Cloud Console](https://console.cloud.google.com/).
        2. Create a new project.
        3. Enable **'YouTube Data API v3'**.
        4. Go to **Credentials** > **+ Create Credentials** > **API Key**.
        """)
    st.info("The API Key is required to fetch data.")

# --- FUNCTIONS ---
def extract_id(url):
    pattern = r'(?:shorts\/|v=|be\/)([0-9A-Za-z_-]{11})'
    match = re.search(pattern, url)
    return match.group(1) if match else None

def get_video_description(v_id, key):
    try:
        youtube = build('youtube', 'v3', developerKey=key)
        request = youtube.videos().list(part="snippet", id=v_id)
        response = request.execute()
        if response['items']:
            return response['items'][0]['snippet']['description']
        return "No description found."
    except Exception as e:
        return f"Error: {e}"

# --- MAIN GUI ---
st.title("🎥 AWS Solutions Architect Questions Description Fetcher")

# Define two columns for side-by-side layout
col1, col2 = st.columns([1, 2], gap="small")

with col1:
    st.subheader("Step 1: Enter URL")
    default_url = "https://www.youtube.com/shorts/3o3QSvikxco"
    url_input = st.text_input("Paste Short Link", value=default_url)
    fetch_button = st.button("Fetch Description", type="primary", use_container_width=True)

with col2:
    st.subheader("Step 2: Details")
    if fetch_button:
        if not api_key:
            st.warning("Please enter your API Key in the sidebar!")
        elif not url_input:
            st.warning("Please enter a URL.")
        else:
            video_id = extract_id(url_input)
            if video_id:
                with st.spinner("Fetching..."):
                    desc = get_video_description(video_id, api_key)
                    st.markdown("**Video Description:**")
                    st.text_area(label="Output", value=desc, height=500, label_visibility="collapsed")
            else:
                st.error("Invalid YouTube URL.")
import streamlit as st

st.markdown(
    """
    <style>
    /* 1. Full‑page gradient background */
    .stApp {
        background: linear-gradient(135deg, #feda75 0%, #fa7e1e 50%, #d62976 100%);
        min-height: 100vh;
    }

    /* 2. Main content container styling */
    .main .block-container {
        background-color: #FFFFFF !important;  /* solid white */
        border-radius: 1rem !important;
        box-shadow: 0 4px 20px rgba(0,0,0,0.1) !important;
        padding: 2rem 4rem !important;
    }

    /* 3. Header styling */
    .stTitle, .stSubheader {
        color: #111111 !important;
        text-shadow: 0 1px 3px rgba(0,0,0,0.1);
    }

    /* 4. Buttons and inputs */
    .stButton>button {
        background-color: #405DE6 !important;
        color: white !important;
        border-radius: 0.5rem !important;
        padding: 0.6rem 1.2rem !important;
    }
    .stTextInput>div>div>input, .stSelectbox>div>div>div>select {
        border: 1px solid #ccc !important;
        border-radius: 0.5rem !important;
        padding: 0.6rem !important;
        background-color: #fafafa !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

import streamlit as st
from generator import generate_caption

st.set_page_config(page_title="Greycuff Caption AI", layout="centered")
st.title("🪄 Greycuff: Instagram Caption Generator")

topic = st.text_input("📝 Topic (e.g. travel, food):")
mood = st.selectbox("😄 Mood", ["Funny", "Romantic", "Motivational", "Savage", "Sad"])
style = st.selectbox("🎨 Style", ["Poetic", "Emoji-rich", "Minimalist", "Trendy", "Hashtag-heavy"])

if st.button("✨ Generate Caption"):
    if not topic:
        st.warning("Please enter a topic.")
    else:
        with st.spinner("Creating your caption..."):
            caption = generate_caption(topic, mood, style)
            st.success("Here’s your caption:")
            st.write(f"> {caption}")

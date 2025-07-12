import streamlit as st
from generator import generate_caption

# ─── Page Config ──────────────────────────────────────────────────────────────
st.set_page_config(page_title="Greycuff Caption AI", layout="wide")

# ─── Custom CSS for Input Blocks ───────────────────────────────────────────────
st.markdown(
    """
    <style>
    /* 1. Make the whole page white */
    .stApp {
      background-color: #FFFFFF;
    }

    /* 2. Style for each input/block container */
    .stTextInput > div, .stSelectbox > div, .stButton > button {
      background-color: #F7F7F7 !important;
      border: 1px solid #E1E1E1 !important;
      border-radius: 0.75rem !important;
      padding: 1rem !important;
      margin-bottom: 1rem !important;
    }

    /* 3. Ensure selectboxes fill the width */
    .stSelectbox > div > div {
      width: 100% !important;
    }
    .stTextInput > div > div > input {
      width: 100% !important;
    }

    /* 4. Style the Generate button separately */
    .stButton > button {
      background-color: #405DE6 !important;
      color: white !important;
      font-size: 1rem !important;
      padding: 0.75rem 1.5rem !important;
      width: auto;
    }

    /* 5. Card around title/subheader for emphasis */
    .stTitle, .stSubheader {
      padding: 0.5rem 1rem !important;
      background-color: #FFFB8F !important;
      border-radius: 0.5rem !important;
      display: inline-block !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ─── Header ───────────────────────────────────────────────────────────────────
st.title("🪄 Greycuff: Instagram Caption Generator")
st.subheader("Generate catchy, emoji‑filled captions in seconds!")

# ─── Input Blocks ─────────────────────────────────────────────────────────────
# 1. Topic
topic = st.text_input("📝 Topic (e.g. travel, food):", max_chars=100)

# 2. Mood
mood = st.selectbox(
    "😄 Mood",
    ["Funny", "Romantic", "Motivational", "Savage", "Sad"]
)

# 3. Style
style = st.selectbox(
    "🎨 Style",
    ["Poetic", "Emoji‑rich", "Minimalist", "Trendy", "Hashtag‑heavy"]
)

# ─── Generate Button & Output ────────────────────────────────────────────────
if st.button("✨ Generate Caption"):
    if not topic.strip():
        st.warning("Please enter a topic to generate a caption.")
    else:
        with st.spinner("Creating your caption..."):
            caption = generate_caption(topic, mood, style)
        st.success("Here’s your caption:")
        st.markdown(f"> {caption}")

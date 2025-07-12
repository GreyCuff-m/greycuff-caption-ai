import streamlit as st
from generator import generate_caption

# ───── Inject Custom CSS ─────
st.markdown(
    """
    <style>
    /* 1. Solid white background + crayon emoji tiling */
    .stApp {
      background-color: #FFFFFF;
      background-image: url('https://twemoji.maxcdn.com/v/latest/72x72/1f58d.png');
      background-repeat: repeat;
      background-size: 60px 60px;
    }

    /* 2. Main container: keep it opaque white */
    .main .block-container {
      background-color: #FFFFFF !important;
      border-radius: 1rem !important;
      box-shadow: 0 4px 20px rgba(0,0,0,0.05) !important;
      padding: 2rem 3rem !important;
    }

    /* 3. Highlight your title & subheader */
    .stTitle > div, .stSubheader > div {
      background-color: #FFFB8F;
      padding: 0.2rem 0.5rem;
      border-radius: 0.25rem;
      display: inline-block;
    }

    /* 4. Inputs & buttons: subtle rounded style */
    .stTextInput > div > div > input,
    .stSelectbox > div > div > div > select {
      border: 1px solid #ccc !important;
      border-radius: 0.5rem !important;
      padding: 0.5rem !important;
      background-color: #fbfbfb !important;
    }
    .stButton > button {
      background-color: #405DE6 !important;
      color: white !important;
      border-radius: 0.5rem !important;
      padding: 0.6rem 1.2rem !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ───── Page Config & Title ─────
st.set_page_config(page_title="Greycuff Caption AI", layout="centered")

st.title("🪄 Greycuff: Instagram Caption Generator")
st.subheader("Generate catchy, emoji‑filled captions in seconds!")

# ───── User Inputs ─────
topic = st.text_input("📝 Topic (e.g. travel, food):")
mood = st.selectbox(
    "😄 Mood",
    ["Funny", "Romantic", "Motivational", "Savage", "Sad"]
)
style = st.selectbox(
    "🎨 Style",
    ["Poetic", "Emoji‑rich", "Minimalist", "Trendy", "Hashtag‑heavy"]
)

# ───── Generate Button ─────
if st.button("✨ Generate Caption"):
    if not topic.strip():
        st.warning("Please enter a topic to generate a caption.")
    else:
        with st.spinner("Creating your caption..."):
            caption = generate_caption(topic, mood, style)
            st.success("Here’s your caption:")
            st.write(f"> {caption}")

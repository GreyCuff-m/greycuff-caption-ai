import streamlit as st
from generator import generate_caption

# ─── Inject Custom CSS ──────────────────────────────────────────────────────
st.markdown(
    """
    <style>
    /* 1. Crayon emoji tiled on a solid white page */
    .stApp {
      background-color: #FFFFFF !important;
      background-image: url('https://twemoji.maxcdn.com/v/latest/72x72/1f58d.png') !important;
      background-repeat: repeat !important;
      background-size: 60px 60px !important;
    }

    /* 2. Card around the main content */
    .block-container {
      background-color: #FFFFFF !important;
      border-radius: 1rem !important;
      box-shadow: 0 4px 20px rgba(0,0,0,0.05) !important;
      padding: 2rem 3rem !important;
    }

    /* 3. Highlight both h1 & h2 (title + subheader) */
    h1, h2 {
      background-color: #FFFB8F !important;
      padding: 0.3rem 0.6rem !important;
      border-radius: 0.25rem !important;
      display: inline-block !important;
    }

    /* 4. Inputs & selects */
    input, select, textarea {
      border: 1px solid #ccc !important;
      border-radius: 0.5rem !important;
      padding: 0.5rem !important;
      background-color: #fbfbfb !important;
    }

    /* 5. Buttons */
    button.stButton>button {
      background-color: #405DE6 !important;
      color: white !important;
      border-radius: 0.5rem !important;
      padding: 0.6rem 1.2rem !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ─── Page Config & Header ──────────────────────────────────────────────────
st.set_page_config(page_title="Greycuff Caption AI", layout="centered")
st.title("🪄 Greycuff: Instagram Caption Generator")
st.subheader("Generate catchy, emoji‑filled captions in seconds!")

# ─── User Inputs ────────────────────────────────────────────────────────────
topic = st.text_input("📝 Topic (e.g. travel, food):")
mood = st.selectbox("😄 Mood", ["Funny", "Romantic", "Motivational", "Savage", "Sad"])
style = st.selectbox("🎨 Style", ["Poetic", "Emoji‑rich", "Minimalist", "Trendy", "Hashtag‑heavy"])

# ─── Generate Button & Output ───────────────────────────────────────────────
if st.button("✨ Generate Caption"):
    if not topic.strip():
        st.warning("Please enter a topic to generate a caption.")
    else:
        with st.spinner("Creating your caption..."):
            caption = generate_caption(topic, mood, style)
            st.success("Here’s your caption:")
            st.write(f"> {caption}")

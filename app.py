import streamlit as st
from generator import generate_caption

# ─── Page Configuration ───────────────────────────────────────────────────────
st.set_page_config(
    page_title="Greycuff Caption AI",
    layout="wide",
)

# ─── Header ───────────────────────────────────────────────────────────────────
st.title("🪄 Greycuff: Instagram Caption Generator")
st.subheader("Generate catchy, emoji‑filled captions in seconds!")

# ─── User Inputs ──────────────────────────────────────────────────────────────
topic = st.text_input(
    "📝 Topic (e.g. travel, food):",
    max_chars=100,
)

mood = st.selectbox(
    "😄 Mood",
    ["Funny", "Romantic", "Motivational", "Savage", "Sad"],
)

style = st.selectbox(
    "🎨 Style",
    ["Poetic", "Emoji‑rich", "Minimalist", "Trendy", "Hashtag‑heavy"],
)

# ─── Generate Button & Output ────────────────────────────────────────────────
if st.button("✨ Generate Caption"):
    if not topic.strip():
        st.warning("Please enter a topic to generate a caption.")
    else:
        with st.spinner("Creating your caption..."):
            caption = generate_caption(topic, mood, style)
        st.success("Here’s your caption:")
        st.write(f"> {caption}")

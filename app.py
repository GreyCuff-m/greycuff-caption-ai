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

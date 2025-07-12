import streamlit as st

st.markdown(
    """
    <style>
      /* Full-page background */
      .stApp {
        background: url('https://images.unsplash.com/photo-1498050108023-c5249f4df085?ixlib=rb-4.0') center/cover no-repeat;
      }
      /* App content container */
      .main .block-container {
        background-color: rgba(255,255,255,0.8);
        border-radius: 12px;
        padding: 2rem;
      }
      /* Title style */
      .css-uf99v8 h1 {
        font-family: 'Arial Black', sans-serif;
        color: #4B4E6D;
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

import streamlit as st

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
      background-color: #FFFB8F;  /* soft yellow */
      padding: 0.2rem 0.5rem;
      border-radius: 0.25rem;
      display: inline-block;
    }

    /* 4. Inputs & buttons: subtle rounded style */
    .stTextInput>div>div>input,
    .stSelectbox>div>div>div>select {
      border: 1px solid #ccc !important;
      border-radius: 0.5rem !important;
      padding: 0.5rem !important;
      background-color: #fbfbfb !important;
    }
    .stButton>button {
      background-color: #405DE6 !important;
      color: white !important;
      border-radius: 0.5rem !important;
      padding: 0.6rem 1.2rem !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

import streamlit as st

st.markdown(
    <style>
    /* 1. Full‑page gradient background */
    .stApp {
        background: linear-gradient(135deg, #feda75 0%, #fa7e1e 50%, #d62976 100%);
        min-height: 100vh;
    }
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

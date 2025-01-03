import streamlit as st
from Langflow import GPT_insight

st.title("Social Media Performance Analysis")

social_media_platform = st.selectbox(
    "Select a Social Media Platform:",
    ["Facebook", "LinkedIn", "Instagram", "X"]
)

post_type = st.selectbox(
    "Select a Post Type:",
    ["Link", "Post", "Video or Reel"]
)

def analyze():
    try:
        with st.spinner("Analyzing..."):
            # Generate GPT insight
            response = GPT_insight(platform=social_media_platform, post_type=post_type)
        st.subheader("GPT Insight")
        st.write(response)
    except KeyError:
        st.error("GPT token reached limit. Please try again.")

if st.button("Analyze"):
    analyze()

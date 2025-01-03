import time
import streamlit as st
from Langflow import GPT_insight

# Page title
st.title("Social Media Performance Analysis")

# Dropdown menu for Social Media Platform
social_media_platform = st.selectbox(
    "Select a Social Media Platform:",
    ["Facebook", "LinkedIn", "Instagram", "X"]
)

# Dropdown menu for Post Type
post_type = st.selectbox(
    "Select a Post Type:",
    ["Link", "Post", "Video or Reel"]
)

# Button to trigger analysis
if st.button("Analyze"):
    # Display loading spinner with "Analyzing..." text
    with st.spinner("Analyzing..."):
        # Simulate some delay for analysis (optional)
        time.sleep(2)  # Remove or adjust as per real response time

        # Generate GPT insight
        response = GPT_insight(platform=social_media_platform, post_type=post_type)

    # Display GPT Insight in the UI
    st.subheader("GPT Insight")
    st.write(response)

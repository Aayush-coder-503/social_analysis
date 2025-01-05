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

# Add a red-colored note below the button
st.markdown(
    """
    <div style="color: red; font-weight: bold; margin-top: 20px;">
        Note: We are using a free API key for vector embedding and for LLM. Token can reach its limit.
    </div>
    """,
    unsafe_allow_html=True
)

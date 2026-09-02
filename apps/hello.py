"""
Hello Streamlit — your very first app!
=======================================

Run this file to verify your environment is set up correctly:

    streamlit run apps/hello.py

If you see a welcome page, you're ready for Module 01.
"""

import streamlit as st

# ---------------------------------------------------------------------------
# Page configuration (must be the first Streamlit call)
# ---------------------------------------------------------------------------
st.set_page_config(
    page_title="Hello Streamlit",
    page_icon="👋",
    layout="centered",
)

# ---------------------------------------------------------------------------
# Main content
# ---------------------------------------------------------------------------
st.title("👋 Hello, Streamlit!")
st.markdown(
    "Welcome to **Streamlit for Data Science — Learn, Build, Deploy**.\n\n"
    "This starter app confirms your environment is working. "
    "If you can see this page, you're all set for Module 01."
)

st.divider()

st.header("Quick Checklist")
st.checkbox("Python 3.10+ installed", value=True, disabled=True)
st.checkbox("Streamlit installed", value=True, disabled=True)
st.checkbox("Repository cloned", value=True, disabled=True)

st.divider()

# ---------------------------------------------------------------------------
# A tiny interactive demo — proves widgets work
# ---------------------------------------------------------------------------
st.subheader("🎮 Quick Demo")

name = st.text_input("What is your name?", placeholder="Enter your name here")

if name:
    st.success(f"Hello, **{name}**! Your Streamlit environment is working perfectly. 🎉")
else:
    st.info("Type your name above to see the widget in action.")

st.divider()
st.caption(
    "Next step → Open `notebooks/01_first_streamlit_app.ipynb` to start Module 01."
)

"""
01 — Introduction Demo
======================
A beginner-friendly Streamlit app demonstrating core concepts
from Module 01: what Streamlit is, text elements, and the rerun model.

Run this app:
    streamlit run apps/01_introduction_demo.py

Related Materials:
- 📓 Notebook: notebooks/01_Streamlit_Introduction.ipynb
- 📓 Notebook: notebooks/02_First_Streamlit_App.ipynb
- 📖 Reading: readings/01_streamlit_introduction.md
- 📖 Reading: readings/02_first_streamlit_app.md
"""

import streamlit as st
import pandas as pd
import numpy as np

# ---------------------------------------------------------------------------
# 1. PAGE CONFIG — must be the first st. call!
# ---------------------------------------------------------------------------
st.set_page_config(
    page_title="01 — Introduction Demo",
    page_icon="🚀",
    layout="centered",
)

# ---------------------------------------------------------------------------
# 2. TITLE AND DESCRIPTION
# ---------------------------------------------------------------------------
st.title("🚀 Streamlit Introduction Demo")
st.markdown(
    "Welcome to the **first demo app** for Module 01!\n\n"
    "This app demonstrates the core Streamlit concepts you've learned about:\n"
    "text elements, the rerun model, and basic data display."
)

st.divider()

# ---------------------------------------------------------------------------
# 3. TEXT ELEMENTS SHOWCASE
# ---------------------------------------------------------------------------
st.header("📝 Text Elements")
st.write("Here are the main text-rendering functions in Streamlit:")

st.subheader("This is a subheader (h3)")
st.markdown("**Bold text** and *italic text* via Markdown.")
st.caption("This is a caption — small gray text for annotations.")

st.divider()

# ---------------------------------------------------------------------------
# 4. CODE BLOCK DISPLAY
# ---------------------------------------------------------------------------
st.header("💻 Code Display")
st.code(
    'import streamlit as st\n\n'
    'st.title("My App")\n'
    'st.write("Hello, world!")',
    language="python",
)

st.divider()

# ---------------------------------------------------------------------------
# 5. POLYMORPHIC st.write()
# ---------------------------------------------------------------------------
st.header("🎨 Polymorphic st.write()")
st.write("st.write() renders different data types appropriately:")

st.write("**String:**", "This is a plain string.")
st.write(
    "**DataFrame:**",
    pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]}),
)
st.write("**Dictionary:**", {"framework": "Streamlit", "language": "Python"})

st.divider()

# ---------------------------------------------------------------------------
# 6. THE RERUN MODEL — Interactive Demo
# ---------------------------------------------------------------------------
st.header("🔄 The Rerun Model")
st.markdown(
    "Every time you interact with a widget, the **entire script reruns**.\n"
    "Try clicking the button below — watch the random number change!"
)

if st.button("🎲 Generate Random Number"):
    st.write(f"Your random number: **{np.random.randint(1, 100)}**")

st.divider()

# ---------------------------------------------------------------------------
# 7. BASIC DATA DISPLAY
# ---------------------------------------------------------------------------
st.header("📊 Basic Data Display")

np.random.seed(42)
df = pd.DataFrame(
    {
        "Student": [f"S{i+1}" for i in range(10)],
        "Score": np.random.randint(60, 100, 10),
        "Grade": np.random.choice(["A", "B", "C"], 10),
    }
)

st.dataframe(df, use_container_width=True)

st.divider()

# ---------------------------------------------------------------------------
# 8. FOOTER
# ---------------------------------------------------------------------------
st.caption(
    "Built with Streamlit • Module 01 • "
    "[Streamlit Docs](https://docs.streamlit.io/)"
)

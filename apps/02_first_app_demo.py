"""
02 — First App Demo
===================
A complete beginner Streamlit app demonstrating:
- Proper app structure (imports → config → title → data → display)
- The rerun model with st.session_state
- Text elements and data display
- Practical Data Science use case

Run this app:
    streamlit run apps/02_first_app_demo.py

Related Materials:
- 📓 Notebook: notebooks/01_Streamlit_Introduction.ipynb
- 📓 Notebook: notebooks/02_First_Streamlit_App.ipynb
- 📖 Reading: readings/02_first_streamlit_app.md
"""

import streamlit as st
import pandas as pd
import numpy as np

# ---------------------------------------------------------------------------
# 1. IMPORTS (always at the top)
# ---------------------------------------------------------------------------

# ---------------------------------------------------------------------------
# 2. PAGE CONFIG (must be first st. call!)
# ---------------------------------------------------------------------------
st.set_page_config(
    page_title="Student Grade Analyzer",
    page_icon="🎓",
    layout="centered",
)

# ---------------------------------------------------------------------------
# 3. TITLE AND DESCRIPTION
# ---------------------------------------------------------------------------
st.title("🎓 Student Grade Analyzer")
st.markdown(
    "Welcome to the **Student Grade Analyzer**!\n\n"
    "This app demonstrates a practical Streamlit application:\n"
    "- Generate sample student data\n"
    "- Display it interactively\n"
    "- Show summary statistics\n"
    "- Visualize grade distributions"
)

st.divider()

# ---------------------------------------------------------------------------
# 4. GENERATE SAMPLE DATA
# ---------------------------------------------------------------------------
np.random.seed(42)
n_students = 30

data = pd.DataFrame(
    {
        "Student": [f"Student {i+1}" for i in range(n_students)],
        "Math": np.random.randint(50, 100, n_students),
        "Science": np.random.randint(50, 100, n_students),
        "English": np.random.randint(50, 100, n_students),
    }
)
data["Average"] = data[["Math", "Science", "English"]].mean(axis=1).round(1)
data["Grade"] = data["Average"].apply(
    lambda x: (
        "A"
        if x >= 90
        else "B"
        if x >= 80
        else "C"
        if x >= 70
        else "D"
        if x >= 60
        else "F"
    )
)

# ---------------------------------------------------------------------------
# 5. METRICS OVERVIEW
# ---------------------------------------------------------------------------
st.header("📈 Overview")

col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Students", len(data))
col2.metric("Average Score", f"{data['Average'].mean():.1f}")
col3.metric("Highest Average", f"{data['Average'].max():.1f}")
col4.metric("Lowest Average", f"{data['Average'].min():.1f}")

st.divider()

# ---------------------------------------------------------------------------
# 6. DISPLAY DATA
# ---------------------------------------------------------------------------
st.header("📊 Student Grades")
st.dataframe(data, use_container_width=True)

st.divider()

# ---------------------------------------------------------------------------
# 7. SUMMARY STATISTICS
# ---------------------------------------------------------------------------
st.header("📉 Summary Statistics")
st.write(data[["Math", "Science", "English", "Average"]].describe().round(1))

st.divider()

# ---------------------------------------------------------------------------
# 8. GRADE DISTRIBUTION
# ---------------------------------------------------------------------------
st.header("🎯 Grade Distribution")
grade_counts = data["Grade"].value_counts().sort_index()
st.bar_chart(grade_counts)

st.divider()

# ---------------------------------------------------------------------------
# 9. SESSION STATE DEMO — Rerun Model in Action
# ---------------------------------------------------------------------------
st.header("🔄 Rerun Model Demo")
st.markdown(
    "Click the button below. Notice how the counter **persists** across reruns "
    "because we use `st.session_state`."
)

if "click_count" not in st.session_state:
    st.session_state.click_count = 0

if st.button("➕ Click Me"):
    st.session_state.click_count += 1

st.write(f"You've clicked **{st.session_state.click_count}** times.")

st.divider()

# ---------------------------------------------------------------------------
# 10. FOOTER
# ---------------------------------------------------------------------------
st.caption(
    "Built with Streamlit • Module 01 • Student Grade Analyzer Demo • "
    "[Docs](https://docs.streamlit.io/)"
)

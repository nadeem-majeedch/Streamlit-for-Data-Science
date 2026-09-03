"""
Exercise 01 — Hello Streamlit SOLUTION
========================================
INSTRUCTOR USE ONLY — Do not share with students.

Reference implementation with all TODOs completed.
Run: streamlit run instructor/solutions/exercises_solutions/01_hello_streamlit_solution.py
"""

import streamlit as st
import pandas as pd
import numpy as np

# ---------------------------------------------------------------------------
# Page Config
# ---------------------------------------------------------------------------
st.set_page_config(
    page_title="Exercise 01 — Hello Streamlit (SOLUTION)",
    page_icon="✅",
    layout="centered",
)

st.title("✅ Exercise 01 — Hello Streamlit (Solution)")
st.markdown("Complete reference implementation for instructor use.")
st.divider()

# ============================================================================
# PART 1 — Text Elements
# ============================================================================

st.header("Part 1 — Text Elements")

# TODO 1a: Title
st.title("My Streamlit App")

# TODO 1b: Subtitle
st.header("Welcome to Data Science")
st.subheader("Learning Streamlit, one app at a time")

# TODO 1c: Paragraph
st.write("Streamlit makes it easy to build interactive data apps in pure Python.")
st.markdown("**Streamlit** is an open-source app framework for *Data Science* teams.")

# TODO 1d: Caption
st.caption("Created as part of Module 01 — Streamlit Fundamentals")

# TODO 1e: Code block
st.code('print("Hello, Streamlit!")', language="python")

# TODO 1f: LaTeX
st.latex(r"E = mc^2")

st.divider()

# ============================================================================
# PART 2 — Data Display
# ============================================================================

st.header("Part 2 — Display Data")

# TODO 2a: Dictionary
students = {"Alice": 95, "Bob": 87, "Carol": 92, "Dave": 78}
st.write("**Student Grades:**", students)

# TODO 2b: DataFrame with st.dataframe()
df = pd.DataFrame({
    "Name": ["Alice", "Bob", "Carol", "Dave", "Eve"],
    "Score": [95, 87, 92, 78, 88],
    "Grade": ["A", "B+", "A", "C+", "B+"],
})
st.subheader("Student Scores (DataFrame)")
st.dataframe(df, use_container_width=True, hide_index=True)

# TODO 2c: Same data with st.table()
st.subheader("Student Scores (Table)")
st.table(df)

# Difference: st.dataframe() is interactive (sortable, scrollable, resizable),
# while st.table() is a static, formatted table.

# TODO 2d: NumPy array
arr = np.random.randn(10)
st.subheader("Random Numbers")
st.write("NumPy array:", arr)

st.divider()

# ============================================================================
# PART 3 — Student Report Card
# ============================================================================

st.header("Part 3 — Student Report Card")

st.title("Student Report Card")

student_name = "Alex Johnson"
st.markdown(f"**Student:** {student_name}")

subjects = pd.DataFrame({
    "Subject": ["Mathematics", "Physics", "Computer Science"],
    "Score": [92, 85, 97],
})
st.dataframe(subjects, use_container_width=True, hide_index=True)

average = subjects["Score"].mean()
st.metric(label="Average Score", value=f"{average:.1f}", delta="+5.3")

from datetime import date
st.caption(f"Report generated on {date.today().strftime('%B %d, %Y')}")

st.divider()

# ============================================================================
# PARTS 4 & 5 — Theory (no code needed, answers in exercise file)
# ============================================================================

st.header("Parts 4 & 5 — Theory Questions")
st.info("See the exercise file for output prediction and scenario questions.")

st.divider()
st.caption("Solution: Exercise 01 — Hello Streamlit · Module 01")

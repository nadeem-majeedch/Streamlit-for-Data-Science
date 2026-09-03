"""
Exercise 01 — Hello Streamlit
==============================
Module 01 · Beginner

Master the fundamentals of Streamlit text rendering and app structure.

Run this file:
    streamlit run exercises/01_hello_streamlit.py

Instructions:
    Complete every TODO section. Run the app after each step.
    Do NOT copy from the notebook — write every line yourself.

Related Materials:
- Reading: ../readings/01_streamlit_introduction.md
- Reading: ../readings/02_first_streamlit_app.md
- Notebook: ../notebooks/01_Streamlit_Introduction.ipynb
- Notebook: ../notebooks/02_First_Streamlit_App.ipynb
- Demo App: ../apps/01_introduction_demo.py
"""

import streamlit as st
import pandas as pd
import numpy as np

# ---------------------------------------------------------------------------
# Page Config
# ---------------------------------------------------------------------------
st.set_page_config(
    page_title="Exercise 01 — Hello Streamlit",
    page_icon="✏️",
    layout="centered",
)

st.title("✏️ Exercise 01 — Hello Streamlit")
st.markdown(
    "Complete every TODO below. Run the app after each step to verify."
)

st.divider()

# ============================================================================
# PART 1 — Text Elements (Understanding)
# ============================================================================

st.header("Part 1 — Text Elements")

# TODO 1a: Add a main title using st.title()
# TODO 1b: Add a subtitle using st.header() or st.subheader()
# TODO 1c: Add a paragraph of text using st.write() or st.markdown()
# TODO 1d: Add a caption using st.caption()
# TODO 1e: Add a code block showing `print("Hello, Streamlit!")`
#         using st.code()
# TODO 1f: Add a LaTeX formula using st.latex(r"E = mc^2")

# Your code here:

st.divider()

# ============================================================================
# PART 2 — Data Display (Small Modification)
# ============================================================================

st.header("Part 2 — Display Data")

# TODO 2a: Create a small dictionary with 4 students and their grades,
#         then display it with st.write()

# TODO 2b: Create a Pandas DataFrame with columns "Name", "Score", "Grade"
#         for 5 students. Display it with st.dataframe()

# TODO 2c: Display the same DataFrame using st.table() instead.
#         What is the difference between st.dataframe() and st.table()?

# TODO 2d: Create a NumPy array with 10 random numbers.
#         Display it with st.write() and observe the formatting.

# Your code here:

st.divider()

# ============================================================================
# PART 3 — App Structure (Simple Coding)
# ============================================================================

st.header("Part 3 — App Structure Challenge")

# CHALLENGE: Build a mini "Student Report Card" app that shows:
#   1. A title: "Student Report Card"
#   2. Student name in bold using markdown
#   3. A DataFrame with 3 subjects and scores
#   4. The average score calculated and displayed as a metric
#   5. A caption showing today's date
#
# Structure your code with clear sections using st.divider()

# Your code here:

# ============================================================================
# PART 4 — Output Prediction
# ============================================================================

st.divider()
st.header("Part 4 — Output Prediction")

st.markdown("""
Before running, predict what each code snippet outputs:

**Q1:** What does `st.write("Hello", "World")` display?
- A) Two separate lines
- B) "Hello World" on one line
- C) A tuple `("Hello", "World")`

**Q2:** What does `st.write(1 + 1)` display?
- A) `2`
- B) `"1 + 1"`
- C) Error

**Q3:** What happens if `st.set_page_config()` is NOT the first
Streamlit call?
- A) Nothing — it works fine
- B) Streamlit raises an exception
- C) The page config is ignored

<details>
<summary>Click to check answers</summary>

Q1: **B** — `st.write` concatenates multiple arguments with spaces.
Q2: **A** — `st.write` evaluates Python expressions and renders the result.
Q3: **B** — Streamlit raises `st.set_page_config can only be called once per page`.

</details>
""")

st.divider()

# ============================================================================
# PART 5 — Scenario Question
# ============================================================================

st.header("Part 5 — Scenario Question")

st.markdown("""
Your professor asks you to build a Streamlit app that:
1. Shows a title "Class Survey Results"
2. Displays a table of survey responses
3. Shows a summary statistic

A student writes this code:

```python
import streamlit as st
import pandas as pd

st.dataframe({"Q1": ["Yes", "No"], "Q2": [5, 3]})
st.title("Class Survey Results")
st.metric("Average Q2", 4.0)
```

**What is wrong with this code?** (Select all that apply)

A) The title appears after the data — looks disorganized
B) `st.set_page_config()` is missing
C) The metric label should be lowercase
D) Nothing — the code is correct

<details>
<summary>Answer</summary>

**A and B.** The `st.title()` should come before `st.dataframe()` for logical
ordering, and `st.set_page_config()` must be the very first Streamlit call
(ideally before any other st.* call). While B won't always cause a visible
error if it's the first call in the file, it is a structural requirement.

</details>
""")

st.divider()
st.caption("Exercise 01 complete. Proceed to Exercise 03 for widget mastery.")

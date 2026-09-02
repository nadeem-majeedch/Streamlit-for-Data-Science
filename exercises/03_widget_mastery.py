"""
✏️ Exercise 03 — Widget Mastery
================================
Module 02 · Beginner

Build a Streamlit app that demonstrates mastery of every core widget type.

Run this file:
    streamlit run exercises/03_widget_mastery.py

Instructions:
    Complete the TODO sections below. Each TODO asks you to add a specific
    widget with certain requirements. Run the app after each step to verify.

Related Materials:
- 📖 Reading: ../readings/03_streamlit_widgets_and_input.md
- 📓 Notebook: ../notebooks/03_streamlit_widgets.ipynb
- 🖥️ Demo App: ../apps/03_widgets_demo.py
"""

import streamlit as st

# ---------------------------------------------------------------------------
# Page Config
# ---------------------------------------------------------------------------
st.set_page_config(
    page_title="Exercise 03 — Widget Mastery",
    page_icon="✏️",
    layout="centered",
)

st.title("✏️ Exercise 03 — Widget Mastery")
st.markdown(
    "Complete each TODO section below. Run the app after each step to verify."
)

st.divider()

# ---------------------------------------------------------------------------
# Part 1: Buttons & Toggles
# ---------------------------------------------------------------------------
st.header("Part 1: Buttons & Toggles")

# TODO 1: Add a button that, when clicked, shows "Hello, Streamlit!"
# Hint: Use st.button() with an if statement


st.divider()

# ---------------------------------------------------------------------------
# Part 2: Selection Widgets
# ---------------------------------------------------------------------------
st.header("Part 2: Selection Widgets")

# TODO 2: Add a selectbox with 3 programming languages.
# Display the selected language below the selectbox.


# TODO 3: Add a multiselect for choosing skills (at least 5 options).
# Display the selected skills as a bulleted list.


# TODO 4: Add a radio button for choosing a favorite color (horizontal layout).
# Display the selected color.


st.divider()

# ---------------------------------------------------------------------------
# Part 3: Text Input
# ---------------------------------------------------------------------------
st.header("Part 3: Text Input")

# TODO 5: Add a text_input for the user's name with a placeholder.
# If the name is not empty, show "Welcome, [name]!"


# TODO 6: Add a text_area for a bio (height=100).
# Display the bio length in characters below.


st.divider()

# ---------------------------------------------------------------------------
# Part 4: Numeric Input
# ---------------------------------------------------------------------------
st.header("Part 4: Numeric Input")

# TODO 7: Add a number_input for age (range 0-120, default 25).
# TODO 8: Add a slider for experience years (0-30, default 5).
# Display both values side by side using st.columns(2).


st.divider()

# ---------------------------------------------------------------------------
# Part 5: Date & Time
# ---------------------------------------------------------------------------
st.header("Part 5: Date & Time")

# TODO 9: Add a date_input for a birthday.
# TODO 10: Add a time_input for a meeting time.
# Display both values.


st.divider()

# ---------------------------------------------------------------------------
# Part 6: Combined Challenge
# ---------------------------------------------------------------------------
st.header("Part 6: Combined Challenge")

# TODO 11: Create a mini registration form that collects:
#   - Name (text_input)
#   - Email (text_input)
#   - Age (number_input)
#   - Department (selectbox)
#   - Skills (multiselect)
#   - Start date (date_input)
#
# When the user clicks a "Register" button, display a summary card
# with all the collected information.


# ---------------------------------------------------------------------------
# Footer
# ---------------------------------------------------------------------------
st.divider()
st.caption("Exercise 03 — Widget Mastery • Module 02 • Streamlit for Data Science")

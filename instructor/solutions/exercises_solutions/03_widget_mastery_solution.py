"""
Exercise 03 — Widget Mastery SOLUTION
=======================================
INSTRUCTOR USE ONLY — Do not share with students.

Reference implementation with all TODOs completed.
Run: streamlit run instructor/solutions/exercises_solutions/03_widget_mastery_solution.py
"""

import streamlit as st

st.set_page_config(
    page_title="Exercise 03 — Widget Mastery (SOLUTION)",
    page_icon="✅",
    layout="centered",
)

st.title("✅ Exercise 03 — Widget Mastery (Solution)")
st.markdown("Complete reference implementation for instructor use.")
st.divider()

# ============================================================================
# Part 1: Buttons & Toggles
# ============================================================================

st.header("Part 1: Buttons & Toggles")

# TODO 1: Button
if st.button("Say Hello!"):
    st.success("Hello, Streamlit!")

# Additional toggles
if st.toggle("Enable notifications"):
    st.info("Notifications enabled!")
    if st.button("Send Test Notification"):
        st.toast("🔔 Test notification sent!")

st.divider()

# ============================================================================
# Part 2: Selection Widgets
# ============================================================================

st.header("Part 2: Selection Widgets")

# TODO 2: Selectbox
language = st.selectbox(
    "Favorite Programming Language",
    ["Python", "JavaScript", "Rust", "Go", "TypeScript"],
)
st.write(f"You selected: **{language}**")

# TODO 3: Multiselect
skills = st.multiselect(
    "Your Skills",
    ["Python", "Pandas", "NumPy", "SQL", "Git", "Docker", "ML", "Deep Learning"],
    default=["Python", "Pandas"],
)
if skills:
    st.write("Your skills:")
    for skill in skills:
        st.write(f"- {skill}")

# TODO 4: Radio (horizontal)
color = st.radio(
    "Favorite Color",
    ["Red", "Green", "Blue", "Purple", "Orange"],
    horizontal=True,
)
st.write(f"Your favorite color: **{color}**")

st.divider()

# ============================================================================
# Part 3: Text Input
# ============================================================================

st.header("Part 3: Text Input")

# TODO 5: Text input with placeholder
name = st.text_input("Your Name", placeholder="Enter your name here...")
if name:
    st.write(f"Welcome, **{name}**! 👋")

# TODO 6: Text area for bio
bio = st.text_area("Your Bio", height=100, placeholder="Tell us about yourself...")
if bio:
    st.write(f"Bio length: **{len(bio)}** characters")

st.divider()

# ============================================================================
# Part 4: Numeric Input
# ============================================================================

st.header("Part 4: Numeric Input")

# TODO 7 & 8: Number input and slider
col1, col2 = st.columns(2)
with col1:
    age = st.number_input("Age", min_value=0, max_value=120, value=25)
with col2:
    experience = st.slider("Years of Experience", 0, 30, 5)

st.write(f"Age: **{age}** · Experience: **{experience} years**")

if experience > 0:
    years_per_age = experience / age if age > 0 else 0
    st.metric("Experience Ratio", f"{years_per_age:.2%}")

st.divider()

# ============================================================================
# Part 5: Date & Time
# ============================================================================

st.header("Part 5: Date & Time")

# TODO 9 & 10: Date and time inputs
col1, col2 = st.columns(2)
with col1:
    birthday = st.date_input("Your Birthday")
with col2:
    meeting_time = st.time_input("Meeting Time")

st.write(f"Birthday: **{birthday}**")
st.write(f"Meeting at: **{meeting_time}**")

st.divider()

# ============================================================================
# Part 6: Combined Challenge
# ============================================================================

st.header("Part 6: Combined Challenge — Registration Form")

# TODO 11: Registration form
reg_name = st.text_input("Name (Required)", key="reg_name")
reg_email = st.text_input("Email (Required)", key="reg_email")
reg_age = st.number_input("Age", min_value=16, max_value=100, value=22, key="reg_age")
reg_dept = st.selectbox(
    "Department",
    ["Engineering", "Marketing", "Sales", "Finance", "HR"],
    key="reg_dept",
)
reg_skills = st.multiselect(
    "Skills",
    ["Python", "SQL", "JavaScript", "Data Analysis", "Machine Learning"],
    key="reg_skills",
)
reg_start = st.date_input("Start Date", key="reg_start")

if st.button("Register", type="primary"):
    if not reg_name or not reg_email:
        st.error("Please fill in Name and Email.")
    elif "@" not in reg_email:
        st.error("Please enter a valid email address.")
    else:
        st.success("Registration successful! 🎉")
        st.divider()
        st.subheader("Registration Summary")
        col1, col2 = st.columns(2)
        with col1:
            st.write(f"**Name:** {reg_name}")
            st.write(f"**Email:** {reg_email}")
            st.write(f"**Age:** {reg_age}")
        with col2:
            st.write(f"**Department:** {reg_dept}")
            st.write(f"**Skills:** {', '.join(reg_skills) if reg_skills else 'None selected'}")
            st.write(f"**Start Date:** {reg_start}")

st.divider()
st.caption("Solution: Exercise 03 — Widget Mastery · Module 02")

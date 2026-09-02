"""
🖥️ Demo App 04 — Forms & Validation
======================================
A complete demo of Streamlit forms and input validation patterns.

Run this app:
    streamlit run apps/04_forms_demo.py

Related Materials:
- 📖 Reading: ../readings/03_streamlit_widgets_and_input.md
- 📓 Notebook: ../notebooks/04_interactive_ds_controls.ipynb
- ✏️ Exercise: ../exercises/04_dataset_filter_app.py
"""

import streamlit as st
import re
from datetime import date

# ---------------------------------------------------------------------------
# Page Config
# ---------------------------------------------------------------------------
st.set_page_config(
    page_title="04 — Forms & Validation Demo",
    page_icon="📝",
    layout="centered",
)

# ---------------------------------------------------------------------------
# Title
# ---------------------------------------------------------------------------
st.title("📝 Forms & Validation Demo")
st.markdown(
    "Demonstrates `st.form()` for batch submission and "
    "input validation patterns."
)

st.divider()

# ---------------------------------------------------------------------------
# 1. Basic Form
# ---------------------------------------------------------------------------
st.header("1. Basic Form")

with st.form("basic_form"):
    name = st.text_input("Full Name *", placeholder="e.g., Ali Khan")
    email = st.text_input("Email *", type="email", placeholder="user@example.com")
    age = st.number_input("Age *", min_value=1, max_value=150, value=25)
    submitted = st.form_submit_button("Submit")

if submitted:
    if not name or not email:
        st.error("Please fill in all required fields.")
    else:
        st.success(f"Submitted! Name: {name}, Email: {email}, Age: {age}")

st.divider()

# ---------------------------------------------------------------------------
# 2. Multi-Column Form
# ---------------------------------------------------------------------------
st.header("2. Multi-Column Form")

with st.form("column_form"):
    col1, col2 = st.columns(2)
    with col1:
        first_name = st.text_input("First Name *")
        department = st.selectbox("Department", ["CS", "Math", "Physics", "Biology"])
    with col2:
        last_name = st.text_input("Last Name *")
        gpa = st.slider("GPA", 0.0, 4.0, 3.0, step=0.1)

    start_date = st.date_input("Start Date", value=date(2026, 9, 1))
    notes = st.text_area("Additional Notes", placeholder="Optional...")

    col1, col2 = st.columns(2)
    with col1:
        cancel = st.form_submit_button("Cancel")
    with col2:
        register = st.form_submit_button("Register", type="primary")

if register:
    if not first_name or not last_name:
        st.error("First name and last name are required.")
    else:
        st.balloons()
        st.success(f"Welcome, {first_name} {last_name}!")
        col1, col2 = st.columns(2)
        with col1:
            st.write(f"**Department:** {department}")
            st.write(f"**GPA:** {gpa}")
        with col2:
            st.write(f"**Start Date:** {start_date}")
            if notes:
                st.write(f"**Notes:** {notes}")

if cancel:
    st.info("Registration cancelled.")

st.divider()

# ---------------------------------------------------------------------------
# 3. Validation Patterns
# ---------------------------------------------------------------------------
st.header("3. Validation Patterns")

# Pattern 1: Built-in validation
st.subheader("Pattern 1: Built-in Validation (≥ 1.62)")
st.markdown(
    "Use `type=\"email\"` or `type=\"url\"` for browser-native validation."
)

col1, col2 = st.columns(2)
with col1:
    email_val = st.text_input("Email (type=email)", type="email", key="val_email")
with col2:
    url_val = st.text_input("Website (type=url)", type="url", key="val_url")

st.divider()

# Pattern 2: Custom regex validation
st.subheader("Pattern 2: Custom Regex Validation")

password = st.text_input(
    "Password (min 8 chars, 1 digit, 1 uppercase)",
    type="password",
    key="val_password",
)

errors = []
if password:
    if len(password) < 8:
        errors.append("❌ Must be at least 8 characters")
    if not re.search(r"[A-Z]", password):
        errors.append("❌ Must contain at least one uppercase letter")
    if not re.search(r"\d", password):
        errors.append("❌ Must contain at least one digit")

if errors:
    for e in errors:
        st.error(e)
elif password:
    st.success("Password meets all requirements! ✅")

st.divider()

# Pattern 3: Form with validation
st.subheader("Pattern 3: Form-Level Validation")

with st.form("validated_form"):
    username = st.text_input("Username * (3-20 alphanumeric chars)")
    confirm_email = st.text_input("Confirm Email *", type="email")
    agree = st.checkbox("I agree to the terms and conditions *")
    validate_submit = st.form_submit_button("Create Account")

if validate_submit:
    form_errors = []
    if not username or len(username) < 3:
        form_errors.append("Username must be at least 3 characters")
    elif not username.isalnum():
        form_errors.append("Username must be alphanumeric")
    if not confirm_email:
        form_errors.append("Email is required")
    if not agree:
        form_errors.append("You must agree to the terms")

    if form_errors:
        for e in form_errors:
            st.error(e)
    else:
        st.success(f"Account created for **{username}**! 🎉")

st.divider()

# ---------------------------------------------------------------------------
# 4. Session State Persistence
# ---------------------------------------------------------------------------
st.header("4. Form Submission History")

if "submissions" not in st.session_state:
    st.session_state.submissions = []

with st.form("history_form"):
    item = st.text_input("Add an item to the list")
    if st.form_submit_button("Add"):
        if item:
            st.session_state.submissions.append(item)
            st.rerun()

if st.session_state.submissions:
    st.write(f"**Items ({len(st.session_state.submissions)}):**")
    for i, item in enumerate(st.session_state.submissions, 1):
        st.write(f"{i}. {item}")

    if st.button("Clear All"):
        st.session_state.submissions = []
        st.rerun()
else:
    st.info("No items yet. Add one using the form above.")

# ---------------------------------------------------------------------------
# Footer
# ---------------------------------------------------------------------------
st.divider()
st.caption(
    "Forms & Validation Demo • Module 02 • "
    "[Streamlit Forms](https://docs.streamlit.io/develop/api-reference/execution-flow/st.form)"
)

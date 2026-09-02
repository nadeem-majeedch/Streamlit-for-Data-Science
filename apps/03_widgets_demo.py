"""
🖥️ Demo App 03 — Widgets Showcase
===================================
A complete demo of every core Streamlit widget type.

Run this app:
    streamlit run apps/03_widgets_demo.py

Related Materials:
- 📖 Reading: ../readings/03_streamlit_widgets_and_input.md
- 📓 Notebook: ../notebooks/03_streamlit_widgets.ipynb
- ✏️ Exercise: ../exercises/03_widget_mastery.py
"""

import streamlit as st
from datetime import date, time

# ---------------------------------------------------------------------------
# Page Config
# ---------------------------------------------------------------------------
st.set_page_config(
    page_title="03 — Widgets Demo",
    page_icon="🎛️",
    layout="wide",
)

# ---------------------------------------------------------------------------
# Title
# ---------------------------------------------------------------------------
st.title("🎛️ Streamlit Widgets Showcase")
st.markdown(
    "A complete tour of every core Streamlit widget type.\n"
    "Each section demonstrates a different category of widgets."
)

st.divider()

# ---------------------------------------------------------------------------
# 1. Buttons & Toggles
# ---------------------------------------------------------------------------
st.header("1. Buttons & Toggles")

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("Button")
    if st.button("Click Me!", key="demo_button"):
        st.success("Button clicked! 🎉")
    st.caption("Returns True on the rerun after click.")

with col2:
    st.subheader("Toggle")
    dark_mode = st.toggle("Dark Mode", key="demo_toggle")
    if dark_mode:
        st.info("Dark mode is ON")
    else:
        st.write("Dark mode is OFF")
    st.caption("Persistent boolean state.")

with col3:
    st.subheader("Checkbox")
    agree = st.checkbox("I agree to terms", key="demo_checkbox")
    st.write(f"Agreed: {agree}")
    st.caption("Another boolean state widget.")

st.divider()

# ---------------------------------------------------------------------------
# 2. Selection Widgets
# ---------------------------------------------------------------------------
st.header("2. Selection Widgets")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.subheader("Selectbox")
    color = st.selectbox(
        "Pick a color",
        ["Red", "Green", "Blue", "Yellow", "Purple"],
        key="demo_selectbox",
    )
    st.write(f"Selected: **{color}**")

with col2:
    st.subheader("Multiselect")
    skills = st.multiselect(
        "Your skills",
        ["Python", "SQL", "R", "Julia", "Scala"],
        default=["Python"],
        key="demo_multiselect",
    )
    st.write(f"Skills: {skills}")

with col3:
    st.subheader("Radio")
    option = st.radio(
        "Favorite framework",
        ["Streamlit", "Dash", "Flask", "Gradio"],
        horizontal=True,
        key="demo_radio",
    )
    st.write(f"Choice: **{option}**")

with col4:
    st.subheader("Select Slider")
    size = st.select_slider(
        "Shirt size",
        options=["XS", "S", "M", "L", "XL", "XXL"],
        key="demo_select_slider",
    )
    st.write(f"Size: **{size}**")

st.divider()

# ---------------------------------------------------------------------------
# 3. Text Input
# ---------------------------------------------------------------------------
st.header("3. Text Input")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Text Input")
    name = st.text_input(
        "Your name",
        placeholder="Enter your name here",
        key="demo_text_input",
    )
    if name:
        st.write(f"Hello, **{name}**!")

with col2:
    st.subheader("Text Area")
    notes = st.text_area(
        "Notes",
        placeholder="Write your notes here...",
        height=120,
        key="demo_text_area",
    )
    if notes:
        st.write(f"Character count: **{len(notes)}**")

st.divider()

# ---------------------------------------------------------------------------
# 4. Number & Slider
# ---------------------------------------------------------------------------
st.header("4. Number & Slider")

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("Number Input")
    age = st.number_input(
        "Age",
        min_value=0,
        max_value=120,
        value=25,
        step=1,
        key="demo_number_input",
    )
    st.write(f"Age: **{age}**")

with col2:
    st.subheader("Slider")
    score = st.slider(
        "Score",
        min_value=0,
        max_value=100,
        value=75,
        key="demo_slider",
    )
    st.write(f"Score: **{score}**")

with col3:
    st.subheader("Range Slider")
    budget = st.slider(
        "Budget range",
        min_value=0,
        max_value=10000,
        value=(1000, 5000),
        key="demo_range_slider",
    )
    st.write(f"Budget: **${budget[0]:,} — ${budget[1]:,}**")

st.divider()

# ---------------------------------------------------------------------------
# 5. Date & Time
# ---------------------------------------------------------------------------
st.header("5. Date & Time")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Date Input")
    dob = st.date_input(
        "Date of birth",
        value=date(2000, 1, 1),
        key="demo_date_input",
    )
    st.write(f"Selected: **{dob}**")

with col2:
    st.subheader("Time Input")
    meeting = st.time_input(
        "Meeting time",
        value=time(9, 0),
        key="demo_time_input",
    )
    st.write(f"Time: **{meeting}**")

st.divider()

# ---------------------------------------------------------------------------
# 6. Color Picker
# ---------------------------------------------------------------------------
st.header("6. Color Picker")

color = st.color_picker("Pick a brand color", "#FF5733", key="demo_color")
st.markdown(
    f"<div style='background:{color};height:60px;border-radius:8px;"
    f"display:flex;align-items:center;justify-content:center;"
    f"color:white;font-weight:bold;font-size:1.2em;'>{color}</div>",
    unsafe_allow_html=True,
)

st.divider()

# ---------------------------------------------------------------------------
# 7. Widget Keys & Session State
# ---------------------------------------------------------------------------
st.header("7. Keys & Session State Demo")

st.markdown(
    "Every widget with a `key` parameter stores its value in `st.session_state`.\n"
    "Try typing in the input below, then check the session state display."
)

st.text_input("Type something", key="session_demo_input")

st.write("**Session State:**")
st.json(
    {k: v for k, v in st.session_state.items() if not k.startswith("_")}
)

# ---------------------------------------------------------------------------
# Footer
# ---------------------------------------------------------------------------
st.divider()
st.caption(
    "Widgets Demo • Module 02 • "
    "[Streamlit Docs](https://docs.streamlit.io/develop/api-reference/widgets)"
)

"""
🖥️ Demo App 05 — Layouts Showcase
====================================
A complete demo of every Streamlit layout element.

Run this app:
    streamlit run apps/05_layouts_demo.py

Related Materials:
- 📖 Reading: ../readings/05_layouts_and_containers.md
- 📓 Notebook: ../notebooks/05_layouts_and_containers.ipynb
- ✏️ Exercise: ../exercises/05_layout_basics.py
"""

import streamlit as st
import pandas as pd
import numpy as np

# ---------------------------------------------------------------------------
# Page Config
# ---------------------------------------------------------------------------
st.set_page_config(
    page_title="05 — Layouts Demo",
    page_icon="📐",
    layout="wide",
)

# ---------------------------------------------------------------------------
# Sidebar
# ---------------------------------------------------------------------------
st.sidebar.header("🎛️ Controls")
st.sidebar.write("The sidebar is your **control panel**.")
dataset = st.sidebar.selectbox(
    "Dataset", ["Sales", "Inventory", "Customers"], key="demo_dataset"
)
point_count = st.sidebar.slider("Data points", 10, 100, 30, key="demo_points")
show_raw = st.sidebar.checkbox("Show raw data", key="demo_raw")

# ---------------------------------------------------------------------------
# Title
# ---------------------------------------------------------------------------
st.title("📐 Streamlit Layouts Showcase")
st.markdown(
    "A complete tour of every layout element in Streamlit.\n"
    "Each section demonstrates a different layout tool."
)

st.divider()

# ---------------------------------------------------------------------------
# 1. Sidebar (already above)
# ---------------------------------------------------------------------------
st.header("1. Sidebar")
st.markdown(
    "The sidebar on the left contains controls that affect the main area.\n"
    "**Current settings:** Dataset = `{}`, Points = `{}`, Raw data = `{}`".format(
        dataset, point_count, show_raw
    )
)

st.divider()

# ---------------------------------------------------------------------------
# 2. Columns — Equal
# ---------------------------------------------------------------------------
st.header("2. Columns — Equal Width")

c1, c2, c3, c4 = st.columns(4)
with c1:
    st.metric("Revenue", "$45,231", "+5.2%", icon="💰")
with c2:
    st.metric("Users", "1,204", "+12.1%", icon="👥")
with c3:
    st.metric("Orders", "347", "-3.2%", icon="📦")
with c4:
    st.metric("Conversion", "3.2%", "+0.4%", icon="🎯")

st.divider()

# ---------------------------------------------------------------------------
# 3. Columns — Unequal
# ---------------------------------------------------------------------------
st.header("3. Columns — Unequal (70/30)")

np.random.seed(42)
chart_df = pd.DataFrame(
    np.random.randn(point_count, 3).cumsum(),
    columns=["Series A", "Series B", "Series C"],
)

main_area, side_area = st.columns([0.7, 0.3], border=True)
with main_area:
    st.subheader("Chart")
    st.line_chart(chart_df)
with side_area:
    st.subheader("Summary")
    st.write(f"**Points:** {point_count}")
    st.write(f"**Series:** {len(chart_df.columns)}")
    st.write(f"**Last values:**")
    for col in chart_df.columns:
        st.write(f"- {col}: {chart_df[col].iloc[-1]:.2f}")

st.divider()

# ---------------------------------------------------------------------------
# 4. Columns — Gap & Alignment
# ---------------------------------------------------------------------------
st.header("4. Column Gap & Vertical Alignment")

st.subheader("Vertical Alignment: center")
left, center, right = st.columns(3, vertical_alignment="center")
left.button("Short", key="align_left")
center.markdown("This is a\nmuch longer\ntext block\nthat spans lines")
right.checkbox("Check me", key="align_right")

st.divider()

# ---------------------------------------------------------------------------
# 5. Tabs
# ---------------------------------------------------------------------------
st.header("5. Tabs")

tab1, tab2, tab3 = st.tabs(["📊 Bar Chart", "📈 Line Chart", "📋 Data"])

with tab1:
    st.bar_chart(chart_df)

with tab2:
    st.line_chart(chart_df)

with tab3:
    st.dataframe(chart_df.round(2), use_container_width=True, hide_index=True)

st.divider()

# ---------------------------------------------------------------------------
# 6. Lazy Tabs
# ---------------------------------------------------------------------------
st.header("6. Lazy Tab Execution")

tab_fast, tab_slow = st.tabs(["⚡ Quick View", "🔬 Deep Analysis"])

with tab_fast:
    st.write("This always runs — lightweight content.")
    st.write(f"Data shape: {chart_df.shape}")

with tab_slow:
    if tab_slow.open:
        st.write("Expensive analysis only runs when tab is selected:")
        corr = chart_df.corr()
        st.dataframe(corr.style.background_gradient(cmap="coolwarm"))
    else:
        st.info("Switch to this tab to see the analysis.")

st.divider()

# ---------------------------------------------------------------------------
# 7. Expander
# ---------------------------------------------------------------------------
st.header("7. Expander — Progressive Disclosure")

st.metric("Total Points", f"{point_count * 3}")

with st.expander("📊 Data Distribution"):
    st.bar_chart(chart_df.abs().mean())

with st.expander("📈 Correlation Matrix"):
    st.dataframe(chart_df.corr().round(3))

with st.expander("📋 Full Data", expanded=False):
    st.dataframe(chart_df.round(2), use_container_width=True)

st.divider()

# ---------------------------------------------------------------------------
# 8. Container & Empty
# ---------------------------------------------------------------------------
st.header("8. Container & Empty")

output = st.container()
output.write("📦 This is inside a container — written first in code, appears first here.")
output.write("📦 Containers let you write content in any order.")

placeholder = st.empty()
placeholder.info("🔄 This is an empty() placeholder — it can be replaced.")
placeholder.metric("Now it shows a metric!", "42", "+7")

st.divider()

# ---------------------------------------------------------------------------
# 9. Popover
# ---------------------------------------------------------------------------
st.header("9. Popover — Floating Settings")

with st.popover("⚙️ Display Settings", icon="⚙️"):
    pop_chart = st.selectbox("Chart type", ["Line", "Bar", "Area"], key="pop_chart_type")
    pop_grid = st.checkbox("Show grid", key="pop_grid")
    pop_color = st.color_picker("Chart color", "#FF4B4B", key="pop_color")

st.write(f"**Settings:** Chart = `{pop_chart}`, Grid = `{pop_grid}`")

st.divider()

# ---------------------------------------------------------------------------
# 10. Dialog (Modal)
# ---------------------------------------------------------------------------
st.header("10. Dialog — Modal Window")

@st.dialog("💬 Feedback Form")
def feedback_dialog():
    name = st.text_input("Your name")
    rating = st.slider("Rating", 1, 5, 3)
    comment = st.text_area("Comments")
    if st.button("Submit Feedback"):
        if name:
            st.success(f"Thank you, {name}! Rating: {rating}/5")
            st.rerun()
        else:
            st.error("Please enter your name.")

if st.button("💬 Give Feedback"):
    feedback_dialog()

st.divider()

# ---------------------------------------------------------------------------
# 11. Layout Hierarchy
# ---------------------------------------------------------------------------
st.header("11. Layout Hierarchy Diagram")

st.code(
    """
Page (st.set_page_config)
├── Sidebar (st.sidebar)
│   ├── Controls
│   └── Filters
└── Main Area
    ├── Tabs (st.tabs)
    │   ├── Tab 1 → Columns → Content
    │   └── Tab 2 → Expanders → Details
    ├── Popovers (floating settings)
    └── Dialogs (modal workflows)
""",
    language="text",
)

# ---------------------------------------------------------------------------
# Footer
# ---------------------------------------------------------------------------
st.divider()
st.caption(
    "Layouts Demo • Module 03 • "
    "[Streamlit Docs](https://docs.streamlit.io/develop/api-reference/layout)"
)

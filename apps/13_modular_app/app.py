"""
Modular Streamlit App — Entry Point
====================================

Module 09 · Advanced

Demonstrates proper application architecture with:
- Separated concerns (UI, data, business logic)
- Configuration module
- Reusable components
- Multipage navigation

Run: streamlit run apps/13_modular_app/app.py
"""

import streamlit as st
import sys
import os

# Add app directory to path for imports
sys.path.insert(0, os.path.dirname(__file__))

from config import APP_TITLE, APP_ICON
from components import render_header, render_footer

# Page config
st.set_page_config(
    page_title=APP_TITLE,
    page_icon=APP_ICON,
    layout="wide"
)

# --- Shared Elements (persist across pages) ---
render_header()

# Sidebar with shared widgets
st.sidebar.title(APP_TITLE)
st.sidebar.markdown("---")

# User preferences (stored in session state)
if "theme" not in st.session_state:
    st.session_state.theme = "light"
if "show_tips" not in st.session_state:
    st.session_state.show_tips = True

st.session_state.theme = st.sidebar.selectbox(
    "Theme",
    ["light", "dark", "blue"],
    index=["light", "dark", "blue"].index(st.session_state.theme)
)

st.session_state.show_tips = st.sidebar.toggle(
    "Show tips",
    st.session_state.show_tips
)

st.sidebar.markdown("---")

# --- Navigation ---
try:
    from pages import home, explore, analysis, settings

    pg = st.navigation(
        {
            "Main": [
                st.Page(home, title="Home", icon="🏠"),
                st.Page(explore, title="Explore", icon="📊"),
            ],
            "Analysis": [
                st.Page(analysis, title="Analysis", icon="📈"),
            ],
            "Settings": [
                st.Page(settings, title="Settings", icon="⚙️"),
            ]
        }
    )
    pg.run()
except Exception as e:
    # Fallback if pages module not available
    st.info(f"""
    **Welcome to {APP_TITLE}!**
    
    This demo shows proper application architecture.
    
    The modular structure includes:
    - `config.py` — Configuration settings
    - `components.py` — Reusable UI components
    - `data_loader.py` — Data loading functions
    - `pages/` — Individual page modules
    
    **Error loading pages:** {e}
    """)

# Footer
render_footer()

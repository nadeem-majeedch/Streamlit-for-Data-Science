"""
Settings Page
=============

App configuration and preferences.
"""

import streamlit as st
from components import section_header, info_box
from config import (
    APP_TITLE, CACHE_TTL, MAX_ROWS, 
    CATEGORIES, REGIONS, COLORS
)


def render():
    """Render the settings page."""
    
    section_header(
        "⚙️ Settings",
        "Configure app preferences and view current configuration"
    )
    
    # App info
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📱 App Information")
        st.write(f"**Title:** {APP_TITLE}")
        st.write(f"**Cache TTL:** {CACHE_TTL} seconds")
        st.write(f"**Max Rows:** {MAX_ROWS:,}")
    
    with col2:
        st.subheader("🎨 Theme Colors")
        for name, color in COLORS.items():
            st.color_picker(name, value=color, key=f"color_{name}", disabled=True)
    
    st.divider()
    
    # Data configuration
    st.subheader("📊 Data Configuration")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("**Categories:**")
        for cat in CATEGORIES:
            st.write(f"  - {cat}")
    
    with col2:
        st.write("**Regions:**")
        for reg in REGIONS:
            st.write(f"  - {reg}")
    
    st.divider()
    
    # Session state viewer
    st.subheader("🔍 Session State")
    
    if st.button("Show Session State"):
        # Filter out internal keys
        state = {k: v for k, v in st.session_state.items() if not k.startswith("_")}
        st.json(state)
    
    # Cache management
    st.subheader("🗑️ Cache Management")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("Clear Data Cache"):
            st.cache_data.clear()
            st.success("Data cache cleared!")
    
    with col2:
        if st.button("Clear Resource Cache"):
            st.cache_resource.clear()
            st.success("Resource cache cleared!")
    
    with col3:
        if st.button("Reload App"):
            st.rerun()
    
    st.divider()
    
    # Architecture info
    info_box(
        "Architecture Notes",
        """
        This demo app demonstrates proper Streamlit architecture:
        
        - **config.py** — Centralized configuration
        - **components.py** — Reusable UI components
        - **data_loader.py** — Separated data logic
        - **pages/** — Modular page structure
        
        Each module has a single responsibility and can be tested independently.
        """,
        type="info"
    )


# For multipage navigation
if __name__ == "__main__":
    render()

"""
Reusable UI Components
======================

Build once, use everywhere.
These components ensure consistency across all pages.
"""

import streamlit as st
from config import APP_TITLE, COLORS


def render_header():
    """Render common header elements."""
    # Note: st.set_page_config is called in app.py before this
    pass


def render_footer():
    """Render common footer elements."""
    st.divider()
    st.caption(f"""
    💡 **{APP_TITLE}** | Built with Streamlit | Module 09 Demo
    """)


def metric_card(label, value, delta=None, delta_color="normal"):
    """
    Render a consistent metric card.
    
    Args:
        label: Metric label
        value: Metric value
        delta: Optional change indicator
        delta_color: "normal" (green=positive) or "inverse" (red=positive)
    """
    st.metric(
        label=label,
        value=value,
        delta=delta,
        delta_color=delta_color
    )


def metric_row(metrics: dict, delta_values: dict = None):
    """
    Render a row of metrics.
    
    Args:
        metrics: Dict of {label: value}
        delta_values: Optional dict of {label: delta_value}
    """
    cols = st.columns(len(metrics))
    for col, (label, value) in zip(cols, metrics.items()):
        with col:
            delta = delta_values.get(label) if delta_values else None
            metric_card(label, value, delta)


def data_preview(df, max_rows=5, show_shape=True):
    """
    Show data preview with consistent formatting.
    
    Args:
        df: Pandas DataFrame
        max_rows: Maximum rows to display
        show_shape: Whether to show shape info
    """
    if show_shape:
        st.info(f"📊 {df.shape[0]:,} rows × {df.shape[1]} columns")
    st.dataframe(df.head(max_rows), use_container_width=True)


def section_header(title, description=None, divider=True):
    """
    Render section header with optional description.
    
    Args:
        title: Section title
        description: Optional description text
        divider: Whether to add divider before
    """
    if divider:
        st.divider()
    st.subheader(title)
    if description:
        st.caption(description)


def status_badge(status):
    """
    Render status with appropriate styling.
    
    Args:
        status: "success", "warning", "error", or "info"
    """
    icons = {
        "success": "✅",
        "warning": "⚠️",
        "error": "❌",
        "info": "ℹ️"
    }
    colors = {
        "success": "green",
        "warning": "orange",
        "error": "red",
        "info": "blue"
    }
    icon = icons.get(status, "ℹ️")
    color = colors.get(status, "blue")
    st.markdown(f":{color}[{icon} {status.title()}]")


def info_box(title, content, type="info"):
    """
    Render an info box with title and content.
    
    Args:
        title: Box title
        content: Box content
        type: "info", "success", "warning", "error"
    """
    if type == "info":
        st.info(f"**{title}**\n\n{content}")
    elif type == "success":
        st.success(f"**{title}**\n\n{content}")
    elif type == "warning":
        st.warning(f"**{title}**\n\n{content}")
    elif type == "error":
        st.error(f"**{title}**\n\n{content}")


def sidebar_select(label, options, key=None, help_text=None):
    """
    Consistent sidebar selectbox.
    
    Args:
        label: Select label
        options: List of options
        key: Widget key
        help_text: Optional help text
    """
    return st.sidebar.selectbox(
        label,
        options,
        key=key,
        help=help_text
    )


def sidebar_multiselect(label, options, default=None, key=None):
    """
    Consistent sidebar multiselect.
    
    Args:
        label: Select label
        options: List of options
        default: Default selected options
        key: Widget key
    """
    return st.sidebar.multiselect(
        label,
        options,
        default=default or [],
        key=key
    )


def sidebar_slider(label, min_val, max_val, default, step=None, key=None):
    """
    Consistent sidebar slider.
    
    Args:
        label: Slider label
        min_val: Minimum value
        max_val: Maximum value
        default: Default value
        step: Step size
        key: Widget key
    """
    return st.sidebar.slider(
        label,
        min_val,
        max_val,
        default,
        step=step,
        key=key
    )

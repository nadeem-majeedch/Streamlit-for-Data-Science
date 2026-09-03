"""
Exercise 11: Session State Management Workshop
===============================================

Module 07 · Intermediate

Build stateful Streamlit applications using session state and the rerun model.

Learning Objectives:
- Initialize and manage session state properly
- Build multi-step workflows
- Implement undo/redo functionality
- Use callbacks for efficient state updates

Instructions:
Complete each section by filling in the TODOs.
Run with: streamlit run exercises/11_state_management_workshop.py
"""

import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="State Management Workshop", page_icon="🧠", layout="wide")
st.title("🧠 Exercise 11: Session State Management Workshop")
st.markdown("*Module 07 · Intermediate — Build stateful Streamlit applications*")

st.divider()

# ============================================================================
# CHALLENGE 1: Counter with History
# ============================================================================
st.header("🎯 Challenge 1: Counter with History")
st.write("Build a counter that tracks its history of changes.")

# TODO: Initialize session state for counter and history
# if "counter" not in st.session_state:
#     st.session_state.counter = 0
# if "history" not in st.session_state:
#     st.session_state.history = []

# TODO: Create three columns with Increment, Decrement, and Reset buttons
# When clicked, update the counter AND append to history
# Each history entry should show: action, old_value, new_value

# TODO: Display the current counter value as a metric
# TODO: Display the last 10 history entries
# TODO: Add a "Clear History" button

st.divider()

# ============================================================================
# CHALLENGE 2: Multi-Step Form Wizard
# ============================================================================
st.header("🎯 Challenge 2: Multi-Step Registration Form")
st.write("Build a 3-step registration wizard that collects user information.")

# TODO: Initialize session state for:
# - current_step (1, 2, or 3)
# - form_data dict with keys: name, email, age, interests, newsletter

# Step 1: Personal Info
st.subheader("Step 1: Personal Information")
# TODO: Create text inputs for name and email
# TODO: Store values in session_state.form_data
# TODO: Add "Next" button (only show if name and email are filled)

# Step 2: Demographics
st.subheader("Step 2: Demographics")
# TODO: Create number_input for age (18-100)
# TODO: Create multiselect for interests
# TODO: Store values in session_state.form_data
# TODO: Add "Back" and "Next" buttons

# Step 3: Preferences
st.subheader("Step 3: Preferences")
# TODO: Create checkbox for newsletter subscription
# TODO: Add "Back" and "Submit" buttons
# TODO: On submit, save to session_state.submissions list
# TODO: Show success message and reset form

# TODO: Add a progress bar showing current step

st.divider()

# ============================================================================
# CHALLENGE 3: Undo/Redo Text Editor
# ============================================================================
st.header("🎯 Challenge 3: Simple Text Editor with Undo/Redo")
st.write("Build a text editor that supports undo and redo operations.")

# TODO: Initialize session state for:
# - text_content (string)
# - undo_stack (list)
# - redo_stack (list)

# TODO: Create a text_area for editing
# The text_area should show the current text_content

# TODO: When user clicks "Save Snapshot":
# - Push current text to undo_stack
# - Clear redo_stack
# - Show success message

# TODO: Create a "Save Snapshot" button

st.subheader("History Controls")
col1, col2, col3 = st.columns(3)

with col1:
    # TODO: Implement "Undo" button
    # - Pop from undo_stack
    # - Push current text to redo_stack
    # - Update text_content
    # - Show warning if undo_stack is empty
    pass

with col2:
    # TODO: Implement "Redo" button
    # - Pop from redo_stack
    # - Push current text to undo_stack
    # - Update text_content
    # - Show warning if redo_stack is empty
    pass

with col3:
    # TODO: Implement "Clear All" button
    # - Reset text_content to empty
    # - Clear both stacks
    pass

# TODO: Display current history status
# - Show number of undo steps available
# - Show number of redo steps available

st.divider()

# ============================================================================
# CHALLENGE 4: Shopping Cart
# ============================================================================
st.header("🎯 Challenge 4: Shopping Cart")
st.write("Build a shopping cart with add, remove, and total calculation.")

# TODO: Initialize session state for cart (list of dicts)
# Each item: {"name": str, "price": float, "quantity": int}

# Available products
products = {
    "Apple": 1.50,
    "Banana": 0.75,
    "Orange": 1.25,
    "Grape": 2.50,
    "Mango": 3.00
}

col1, col2 = st.columns([1, 2])

with col1:
    st.subheader("Add Items")
    # TODO: Create selectbox for product
    # TODO: Create number_input for quantity (1-10)
    # TODO: Create "Add to Cart" button
    # TODO: Check if item already in cart, update quantity if so

with col2:
    st.subheader("Your Cart")
    # TODO: Display cart items in a table
    # TODO: Show individual item totals
    # TODO: Add "Remove" button for each item
    # TODO: Calculate and display grand total
    # TODO: Add "Clear Cart" button

st.divider()

# ============================================================================
# CHALLENGE 5: Data Filter State
# ============================================================================
st.header("🎯 Challenge 5: Persistent Data Filters")
st.write("Build filters that persist across interactions.")

# Generate sample data
@st.cache_data
def get_sample_data():
    import numpy as np
    np.random.seed(42)
    n = 100
    return pd.DataFrame({
        "category": np.random.choice(["A", "B", "C", "D"], n),
        "value1": np.random.randn(n) * 10 + 50,
        "value2": np.random.randn(n) * 5 + 20,
        "date": pd.date_range("2024-01-01", periods=n)
    })

df = get_sample_data()

# TODO: Initialize filter state in session_state
# - selected_categories (multiselect)
# - value1_range (slider)
# - show_raw_data (checkbox)

# TODO: Create filter widgets in sidebar
# Each widget should store its value in session_state

# TODO: Apply filters to dataframe
# filtered_df = df[...]
# Use conditions based on session_state values

# TODO: Display metrics showing:
# - Total rows
# - Filtered rows
# - Percentage retained

# TODO: Display filtered data in st.dataframe
# TODO: Add option to download filtered data as CSV

st.divider()

# ============================================================================
# CHALLENGE 6: Preference Persistence
# ============================================================================
st.header("🎯 Challenge 6: User Preference Dashboard")
st.write("Build a dashboard with persistent user preferences.")

# TODO: Initialize default preferences in session_state
# defaults = {
#     "theme": "light",
#     "sidebar_collapsed": False,
#     "default_chart": "bar",
#     "items_per_page": 10,
#     "show_tips": True
# }

# TODO: Create sidebar settings panel
# Each setting should read from and write to session_state.prefs

# TODO: Create "Reset to Defaults" button

# TODO: Main content area that uses preferences to customize display
# - Use theme preference to set page styling
# - Use items_per_page to limit displayed content
# - Show/hide tips based on show_tips preference

# TODO: Display current preferences in an expander

# TODO: Add a "Export Preferences" button
# (Show JSON of current preferences)

st.divider()

# ============================================================================
# BONUS CHALLENGE: State Inspector
# ============================================================================
st.header("🏆 Bonus: Session State Inspector")
st.write("Build a tool that shows the current state of all session_state keys.")

# TODO: Create an expander that shows all session_state keys and their values
# - Show key name
# - Show value type
# - Show value (truncated if too long)
# - Show size for lists/dicts

# TODO: Add search functionality
# - text_input to filter keys by name
# - Show only matching keys

# TODO: Add "Clear All State" button with confirmation
# - Show warning before clearing
# - require confirmation checkbox

st.divider()

# ============================================================================
# COMPLETION
# ============================================================================
st.success("🎉 Workshop Complete!")
st.markdown("""
**What you practiced:**
- ✅ Session state initialization and persistence
- ✅ Multi-step workflow management
- ✅ Undo/redo pattern implementation
- ✅ Shopping cart state management
- ✅ Persistent filter state
- ✅ User preference storage

**Next steps:**
- Try Challenge 6: Build a complete stateful application
- Read: [Session State & Execution](../readings/11_session_state_and_execution.md)
- Notebook: [Session State Execution Model](../notebooks/11_session_state_execution_model.ipynb)
""")

# Run check
if __name__ == "__main__":
    st.write("✅ Exercise file is valid and ready to run!")

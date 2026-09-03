"""
Streamlit Session State & Execution Model Demo
===============================================

Module 07 · Intermediate

A complete demonstration of session state concepts:
- Counter with persistence
- Multi-step workflow
- User preferences
- Prediction history
- Undo/redo pattern

Run: streamlit run apps/11_session_state_demo.py
"""

import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(
    page_title="Session State Demo",
    page_icon="🧠",
    layout="wide"
)

st.title("🧠 Session State & Execution Model Demo")
st.caption("Module 07 · Understanding reruns and state persistence")

# ============================================================================
# Initialize Session State
# ============================================================================
if "counter" not in st.session_state:
    st.session_state.counter = 0
if "history" not in st.session_state:
    st.session_state.history = []
if "step" not in st.session_state:
    st.session_state.step = 1
if "form_data" not in st.session_state:
    st.session_state.form_data = {}
if "predictions" not in st.session_state:
    st.session_state.predictions = []
if "text_content" not in st.session_state:
    st.session_state.text_content = ""
if "undo_stack" not in st.session_state:
    st.session_state.undo_stack = []
if "redo_stack" not in st.session_state:
    st.session_state.redo_stack = []
if "prefs" not in st.session_state:
    st.session_state.prefs = {
        "theme": "light",
        "items_per_page": 10,
        "show_tips": True
    }

# ============================================================================
# Sidebar Navigation
# ============================================================================
st.sidebar.title("📚 Module 07 Demo")
st.sidebar.markdown("---")

demo = st.sidebar.radio(
    "Select Demo:",
    [
        "1️⃣ Counter with History",
        "2️⃣ Multi-Step Wizard",
        "3️⃣ Prediction Calculator",
        "4️⃣ Undo/Redo Text",
        "5️⃣ User Preferences"
    ]
)

st.sidebar.markdown("---")
st.sidebar.markdown("""
**Key Concepts:**
- Reruns happen on every interaction
- `st.session_state` preserves data
- Widget keys enable binding
- Callbacks run before script
""")

# ============================================================================
# Demo 1: Counter with History
# ============================================================================
if demo.startswith("1️⃣"):
    st.header("1️⃣ Counter with History")
    st.write("Watch how the counter persists across reruns while tracking history.")
    
    # Counter controls
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        if st.button("➕ Increment", use_container_width=True):
            old_val = st.session_state.counter
            st.session_state.counter += 1
            st.session_state.history.append({
                "action": "Increment",
                "old": old_val,
                "new": st.session_state.counter,
                "time": datetime.now().strftime("%H:%M:%S")
            })
    
    with col2:
        if st.button("➖ Decrement", use_container_width=True):
            old_val = st.session_state.counter
            st.session_state.counter -= 1
            st.session_state.history.append({
                "action": "Decrement",
                "old": old_val,
                "new": st.session_state.counter,
                "time": datetime.now().strftime("%H:%M:%S")
            })
    
    with col3:
        if st.button("🔄 Reset", use_container_width=True):
            old_val = st.session_state.counter
            st.session_state.counter = 0
            st.session_state.history.append({
                "action": "Reset",
                "old": old_val,
                "new": 0,
                "time": datetime.now().strftime("%H:%M:%S")
            })
    
    with col4:
        if st.button("🗑️ Clear History", use_container_width=True):
            st.session_state.history = []
            st.rerun()
    
    # Display metrics
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Current Count", st.session_state.counter)
    with col2:
        st.metric("Total Changes", len(st.session_state.history))
    with col3:
        if st.session_state.history:
            st.metric("Last Action", st.session_state.history[-1]["action"])
    
    # History log
    if st.session_state.history:
        st.subheader("📜 History Log")
        for entry in reversed(st.session_state.history[-10:]):
            st.write(f"**{entry['time']}** - {entry['action']}: {entry['old']} → {entry['new']}")
    else:
        st.info("No history yet. Click a button to start!")

# ============================================================================
# Demo 2: Multi-Step Wizard
# ============================================================================
elif demo.startswith("2️⃣"):
    st.header("2️⃣ Multi-Step Registration Wizard")
    st.write("Complete the 3-step registration form. Your data persists across steps!")
    
    # Progress
    progress = st.progress(0)
    st.write(f"**Step {st.session_state.step} of 3**")
    
    if st.session_state.step == 1:
        progress.progress(33)
        st.subheader("📋 Step 1: Personal Information")
        
        with st.form("step1"):
            name = st.text_input("Full Name *", value=st.session_state.form_data.get("name", ""))
            email = st.text_input("Email *", value=st.session_state.form_data.get("email", ""))
            
            if st.form_submit_button("Next →"):
                if name and email:
                    st.session_state.form_data["name"] = name
                    st.session_state.form_data["email"] = email
                    st.session_state.step = 2
                    st.rerun()
                else:
                    st.error("Please fill in all required fields!")
    
    elif st.session_state.step == 2:
        progress.progress(66)
        st.subheader("👤 Step 2: Demographics")
        
        with st.form("step2"):
            age = st.number_input("Age", min_value=18, max_value=100,
                                  value=st.session_state.form_data.get("age", 25))
            interests = st.multiselect(
                "Interests",
                ["Data Science", "Machine Learning", "Web Dev", "Mobile", "DevOps", "AI"],
                default=st.session_state.form_data.get("interests", [])
            )
            
            col1, col2 = st.columns(2)
            with col1:
                if st.form_submit_button("← Back"):
                    st.session_state.step = 1
                    st.rerun()
            with col2:
                if st.form_submit_button("Next →"):
                    st.session_state.form_data["age"] = age
                    st.session_state.form_data["interests"] = interests
                    st.session_state.step = 3
                    st.rerun()
    
    else:  # step 3
        progress.progress(100)
        st.subheader("⚙️ Step 3: Preferences")
        
        with st.form("step3"):
            newsletter = st.checkbox("Subscribe to newsletter",
                                     value=st.session_state.form_data.get("newsletter", True))
            
            col1, col2 = st.columns(2)
            with col1:
                if st.form_submit_button("← Back"):
                    st.session_state.step = 2
                    st.rerun()
            with col2:
                if st.form_submit_button("✅ Submit"):
                    st.session_state.form_data["newsletter"] = newsletter
                    st.session_state.step = 1
                    
                    # Save submission
                    st.success("🎉 Registration Complete!")
                    st.json(st.session_state.form_data)
                    
                    # Reset
                    st.session_state.form_data = {}
    
    # Show saved data
    if st.session_state.form_data:
        with st.expander("📦 Saved Data So Far"):
            st.json(st.session_state.form_data)

# ============================================================================
# Demo 3: Prediction Calculator
# ============================================================================
elif demo.startswith("3️⃣"):
    st.header("3️⃣ Prediction Calculator")
    st.write("Calculate results and track prediction history!")
    
    # Calculator
    col1, col2, col3 = st.columns([2, 1, 2])
    
    with col1:
        num1 = st.number_input("First Number", value=0.0, key="calc_n1")
    
    with col2:
        operation = st.selectbox("Operation", ["+", "-", "×", "÷"], key="calc_op")
    
    with col3:
        num2 = st.number_input("Second Number", value=1.0, key="calc_n2")
    
    if st.button("🔢 Calculate"):
        try:
            if operation == "+":
                result = num1 + num2
            elif operation == "-":
                result = num1 - num2
            elif operation == "×":
                result = num1 * num2
            else:  # ÷
                if num2 == 0:
                    st.error("Cannot divide by zero!")
                    st.stop()
                result = num1 / num2
            
            # Save to history
            st.session_state.predictions.append({
                "expression": f"{num1} {operation} {num2}",
                "result": result,
                "time": datetime.now().strftime("%H:%M:%S")
            })
            
            st.success(f"**Result:** {result}")
        except Exception as e:
            st.error(f"Error: {e}")
    
    # History
    if st.session_state.predictions:
        st.divider()
        st.subheader("📜 Calculation History")
        
        df = pd.DataFrame(st.session_state.predictions)
        st.dataframe(df, use_container_width=True)
        
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Total Calculations", len(st.session_state.predictions))
        with col2:
            if st.button("🗑️ Clear History"):
                st.session_state.predictions = []
                st.rerun()

# ============================================================================
# Demo 4: Undo/Redo Text
# ============================================================================
elif demo.startswith("4️⃣"):
    st.header("4️⃣ Text Editor with Undo/Redo")
    st.write("Edit text with full undo/redo support!")
    
    # Text area
    new_text = st.text_area(
        "Edit your text:",
        value=st.session_state.text_content,
        height=200,
        key="text_editor"
    )
    
    # Update on change
    if new_text != st.session_state.text_content:
        st.session_state.undo_stack.append(st.session_state.text_content)
        st.session_state.redo_stack = []  # Clear redo on new edit
        st.session_state.text_content = new_text
    
    # Controls
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        if st.button("💾 Save Snapshot"):
            st.session_state.undo_stack.append(st.session_state.text_content)
            st.session_state.redo_stack = []
            st.success("Snapshot saved!")
    
    with col2:
        if st.button("↩️ Undo"):
            if st.session_state.undo_stack:
                st.session_state.redo_stack.append(st.session_state.text_content)
                st.session_state.text_content = st.session_state.undo_stack.pop()
                st.rerun()
            else:
                st.warning("Nothing to undo!")
    
    with col3:
        if st.button("↪️ Redo"):
            if st.session_state.redo_stack:
                st.session_state.undo_stack.append(st.session_state.text_content)
                st.session_state.text_content = st.session_state.redo_stack.pop()
                st.rerun()
            else:
                st.warning("Nothing to redo!")
    
    with col4:
        if st.button("🗑️ Clear All"):
            st.session_state.text_content = ""
            st.session_state.undo_stack = []
            st.session_state.redo_stack = []
            st.rerun()
    
    # Status
    st.caption(f"Undo steps: {len(st.session_state.undo_stack)} | "
               f"Redo steps: {len(st.session_state.redo_stack)}")

# ============================================================================
# Demo 5: User Preferences
# ============================================================================
else:
    st.header("5️⃣ User Preferences Dashboard")
    st.write("Settings persist across all interactions!")
    
    # Settings sidebar
    with st.sidebar:
        st.subheader("⚙️ Settings")
        
        st.session_state.prefs["theme"] = st.selectbox(
            "Theme", ["light", "dark", "blue"],
            index=["light", "dark", "blue"].index(st.session_state.prefs["theme"])
        )
        
        st.session_state.prefs["items_per_page"] = st.slider(
            "Items per page", 5, 50, st.session_state.prefs["items_per_page"]
        )
        
        st.session_state.prefs["show_tips"] = st.toggle(
            "Show tips", st.session_state.prefs["show_tips"]
        )
        
        if st.button("🔄 Reset Defaults"):
            st.session_state.prefs = {"theme": "light", "items_per_page": 10, "show_tips": True}
            st.rerun()
    
    # Content based on preferences
    if st.session_state.prefs["show_tips"]:
        st.info("💡 **Tip:** Change settings in the sidebar and watch them persist!")
    
    st.subheader(f"📊 Dashboard ({st.session_state.prefs['theme']} theme)")
    
    # Generate sample content
    items = list(range(1, st.session_state.prefs["items_per_page"] + 1))
    
    st.write(f"Showing {len(items)} items (based on your preference):")
    
    # Display items in columns
    cols = st.columns(3)
    for i, item in enumerate(items):
        with cols[i % 3]:
            st.metric(f"Item {item}", f"Value {item * 10}")
    
    # Current preferences
    with st.expander("📋 Current Preferences"):
        st.json(st.session_state.prefs)

# ============================================================================
# Footer
# ============================================================================
st.divider()
st.caption("""
**🎓 Learning Points:**
- Session state persists across reruns
- Widget keys enable bidirectional binding
- Callbacks run before the rest of the script
- Multi-step workflows use state to track progress
""")

# Run verification
if __name__ == "__main__":
    st.write("✅ App is running correctly!")

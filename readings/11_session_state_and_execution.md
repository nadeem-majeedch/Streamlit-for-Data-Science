# 11 — Streamlit Execution Model & Session State

> **📖 Reading · Module 07 · Intermediate**  
> *Understand why Streamlit reruns your script, how session state preserves data, and how to build stateful applications.*

---

## Learning Objectives

After completing this reading you will be able to:

- Explain Streamlit's top-to-bottom rerun execution model
- Understand why `st.session_state` is necessary for stateful apps
- Initialize and persist values across reruns
- Use callbacks for efficient state updates
- Implement multi-step workflows with proper state management
- Debug common state-related bugs

---

## 1. The Streamlit Execution Model

### Top-to-Bottom Reruns

Streamlit executes your script **from top to bottom on every interaction**. This is fundamentally different from traditional web frameworks.

```python
# Every time a user interacts with ANY widget,
# this ENTIRE script runs again from line 1
import streamlit as st

st.title("Counter")  # This runs every rerun
count = 0            # Reset to 0 every rerun!
count += 1           # Now count = 1 every rerun
st.write(f"Count: {count}")  # Always shows "Count: 1"
```

### Why Reruns?

Reruns make Streamlit simple:
- No event handlers to register
- No callbacks to wire up (unless you want them)
- Code is linear and readable
- State is explicit (through `st.session_state`)

### The Rerun Flow

```
User Interaction (click, type, select)
        │
        ▼
Widget value updates in browser
        │
        ▼
Streamlit sends new value to server
        │
        ▼
Script reruns from top to bottom
        │
        ▼
New page sent to browser
```

### Visual Analogy

Think of a Streamlit script like a **spreadsheet formula**:
- The formula (your script) defines how to compute results
- When any input changes, the formula recalculates
- The formula itself doesn't "remember" previous calculations

---

## 2. Why Session State is Necessary

### The Problem

```python
import streamlit as st

# This doesn't work as expected
counter = 0  # Reset on every rerun!

if st.button("Increment"):
    counter += 1  # This only affects the local variable
    
st.write(f"Counter: {counter}")  # Always shows 0
```

### The Solution: Session State

```python
import streamlit as st

# Initialize once (on first run)
if "counter" not in st.session_state:
    st.session_state.counter = 0

if st.button("Increment"):
    st.session_state.counter += 1  # Persists across reruns
    
st.write(f"Counter: {st.session_state.counter}")  # Actually increments!
```

### How Session State Works

- **Dictionary-like**: `st.session_state` behaves like a Python dictionary
- **Per-session**: Each user session has its own state
- **Persistent**: Values survive across reruns
- **Thread-safe**: Safe for concurrent users

---

## 3. Session State Fundamentals

### Initialization Patterns

```python
# Pattern 1: Check and initialize
if "key" not in st.session_state:
    st.session_state.key = default_value

# Pattern 2: Set defaults (Python 3.9+)
st.session_state.setdefault("key", default_value)

# Pattern 3: Nested initialization
if "user" not in st.session_state:
    st.session_state.user = {"name": "", "preferences": {}}
```

### Reading Values

```python
# Direct access
name = st.session_state.name

# With default (avoids KeyError)
count = st.session_state.get("count", 0)

# Check existence
if "initialized" in st.session_state:
    # Do something
```

### Modifying Values

```python
# Simple update
st.session_state.counter = 10

# Increment
st.session_state.counter += 1

# Update dictionary
st.session_state.user["name"] = "Alice"

# List operations
st.session_state.history.append(new_item)
```

### Deleting Values

```python
# Delete a key
del st.session_state.key

# Clear all state
for key in list(st.session_state.keys()):
    del st.session_state[key]
```

---

## 4. Widget-Session State Integration

### Bidirectional Binding

When a widget has a `key`, it's automatically linked to `st.session_state[key]`:

```python
# These are equivalent:
name = st.text_input("Name", key="name")
name = st.session_state.name  # Same value!
```

### Setting Widget Values Programmatically

```python
# Reset a text input
st.session_state.search = ""

# Set a slider position
st.session_state.price_range = (10, 50)

# Change a selectbox selection
st.session_state.category = "Electronics"
```

### Ordering Matters

```python
# ✅ Set value BEFORE widget renders
if st.button("Reset"):
    st.session_state.search = ""

st.text_input("Search", key="search")  # Shows updated value

# ❌ Set value AFTER widget renders (won't update this rerun)
st.text_input("Search", key="search")  # Shows old value
if st.button("Reset"):
    st.session_state.search = ""  # Only takes effect next rerun
```

---

## 5. Callbacks for Efficient Updates

### Basic Callback Pattern

```python
def on_change_handler():
    # Runs BEFORE the rest of the script
    st.session_state.log.append(st.session_state.query)

st.text_input("Query", key="query", on_change=on_change_handler)
```

### Callback Execution Order

```
User interacts with widget
        │
        ▼
Widget value updates
        │
        ▼
on_change callback runs
        │
        ▼
Rest of script runs
```

### Linking Widgets with Callbacks

```python
def update_derived():
    # When category changes, reset subcategory
    st.session_state.subcategory = "All"

st.selectbox("Category", categories, key="category",
             on_change=update_derived)

# This will show "All" when category changes
st.selectbox("Subcategory", subcategories, key="subcategory")
```

---

## 6. Multi-Step Workflows

### Step-by-Step Analysis

```python
import streamlit as st

# Initialize session state
if "step" not in st.session_state:
    st.session_state.step = 1
if "data" not in st.session_state:
    st.session_state.data = None
if "results" not in st.session_state:
    st.session_state.results = None

# Step 1: Upload Data
if st.session_state.step >= 1:
    st.header("Step 1: Upload Data")
    uploaded = st.file_uploader("Upload CSV", type="csv")
    if uploaded:
        st.session_state.data = pd.read_csv(uploaded)
        st.session_state.step = 2

# Step 2: Configure Analysis
if st.session_state.step >= 2:
    st.header("Step 2: Configure")
    target = st.selectbox("Target column", st.session_state.data.columns)
    if st.button("Run Analysis"):
        st.session_state.results = analyze(st.session_state.data, target)
        st.session_state.step = 3

# Step 3: View Results
if st.session_state.step >= 3:
    st.header("Step 3: Results")
    st.dataframe(st.session_state.results)
    
    if st.button("Start Over"):
        st.session_state.step = 1
        st.session_state.data = None
        st.session_state.results = None
```

### User Preferences

```python
# Initialize preferences
if "prefs" not in st.session_state:
    st.session_state.prefs = {
        "theme": "light",
        "language": "en",
        "items_per_page": 25
    }

# Sidebar for preferences
with st.sidebar:
    st.session_state.prefs["theme"] = st.selectbox(
        "Theme", ["light", "dark"], index=0
    )
    st.session_state.prefs["items_per_page"] = st.slider(
        "Items per page", 10, 100, 25
    )

# Main area uses preferences
items = get_items(per_page=st.session_state.prefs["items_per_page"])
```

### Prediction History

```python
if "predictions" not in st.session_state:
    st.session_state.predictions = []

# Input
features = get_user_input()

if st.button("Predict"):
    result = model.predict(features)
    st.session_state.predictions.append({
        "input": features,
        "prediction": result,
        "timestamp": datetime.now()
    })

# Display history
if st.session_state.predictions:
    st.subheader("Prediction History")
    for pred in reversed(st.session_state.predictions):
        st.write(f"{pred['timestamp']}: {pred['prediction']}")
```

---

## 7. Common State Bugs and Solutions

### Bug 1: State Not Persisting

**Symptom:** Values reset on every interaction.

**Cause:** Using local variables instead of session state.

**Solution:**
```python
# ❌ Wrong
count = 0
count += 1

# ✅ Correct
if "count" not in st.session_state:
    st.session_state.count = 0
st.session_state.count += 1
```

### Bug 2: Widget Value Not Updating

**Symptom:** Setting `st.session_state[key]` doesn't change what the widget shows.

**Cause:** Setting value after widget renders.

**Solution:**
```python
# ❌ Wrong
st.text_input("Name", key="name")
st.session_state.name = "Alice"  # Too late!

# ✅ Correct
st.session_state.name = "Alice"  # Set first
st.text_input("Name", key="name")  # Now renders with "Alice"
```

### Bug 3: Key Conflicts

**Symptom:** Two widgets show the same value.

**Cause:** Multiple widgets with the same key.

**Solution:**
```python
# ❌ Wrong
st.text_input("Name", key="name")
st.text_input("Email", key="name")  # Conflict!

# ✅ Correct
st.text_input("Name", key="user_name")
st.text_input("Email", key="user_email")
```

### Bug 4: Conditional Widget Rendering

**Symptom:** Widget values lost when hidden.

**Cause:** Widget not rendered on every rerun.

**Solution:**
```python
# ❌ Wrong
if show_advanced:
    st.slider("Threshold", key="threshold")  # Not rendered when hidden

# ✅ Correct
show_advanced = st.checkbox("Show advanced")
st.slider("Threshold", key="threshold", disabled=not show_advanced)
```

---

## 8. Best Practices

### Do's

1. **Initialize early** — set all session state keys at the top of your script
2. **Use descriptive keys** — `key="user_email"` not `key="ti1"`
3. **Check before accessing** — use `if "key" in st.session_state`
4. **Use callbacks for linked widgets** — efficient and predictable
5. **Separate state from presentation** — functions that modify state vs. functions that display

### Don'ts

1. **Don't store large objects unnecessarily** — use `@st.cache_data` for expensive computations
2. **Don't put widgets in conditional blocks** — use `disabled` instead
3. **Don't rely on rerun order** — use callbacks for linked updates
4. **Don't forget initialization** — always check `if "key" not in st.session_state`

---

## 9. State Management Patterns

### Pattern 1: Simple Counter/Flag

```python
if "count" not in st.session_state:
    st.session_state.count = 0

col1, col2 = st.columns(2)
with col1:
    if st.button("➕"):
        st.session_state.count += 1
with col2:
    if st.button("➖"):
        st.session_state.count -= 1

st.metric("Count", st.session_state.count)
```

### Pattern 2: Multi-Step Wizard

```python
# Initialize all steps
for step in ["upload", "configure", "analyze", "results"]:
    if step not in st.session_state:
        st.session_state[step] = {}

# Progress through steps
steps = ["upload", "configure", "analyze", "results"]
current = steps.index(st.session_state.get("current_step", "upload"))

# Navigation
if current > 0:
    if st.button("⬅️ Back"):
        st.session_state.current_step = steps[current - 1]
        st.rerun()

if current < len(steps) - 1:
    if st.button("Next ➡️"):
        st.session_state.current_step = steps[current + 1]
        st.rerun()
```

### Pattern 3: Undo/Redo

```python
if "history" not in st.session_state:
    st.session_state.history = []
    st.session_state.position = -1

def save_state():
    # Trim any redo history
    st.session_state.history = st.session_state.history[:st.session_state.position + 1]
    st.session_state.history.append(copy.deepcopy(st.session_state.data))
    st.session_state.position += 1

def undo():
    if st.session_state.position > 0:
        st.session_state.position -= 1
        st.session_state.data = copy.deepcopy(st.session_state.history[st.session_state.position])

def redo():
    if st.session_state.position < len(st.session_state.history) - 1:
        st.session_state.position += 1
        st.session_state.data = copy.deepcopy(st.session_state.history[st.session_state.position])
```

---

## Key Takeaways

- **Streamlit reruns your script top-to-bottom on every interaction** — this is the core execution model.
- **`st.session_state` preserves data across reruns** — without it, all local variables reset.
- **Widget keys create bidirectional binding** with session state.
- **Callbacks run before the rest of the script** — useful for linked widget updates.
- **Multi-step workflows** use session state to track progress and accumulate results.
- **Order matters** — set session state values before widgets that depend on them.
- **Initialize early** — check and set all required keys at the top of your script.

---

## Common Mistakes Cheat Sheet

| Mistake | Symptom | Fix |
|---------|---------|-----|
| Local variable for state | Value resets on rerun | Use `st.session_state` |
| Setting after widget | Widget doesn't update | Set before widget renders |
| Same key on two widgets | Conflicting values | Use unique keys |
| Widget in conditional | Value lost when hidden | Use `disabled` parameter |
| Forgetting initialization | KeyError | Check `if "key" not in st.session_state` |

---

## Further Reading

- [Streamlit Session State Docs](https://docs.streamlit.io/develop/api-reference/caching-and-state/st.session_state)
- [Execution Model](https://docs.streamlit.io/develop/concepts/architecture/exec-model)
- [Caching](https://docs.streamlit.io/develop/concepts/architecture/caching)

---

## Related Materials

- 📖 Reading: [04 — Widget Keys and Behavior](04_widget_keys_and_behavior.md)
- 📓 Notebook: [11 — Session State Execution Model](../notebooks/11_session_state_execution_model.ipynb)
- ✏️ Exercise: [11 — State Management Workshop](../exercises/11_state_management_workshop.py)
- 🖥️ Demo App: [11 — Session State Demo](../apps/11_session_state_demo.py)
- 📝 Quiz: [07 — Session State](../quizzes/07_session_state.md)

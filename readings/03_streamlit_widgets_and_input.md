# 03 — Streamlit Widgets & User Input

> **📖 Reading · Module 02 · Beginner**  
> *Master every widget type, understand how they behave, and learn to validate user input.*

---

## Learning Objectives

After completing this reading you will be able to:

- Use every core Streamlit widget: button, checkbox, radio, selectbox, multiselect, slider, number_input, text_input, text_area, date_input, time_input.
- Explain how widget return values work in the rerun model.
- Group widgets inside `st.form()` for batch submission.
- Apply input validation using the `validate` parameter (Streamlit ≥ 1.62).
- Choose the right widget for a given Data Science task.

---

## 1. How Widgets Work in Streamlit

Every widget function (`st.button()`, `st.slider()`, etc.) has two jobs:

1. **Render** an interactive element in the browser.
2. **Return** a value to your Python script — the current state of that widget.

Because of the rerun model, every time *any* widget changes, the script reruns and every widget returns its latest value.

### The Three Patterns

```python
import streamlit as st

# Pattern 1: Capture the return value directly
name = st.text_input("Your name")

# Pattern 2: Use a key for cross-rerun identity
age = st.number_input("Your age", key="user_age")

# Pattern 3: Use callbacks for side effects
def on_change():
    st.session_state.log.append(st.session_state.my_widget)
st.text_input("Type here", key="my_widget", on_change=on_change)
```

---

## 2. Buttons & Toggles

### `st.button` — Click Triggers

Returns `True` on the rerun *immediately after* the click, then `False` on subsequent reruns.

```python
if st.button("Click me"):
    st.write("Button was clicked!")  # This line only runs once
```

### `st.toggle` — Persistent On/Off

Unlike a button, a toggle maintains its state across reruns (it's a boolean widget).

```python
dark_mode = st.toggle("Enable dark mode")
if dark_mode:
    st.write("Dark mode is ON")
```

### `st.form_submit_button` — Batch Submission

Only fires when the form's submit button is clicked. All widgets inside the form share their values only upon submission.

---

## 3. Selection Widgets

### `st.selectbox` — Single Selection from a List

```python
color = st.selectbox("Pick a color", ["Red", "Green", "Blue"])
```

- Returns the selected value (a string, by default).
- Supports `index` to set the default, `placeholder` for empty state, and `format_func` for custom display.

### `st.multiselect` — Multiple Selections

```python
colors = st.multiselect("Pick colors", ["Red", "Green", "Blue"])
# colors is a list: ["Red", "Blue"]
```

- Returns a list of selected values.
- Supports `default` to pre-select items.

### `st.radio` — Exclusive Selection (Buttons)

```python
option = st.radio("Choose one", ["Option A", "Option B", "Option C"])
```

- Returns the selected value.
- Horizontal layout with `horizontal=True`.

### `st.select_slider` — Slider with Custom Labels

```python
size = st.select_slider("Size", options=["S", "M", "L", "XL"])
```

---

## 4. Text Input Widgets

### `st.text_input` — Single-Line Input

```python
email = st.text_input("Email address")
```

### `st.text_area` — Multi-Line Input

```python
notes = st.text_area("Notes", height=150)
```

### Validation (Streamlit ≥ 1.62)

The `validate` parameter enables **client-side validation** — the browser checks the input before the script reruns.

```python
email = st.text_input(
    "Email",
    type="email",          # Uses HTML5 email input
    validate=r".+@.+\..+", # Regex validation
)
```

The `type` parameter accepts:
- `"default"` — plain text
- `"password"` — masked input
- `"email"` — HTML5 email keyboard on mobile, validates email format
- `"url"` — HTML5 URL keyboard on mobile
- `"phone"` — HTML5 phone keyboard on mobile
- `"search"` — search-style input

```python
url = st.text_input("Website", type="url")
phone = st.text_input("Phone", type="phone")
search = st.text_input("Search", type="search")
```

> **Note:** The `validate` parameter and the specialized `type` values are new in Streamlit 1.62. They work on modern browsers and provide instant feedback.

---

## 5. Number & Slider Widgets

### `st.number_input` — Numeric Entry

```python
value = st.number_input("Enter a number", min_value=0, max_value=100, value=25, step=1)
```

### `st.slider` — Drag-to-Select Range

```python
# Single value
age = st.slider("Age", 0, 100, 25)

# Range selection (returns a tuple)
budget = st.slider("Budget range", 0, 10000, (1000, 5000))
```

### `st.select_slider` — Labeled Slider

```python
rating = st.select_slider("Rating", options=["Poor", "Fair", "Good", "Excellent"])
```

---

## 6. Date & Time Widgets

### `st.date_input` — Date Picker

```python
from datetime import date
dob = st.date_input("Date of birth", value=date(2000, 1, 1))
```

### `st.time_input` — Time Picker (Revamped in 1.61)

```python
from datetime import time
meeting = st.time_input("Meeting time", value=time(9, 0))
```

> **Note:** `st.time_input` was significantly improved in Streamlit 1.61 — it now supports seconds granularity via `step` parameter and better formatting.

### `st.datetime_input` — Date + Time Combined (New in 1.62)

```python
from datetime import datetime
appointment = st.datetime_input("Appointment", value=datetime(2026, 1, 15, 10, 30))
```

---

## 7. Color & File Widgets

### `st.color_picker` — Color Selection

```python
color = st.color_picker("Pick a color", "#FF5733")
```

### `st.file_uploader` — File Upload

```python
uploaded_file = st.file_uploader("Upload CSV", type=["csv"])
if uploaded_file:
    import pandas as pd
    df = pd.read_csv(uploaded_file)
    st.dataframe(df)
```

---

## 8. Buttons & Downloads

### `st.button` — Action Trigger

```python
if st.button("Process data"):
    st.write("Processing...")
```

### `st.download_button` — File Download

```python
import pandas as pd
df = pd.DataFrame({"x": [1, 2, 3], "y": [4, 5, 6]})
csv = df.to_csv(index=False)

st.download_button(
    label="Download data as CSV",
    data=csv,
    file_name="data.csv",
    mime="text/csv",
)
```

> **Tip:** `st.download_button` can also accept file-like objects (e.g., `open("file.csv")`) and will auto-infer `file_name` and `mime` (Streamlit ≥ 1.61).

---

## 9. Forms — Batch Widget Submission

Forms let you group widgets and submit them all at once, avoiding a rerun on every keystroke.

```python
with st.form("my_form"):
    name = st.text_input("Name")
    age = st.number_input("Age", 0, 120, 25)
    submitted = st.form_submit_button("Submit")

if submitted:
    st.write(f"Name: {name}, Age: {age}")
```

### Form Behavior

- Widgets inside a form **do not trigger reruns** while the user interacts with them.
- All values are submitted to the script **only when the submit button is clicked**.
- Forms cannot be nested (as of Streamlit 1.62).
- Each form needs a unique `key` or is identified by position.

---

## 10. Widget Keys & Identity

Every widget can accept a `key` parameter — a unique string identifier.

```python
st.text_input("Email", key="email_input")
```

### Why Keys Matter

1. **Session state access:** `st.session_state.email_input` gives you the widget's value.
2. **Stability:** Without explicit keys, Streamlit generates auto-keys based on widget order. Inserting a widget shifts all downstream keys.
3. **Cross-widget communication:** Use `on_change` callbacks with keys to link widgets.

### Best Practice

> **Always provide explicit keys** in production apps. Auto-keys break when you reorder widgets.

```python
# Good
st.text_input("Email", key="email")

# Fragile (order-dependent)
st.text_input("Email")  # Auto-key like "text_input-0"
```

---

## 11. Widget Callbacks

Callbacks let you run code when a widget changes, without waiting for the next rerun.

```python
def update_log():
    st.session_state.history.append(st.session_state.query)

st.text_input(
    "Search query",
    key="query",
    on_change=update_log,
)
```

### Callback Parameters

| Parameter | Purpose |
|---|---|
| `on_change` | Runs when the widget value changes |
| `on_click` | Runs when a button is clicked |
| `args` | Positional arguments to pass to the callback |
| `kwargs` | Keyword arguments to pass to the callback |

---

## 12. Widget Disabled State

Every widget supports `disabled=True` to render it grayed-out and non-interactive. Since Streamlit 1.60, disabled state is enforced **server-side** — a disabled widget's value cannot be tampered with via the browser.

```python
st.text_input("Read-only field", value="Hello", disabled=True)
```

---

## 13. Choosing the Right Widget

| Task | Widget | Why |
|---|---|---|
| Toggle a setting on/off | `st.toggle` or `st.checkbox` | Boolean state |
| Pick one from a list | `st.selectbox` or `st.radio` | Single selection |
| Pick many from a list | `st.multiselect` | Multiple selections |
| Enter a number | `st.number_input` | Precise numeric entry |
| Choose a range | `st.slider` | Visual range selection |
| Enter text | `st.text_input` or `st.text_area` | Single vs. multi-line |
| Enter a date | `st.date_input` | Calendar picker |
| Pick a color | `st.color_picker` | Color wheel |
| Upload a file | `st.file_uploader` | File handling |
| Trigger an action | `st.button` | One-shot action |
| Download results | `st.download_button` | Export data |
| Group and submit | `st.form` | Batch submission |

---

## Key Takeaways

- Widgets return their current value on every rerun — that's how Streamlit gets input.
- `st.selectbox`, `st.multiselect`, `st.radio` handle selection; `st.slider` and `st.number_input` handle numeric input.
- `st.text_input` supports client-side validation via `validate` and specialized `type` (≥ 1.62).
- `st.form` groups widgets to avoid per-keystroke reruns.
- **Always use explicit `key` parameters** for stability and session_state access.
- `on_change` callbacks enable side effects without additional reruns.

---

## Further Reading

- [Streamlit Widgets API Reference](https://docs.streamlit.io/develop/api-reference/widgets)
- [Streamlit Forms](https://docs.streamlit.io/develop/api-reference/execution-flow/st.form)
- [Streamlit Execution Model](https://docs.streamlit.io/develop/concepts/architecture/exec-model)

---

## Related Materials

- 📖 Reading: [04 — Widget Keys & Behavior](04_widget_keys_and_behavior.md)
- 📓 Notebook: [03 — Streamlit Widgets](../notebooks/03_streamlit_widgets.ipynb)
- 📓 Notebook: [04 — Interactive Data Science Controls](../notebooks/04_interactive_ds_controls.ipynb)
- 🖥️ Demo App: [03 — Widgets Demo](../apps/03_widgets_demo.py)
- 🖥️ Demo App: [04 — Forms Demo](../apps/04_forms_demo.py)
- ✏️ Exercise: [03 — Widget Mastery](../exercises/03_widget_mastery.py)
- ✏️ Exercise: [04 — Dataset Filter App](../exercises/04_dataset_filter_app.py)
- 📝 Quiz: [02 — Widgets & Input](../quizzes/02_widgets_input.md)

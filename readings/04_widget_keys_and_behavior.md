# 04 — Widget Keys, Identity & Behavior

> **📖 Reading · Module 02 · Beginner**  
> *Understand why widget keys matter, how identity works, and how to debug widget behavior.*

---

## Learning Objectives

After completing this reading you will be able to:

- Explain how Streamlit assigns identity to widgets.
- Use the `key` parameter to create stable, predictable widget identifiers.
- Access widget values through `st.session_state` using keys.
- Debug common widget behavior issues.
- Use callbacks to create linked widget interactions.

---

## 1. Widget Identity in Streamlit

When Streamlit renders a widget, it needs to track its state across reruns. It does this through **identity** — a way to know which widget is which.

### Auto-Generated Keys

If you don't provide a `key`, Streamlit generates one automatically based on:

1. The widget type (e.g., `text_input`)
2. The label text (e.g., `"Enter your name"`)
3. The order of appearance in the script

```python
# Auto-key might be something like "text_input-Enter your name-1"
st.text_input("Enter your name")
```

### The Problem with Auto-Keys

Auto-keys break when you modify the script:

```python
# Version 1
st.text_input("Name")    # Auto-key: "text_input-Name-0"
st.text_input("Email")   # Auto-key: "text_input-Email-1"

# Version 2 (inserted a widget between them)
st.text_input("Name")    # Auto-key: "text_input-Name-0"
st.text_input("Phone")   # Auto-key: "text_input-Phone-1" ← NEW
st.text_input("Email")   # Auto-key: "text_input-Email-2" ← CHANGED!
```

The email widget's auto-key changed from `1` to `2`. Streamlit now treats it as a **different widget** — its previous value is lost.

### The Fix: Explicit Keys

```python
st.text_input("Name", key="name")
st.text_input("Phone", key="phone")  # New widget — no disruption
st.text_input("Email", key="email")  # Same key as before ✓
```

> **Rule of thumb:** If you're building anything beyond a throwaway script, use explicit keys on every widget.

---

## 2. Keys and Session State

When a widget has a `key`, its value is automatically stored in `st.session_state[key]`.

```python
st.text_input("Email", key="email")
# This automatically creates st.session_state.email
```

You can read and modify widget values through session state:

```python
# Read the current value
current_email = st.session_state.email

# Set a value programmatically
st.session_state.email = "default@example.com"
```

### Bidirectional Binding

Widgets with keys have **bidirectional binding** with `st.session_state`:

1. User types in the widget → `st.session_state[key]` updates → script reruns.
2. You set `st.session_state[key] = new_value` → the widget displays the new value.

```python
st.text_input("Search", key="search")

if st.button("Clear search"):
    st.session_state.search = ""  # Widget will show empty on next rerun
```

---

## 3. Callbacks — Reacting to Widget Changes

Callbacks let you run a function **when a widget's value changes**, before the rest of the script executes.

### Basic Callback Pattern

```python
def log_change():
    st.session_state.history.append(st.session_state.query)

st.text_input("Search", key="query", on_change=log_change)
```

### Callback Flow

```
User types in widget
        │
        ▼
Widget value updates in session_state
        │
        ▼
on_change callback runs
        │
        ▼
Rest of script runs
```

### Linking Widgets with Callbacks

You can use callbacks to make one widget affect another:

```python
def sync_name_to_greeting():
    st.session_state.greeting = f"Hello, {st.session_state.name}!"

st.text_input("Your name", key="name", on_change=sync_name_to_greeting)
st.text_input("Greeting", key="greeting")
```

---

## 4. Widget Return Values vs. Session State

| Aspect | Return Value | Session State |
|---|---|---|
| **Access** | `value = st.widget(...)` | `st.session_state.key` |
| **Availability** | Only in the current rerun | Persists across reruns |
| **Modification** | Can't modify directly | Can modify: `st.session_state.key = x` |
| **Use case** | Simple, one-shot reads | Cross-widget logic, persistence |

### When to Use Which

```python
# Simple case — return value is fine
color = st.selectbox("Color", ["Red", "Green", "Blue"])

# Complex case — need session state
if "history" not in st.session_state:
    st.session_state.history = []

selection = st.selectbox("Pick", ["A", "B", "C"], key="pick")
if st.button("Save"):
    st.session_state.history.append(st.session_state.pick)
```

---

## 5. Widget Behavior Across Reruns

### Value Persistence

When a widget has a `key`, its value persists across reruns via session state. Without a key, the value is "forgotten" unless you capture it in a variable — but that variable is reinitialized on each rerun.

### Default Values

You can set defaults for widgets. The default is used on the **first** rerun. On subsequent reruns, the widget uses the value from session state.

```python
# Default only applies on first load
st.slider("Price", 0, 100, value=25, key="price")
```

### Conditional Rendering

Be careful with widgets inside conditional blocks — they may not render on every rerun, which can cause key conflicts.

```python
# ⚠️ DANGER: Widget may not render on every rerun
if st.checkbox("Show more options"):
    st.text_input("Extra field", key="extra")  # Only rendered sometimes

# ✅ SAFER: Always render, disable when needed
show_extra = st.checkbox("Show more options")
st.text_input("Extra field", key="extra", disabled=not show_extra)
```

---

## 6. Common Widget Behavior Issues

### Issue 1: Widget Value Resets

**Symptom:** Widget shows default value instead of user's input.

**Cause:** Missing `key` parameter, or widget order changed.

**Fix:** Add explicit `key` parameter.

### Issue 2: Widget Not Updating

**Symptom:** Setting `st.session_state.key = new_value` doesn't update the widget.

**Cause:** You're setting the value in the same rerun where the widget is rendered.

**Fix:** Use a callback or set the value *before* the widget is rendered.

```python
# ❌ This doesn't work as expected
st.text_input("Name", key="name")
if st.button("Reset"):
    st.session_state.name = ""  # Set after widget — won't update this rerun

# ✅ This works
if st.button("Reset"):
    st.session_state.name = ""  # Set before the widget renders
st.text_input("Name", key="name")
```

### Issue 3: Callback Not Firing

**Symptom:** `on_change` function doesn't execute.

**Cause:** Callback runs on value change, not on initial render.

**Fix:** Check if you need `on_change` or if you should just read the value directly.

### Issue 4: Form vs. Non-Form Behavior

**Symptom:** Widget triggers a rerun inside a form.

**Cause:** Form submit buttons are the only widgets that trigger reruns inside forms.

**Fix:** Ensure non-submit widgets are inside a `with st.form(...)` block.

---

## 7. Best Practices

1. **Always use explicit keys** — avoid auto-generated keys in production code.
2. **Use descriptive key names** — `key="email"` is better than `key="ti1"`.
3. **Keep keys unique** — no two widgets should share a key.
4. **Use session_state for cross-widget logic** — not return values.
5. **Set default values before the widget** if you need programmatic control.
6. **Avoid widgets in conditionals** — use `disabled` instead.
7. **Use callbacks for linked updates** — don't rely on rerun ordering.

---

## Key Takeaways

- Streamlit assigns identity to widgets via auto-generated keys or explicit `key` parameters.
- **Always use explicit keys** to avoid breakage when scripts change.
- Keys enable bidirectional binding with `st.session_state`.
- Callbacks (`on_change`, `on_click`) run when widget values change.
- Widgets persist their values across reruns when they have keys.
- Be careful with widgets inside conditional blocks — they may not always render.

---

## Further Reading

- [Streamlit Session State Docs](https://docs.streamlit.io/develop/api-reference/caching-and-state/st.session_state)
- [Streamlit Widget Behavior](https://docs.streamlit.io/develop/concepts/architecture/exec-model)
- [Streamlit Forms vs. Widgets](https://docs.streamlit.io/develop/api-reference/execution-flow)

---

## Related Materials

- 📖 Reading: [03 — Streamlit Widgets & User Input](03_streamlit_widgets_and_input.md)
- 📓 Notebook: [03 — Streamlit Widgets](../notebooks/03_streamlit_widgets.ipynb)
- 📓 Notebook: [04 — Interactive Data Science Controls](../notebooks/04_interactive_ds_controls.ipynb)
- 🖥️ Demo App: [03 — Widgets Demo](../apps/03_widgets_demo.py)
- ✏️ Exercise: [03 — Widget Mastery](../exercises/03_widget_mastery.py)

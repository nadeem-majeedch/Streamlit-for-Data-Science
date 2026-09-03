# Quiz 05 — Session State & App Memory

> **📝 Post-Quiz · Module 05 · Intermediate**
> *Test your understanding of Streamlit's execution model, session state, and callbacks.*
> ⏱ Time: 15 minutes · 📊 Points: 25 · Bloom's: Understand, Apply

---

## Part A: Multiple Choice (2 points each)

### Q1. What is Streamlit's execution model?

(a) Event-driven like Flask
(b) Top-to-bottom rerun on every user interaction
(c) WebSocket-based real-time updates
(d) Background thread processing

**CLO:** CLO1, CLO4

---

### Q2. How do you initialize a session state variable?

(a) `st.session_state.counter = 0` (at the top of the script)
(b) `if "counter" not in st.session_state: st.session_state.counter = 0`
(c) `st.init_state("counter", 0)`
(d) `st.state.set("counter", 0)`

**CLO:** CLO4

---

### Q3. What does a callback (`on_change`) do?

(a) Runs after the entire script finishes
(b) Runs before the rest of the script after a widget change
(c) Replaces the rerun model
(d) Only runs on the first page load

**CLO:** CLO4

---

### Q4. Which pattern correctly implements a counter?

```python
# Pattern A
count = 0
if st.button("+"):
    count += 1

# Pattern B
if "count" not in st.session_state:
    st.session_state.count = 0
if st.button("+"):
    st.session_state.count += 1
st.write(st.session_state.count)
```

(a) Pattern A works correctly
(b) Pattern B works correctly
(c) Both work correctly
(d) Neither works correctly

**CLO:** CLO4

---

### Q5. What is `st.rerun()` used for?

(a) To restart the Streamlit server
(b) To force an immediate rerun of the script
(c) To clear session state
(d) To navigate to a different page

**CLO:** CLO4

---

## Part B: True/False (1 point each)

### Q6. Session state is shared between different users of the same app.

**CLO:** CLO4

---

### Q7. A variable defined outside session state (e.g., `count = 0`) persists across reruns.

**CLO:** CLO4

---

### Q8. `st.fragment` allows partial reruns of a Streamlit app.

**CLO:** CLO4

---

## Part C: Short Answer (3 points each)

### Q9. A student writes this code and reports the counter always shows 0:

```python
import streamlit as st

count = 0
if st.button("Increment"):
    count += 1
st.metric("Count", count)
```

Explain why this happens and provide the corrected code.

**CLO:** CLO4

---

### Q10. Explain the difference between initializing session state with `st.session_state.x = 1` at the top of the script vs. using `st.session_state.setdefault("x", 1)`.

**CLO:** CLO4

---

### Q11. You are building a multi-step form (Step 1 → Step 2 → Step 3). Describe how you would use session state to track the current step and persist form data between steps.

**CLO:** CLO4, CLO2

---

## Part D: Code Output (3 points each)

### Q12. What is displayed after the user clicks the button TWICE?

```python
import streamlit as st

if "items" not in st.session_state:
    st.session_state.items = []

if st.button("Add"):
    st.session_state.items.append(len(st.session_state.items) + 1)

st.write(st.session_state.items)
```

**CLO:** CLO4

---

## Part E: Debugging (4 points)

### Q13. This app should let users set and retrieve a saved note. Find and fix ALL bugs:

```python
import streamlit as st

note = ""

saved_note = st.text_area("Write your note:")
if st.button("Save"):
    note = saved_note

if st.button("Show Saved"):
    st.write(f"Saved note: {note}")
```

**CLO:** CLO4

---

## Answer Key

> ⚠️ **Instructor copy**

| Q | Answer | Explanation | Bloom's |
|---|--------|-------------|---------|
| Q1 | **(b)** | Streamlit reruns the script top-to-bottom on every interaction. | Understand |
| Q2 | **(b)** | Conditional initialization prevents overwriting on every rerun. | Apply |
| Q3 | **(b)** | Callbacks run after widget change but before the rest of the script. | Understand |
| Q4 | **(b)** | Pattern B uses session_state; Pattern A resets to 0 on every rerun. | Apply |
| Q5 | **(b)** | `st.rerun()` forces an immediate script rerun. | Understand |
| Q6 | **False** | Session state is per-session (per-user). | Understand |
| Q7 | **False** | Regular variables reset on every rerun. Only session_state persists. | Understand |
| Q8 | **True** | `st.fragment` enables partial reruns for performance. | Understand |
| Q9 | The variable `count` is a local variable that resets to 0 on every rerun. Fix: use `st.session_state`. | Apply |
| Q10 | Both work for initialization, but `setdefault` is safer because it doesn't overwrite existing values. At the top of the script, direct assignment resets the value on every rerun. `setdefault` only sets if the key doesn't exist. | Understand |
| Q11 | Store `current_step` in session_state (1, 2, or 3). Store form data in a session_state dict. Each step reads/writes to the dict. Navigation buttons update `current_step` and call `st.rerun()`. | Apply |
| Q12 | After two clicks: `[1, 2]`. Each click appends the next integer (length + 1). | Apply |
| Q13 | Bug 1: `note` is a regular variable, resets to "" on rerun. Bug 2: Show button loads the reset empty note. Fix: Use `st.session_state.note` instead of `note`. | Apply |

---

## CLO Mapping

| CLO | Questions |
|-----|-----------|
| CLO1 — Explain core concepts | Q1 |
| CLO2 — Build interactive apps | Q11 |
| CLO4 — Manage application state | Q2–Q13 |

---

## Related Materials

- 📖 Reading: [Session State & Execution](../readings/11_session_state_and_execution.md)
- 📓 Notebook: [11 — Session State](../notebooks/11_session_state_execution_model.ipynb)
- ✏️ Exercise: [11 — State Management](../exercises/11_state_management_workshop.py)

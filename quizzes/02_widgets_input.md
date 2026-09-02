# Quiz 02 — Widgets & User Input

> **📝 Quiz · Module 02 · Beginner**  \n> *Test your understanding of Streamlit widgets, forms, and input handling.*  \n> ⏱ Time: 15 minutes · 📊 Points: 20

---

## Instructions

Answer all questions. For multiple-choice questions, circle the correct answer. For code questions, write the complete code.

---

## Part A: Multiple Choice (2 points each)

### Q1. What does a Streamlit widget return on every rerun?

(a) Nothing — widgets only display output  
(b) The widget's current value  
(c) A callback function  
(d) The widget's HTML source

---

### Q2. Which widget would you use to let a user select multiple items from a list?

(a) `st.selectbox()`  
(b) `st.radio()`  
(c) `st.multiselect()`  
(d) `st.checkbox()`

---

### Q3. What is the purpose of the `key` parameter on a widget?

(a) It sets the widget's default value  
(b) It makes the widget visible  
(c) It provides a unique identifier for session_state access and stability  
(d) It changes the widget's color

---

### Q4. What happens when a widget is inside a `st.form()`?

(a) The widget triggers a rerun on every interaction  
(b) The widget's value is not available to the script  
(c) The widget only submits its value when the form's submit button is clicked  
(d) The widget is disabled

---

### Q5. Which parameter enables client-side validation in `st.text_input()` (Streamlit ≥ 1.62)?

(a) `validate`  
(b) `pattern`  
(c) `check`  
(d) `required`

---

## Part B: Short Answer (3 points each)

### Q6. Explain the difference between a widget's **return value** and its value in **session_state**. When would you use each?

---

### Q7. Describe what happens to a counter variable if you write this code:

```python
count = 0
if st.button("Increment"):
    count += 1
st.write(f"Count: {count}")
```

Why does it not work as expected? What is the fix?

---

## Part C: Code Completion (4 points)

### Q8. Complete this code to create a form that collects a user's name and email, and displays a success message on valid submission:

```python
import streamlit as st

# TODO: Create a form with key "registration"
with st.form(______):
    name = st.text_input("Name")
    email = st.text_input("Email", type="email")
    submitted = st.form_submit_button("Register")

if submitted:
    if not name or not email:
        st.______("Please fill in all fields.")
    else:
        st.______(f"Welcome, {name}!")
```

---

## Answer Key (Instructor Only)

> **A1:** (b) The widget's current value  
> **A2:** (c) `st.multiselect()`  
> **A3:** (c) It provides a unique identifier for session_state access and stability  
> **A4:** (c) The widget only submits its value when the form's submit button is clicked  
> **A5:** (a) `validate`  
> **A6:** Return value is available only in the current rerun; session_state persists across reruns. Use return value for simple reads; use session_state for cross-widget logic or persistence.  
> **A7:** The count resets to 0 on every rerun because `count = 0` runs each time. Fix: use `st.session_state.count` instead of a local variable.  
> **A8:** `"registration"`, `error`, `success`

---

## Related Materials

- 📖 Reading: [03 — Streamlit Widgets & User Input](../readings/03_streamlit_widgets_and_input.md)
- 📖 Reading: [04 — Widget Keys & Behavior](../readings/04_widget_keys_and_behavior.md)
- 📓 Notebook: [03 — Streamlit Widgets](../notebooks/03_streamlit_widgets.ipynb)
- 📓 Notebook: [04 — Interactive Data Science Controls](../notebooks/04_interactive_ds_controls.ipynb)
- ✏️ Exercise: [03 — Widget Mastery](../exercises/03_widget_mastery.py)
- ✏️ Exercise: [04 — Dataset Filter App](../exercises/04_dataset_filter_app.py)

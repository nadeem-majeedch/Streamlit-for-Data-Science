# Quiz 07: Session State & Execution Model

> **📝 Quiz · Module 07 · Intermediate**  
> *Test your understanding of Streamlit's execution model and session state.*

---

## Multiple Choice

### Q1. What happens when a user interacts with a Streamlit widget?

a) Only the callback function executes  
b) The entire script reruns from top to bottom  
c) Only the affected widget rerenders  
d) The script pauses and waits for input

---

### Q2. Which statement about `st.session_state` is TRUE?

a) It's a global Python dictionary  
b) It persists data across reruns for each session  
c) It automatically stores all widget values  
d) It's cleared after each page navigation

---

### Q3. What is the correct way to initialize a session state variable?

```python
# Option A
counter = 0

# Option B  
if "counter" not in st.session_state:
    st.session_state.counter = 0

# Option C
st.session_state.counter = 0

# Option D
st.cache("counter", 0)
```

---

### Q4. Why does the following code NOT work as expected?

```python
counter = 0
if st.button("Increment"):
    counter += 1
st.write(f"Count: {counter}")
```

a) `st.button` returns None  
b) The `+=` operator doesn't work with integers  
c) `counter` resets to 0 on each rerun  
d) `st.write` can't display integers

---

### Q5. When a widget has a `key` parameter, what happens?

a) The widget's value is cached for performance  
b) The widget creates a session state entry automatically  
c) The widget is stored in a database  
d) The widget is hidden from the user

---

### Q6. What is the correct order for setting widget values programmatically?

```python
# Option A
st.text_input("Name", key="name")
st.session_state.name = "Alice"

# Option B
st.session_state.name = "Alice"
st.text_input("Name", key="name")
```

a) Option A is correct  
b) Option B is correct  
c) Both work the same way  
d) Neither works

---

### Q7. When do `on_change` callbacks execute?

a) Before the script starts  
b) After the entire script finishes  
c) Before the rest of the script runs  
d) Only when the page loads

---

### Q8. What is the problem with putting widgets inside conditional blocks?

```python
if st.checkbox("Show option"):
    st.slider("Value", key="value")
```

a) The widget will be disabled  
b) The widget may not render on every rerun, causing key conflicts  
c) The widget will be hidden  
d) There's no problem

---

### Q9. Which pattern is correct for linked widgets?

```python
# Option A
def on_category_change():
    st.session_state.subcategory = "Option 1"

category = st.selectbox("Category", ["A", "B"], 
                        on_change=on_category_change)
subcategory = st.selectbox("Subcategory", ["Option 1", "Option 2"])

# Option B
category = st.selectbox("Category", ["A", "B"])
if category == "A":
    st.session_state.subcategory = "Option 1"
subcategory = st.selectbox("Subcategory", ["Option 1", "Option 2"])
```

a) Option A is correct  
b) Option B is correct  
c) Both are correct  
d) Neither is correct

---

### Q10. What is the benefit of using `@st.cache_data` vs `st.session_state` for storing data?

a) `@st.cache_data` is faster  
b) `@st.cache_data` persists across sessions, `st.session_state` doesn't  
c) `@st.cache_data` is for expensive computations, `st.session_state` is for user input  
d) They're identical

---

### Q11. In a multi-step wizard, how should you track the current step?

a) Use a local variable  
b) Use a URL parameter  
c) Use `st.session_state.step`  
d) Use `st.cache`

---

### Q12. What happens when you click "Undo" in a text editor with session state?

a) The browser goes back  
b) Pop from undo_stack, push current to redo_stack, update text  
c) Clear all session state  
d) Rerun the script without changes

---

## Short Answer

### Q13. Explain why Streamlit uses a rerun execution model instead of traditional event handlers. What are the benefits and trade-offs?

---

### Q14. A user reports that their counter resets every time they click a button. Write the corrected code:

```python
# Broken code:
counter = 0
if st.button("Add"):
    counter += 1
st.write(counter)
```

---

### Q15. Design a session state structure for a quiz application that needs to:
- Track current question number
- Store user answers
- Track which questions were answered correctly
- Maintain a score

Write the initialization code.

---

## Code Completion

### Q16. Complete the undo/redo pattern:

```python
if "undo_stack" not in st.session_state:
    st.session_state.undo_stack = []
if "redo_stack" not in st.session_state:
    st.session_state.redo_stack = []
if "current_text" not in st.session_state:
    st.session_state.current_text = ""

def save_snapshot():
    st.session_state.undo_stack.append(st.session_state.current_text)
    st.session_state.redo_stack = []  # TODO: Why clear redo_stack?

def undo():
    if st.session_state.undo_stack:  # TODO: Complete the undo logic
        # TODO: Write the code here
        pass

def redo():
    if st.session_state.redo_stack:  # TODO: Complete the redo logic
        # TODO: Write the code here
        pass
```

---

### Q17. Complete the multi-step form:

```python
if "form_step" not in st.session_state:
    st.session_state.form_step = 1
if "form_data" not in st.session_state:
    st.session_state.form_data = {}

# Step 1
if st.session_state.form_step == 1:
    name = st.text_input("Name")
    if st.button("Next"):
        # TODO: Save name and advance to step 2
        pass

# Step 2  
elif st.session_state.form_step == 2:
    email = st.text_input("Email")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Back"):
            # TODO: Go back to step 1
            pass
    with col2:
        if st.button("Submit"):
            # TODO: Save email and show success
            pass
```

---

## Answer Key

### Multiple Choice

1. **B** - Streamlit reruns the entire script top-to-bottom on every interaction
2. **B** - Session state persists data across reruns for each user session
3. **B** - Check if key exists before initializing to avoid overwriting
4. **C** - Local variables reset on each rerun; use session state instead
5. **B** - Widget keys create automatic bidirectional binding with session state
6. **B** - Set the value BEFORE the widget renders for immediate effect
7. **C** - Callbacks execute before the rest of the script runs
8. **B** - Widgets in conditionals may not render, causing key conflicts
9. **A** - Use callbacks for linked widget updates, not conditional checks
10. **C** - Cache is for expensive computations; session state is for user data
11. **C** - Use session state to track wizard progress across reruns
12. **B** - Pop from undo, push current to redo, update the text

### Short Answer

**Q13.** Benefits: Simpler code (no event handlers), linear execution, explicit state management, easier debugging. Trade-offs: Complete reruns can be slow for large apps (mitigated by caching), must understand state management, no incremental updates.

**Q14.**
```python
if "counter" not in st.session_state:
    st.session_state.counter = 0

if st.button("Add"):
    st.session_state.counter += 1
st.write(st.session_state.counter)
```

**Q15.**
```python
if "quiz" not in st.session_state:
    st.session_state.quiz = {
        "current_question": 0,
        "answers": {},
        "correct": {},
        "score": 0
    }
```

### Code Completion

**Q16.**
```python
def save_snapshot():
    st.session_state.undo_stack.append(st.session_state.current_text)
    st.session_state.redo_stack = []  # New edits invalidate redo history

def undo():
    if st.session_state.undo_stack:
        st.session_state.redo_stack.append(st.session_state.current_text)
        st.session_state.current_text = st.session_state.undo_stack.pop()

def redo():
    if st.session_state.redo_stack:
        st.session_state.undo_stack.append(st.session_state.current_text)
        st.session_state.current_text = st.session_state.redo_stack.pop()
```

**Q17.**
```python
# Step 1
if st.session_state.form_step == 1:
    name = st.text_input("Name")
    if st.button("Next"):
        st.session_state.form_data["name"] = name
        st.session_state.form_step = 2
        st.rerun()

# Step 2  
elif st.session_state.form_step == 2:
    email = st.text_input("Email")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Back"):
            st.session_state.form_step = 1
            st.rerun()
    with col2:
        if st.button("Submit"):
            st.session_state.form_data["email"] = email
            st.session_state.form_step = 1
            st.success("Registration complete!")
            st.json(st.session_state.form_data)
            st.session_state.form_data = {}
```

---

## Related Materials

- 📖 Reading: [11 — Session State & Execution](../readings/11_session_state_and_execution.md)
- 📓 Notebook: [11 — Session State Execution Model](../notebooks/11_session_state_execution_model.ipynb)
- ✏️ Exercise: [11 — State Management Workshop](../exercises/11_state_management_workshop.py)
- 🖥️ Demo App: [11 — Session State Demo](../apps/11_session_state_demo.py)

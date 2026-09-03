# Exercise 11 — State Management: Solution Notes

> **👩‍🏫 Instructor Reference**
> *Expected approach, key code, and grading guidance.*

---

## Challenge 1: Counter with History

### Expected Approach
Initialize `counter` and `history` in session state. Use three columns for buttons. Each button updates counter AND appends to history list.

### Key Code
```python
if "counter" not in st.session_state:
    st.session_state.counter = 0
    st.session_state.history = []

col1, col2, col3 = st.columns(3)
with col1:
    if st.button("➕ Increment"):
        old = st.session_state.counter
        st.session_state.counter += 1
        st.session_state.history.append({
            "action": "Increment", "old": old, "new": st.session_state.counter
        })
with col2:
    if st.button("➖ Decrement"):
        old = st.session_state.counter
        st.session_state.counter -= 1
        st.session_state.history.append({
            "action": "Decrement", "old": old, "new": st.session_state.counter
        })
with col3:
    if st.button("🔄 Reset"):
        old = st.session_state.counter
        st.session_state.counter = 0
        st.session_state.history.append({
            "action": "Reset", "old": old, "new": 0
        })

st.metric("Counter", st.session_state.counter)

if st.session_state.history:
    st.subheader("History")
    for entry in st.session_state.history[-10:][::-1]:
        st.write(f"{entry['action']}: {entry['old']} → {entry['new']}")
```

### Common Mistakes
- Using global variable instead of session_state
- Forgetting to record old value before changing
- Not handling initial state (history = [])

### Grading Notes (25 marks)
- Full marks: Counter works, history tracks all changes, clear history button
- 18 marks: Counter works, history partially working
- 10 marks: Counter works but no history

---

## Challenge 2: Multi-Step Form Wizard

### Expected Approach
Track `current_step` and `form_data` in session_state. Show/hide sections based on step. Navigation buttons update step and store data.

### Key Pattern
```python
if "current_step" not in st.session_state:
    st.session_state.current_step = 1
    st.session_state.form_data = {}

# Progress bar
st.progress(st.session_state.current_step / 3)

if st.session_state.current_step == 1:
    name = st.text_input("Name", value=st.session_state.form_data.get("name", ""))
    email = st.text_input("Email", value=st.session_state.form_data.get("email", ""))
    if st.button("Next →"):
        if name and email:
            st.session_state.form_data["name"] = name
            st.session_state.form_data["email"] = email
            st.session_state.current_step = 2
            st.rerun()

elif st.session_state.current_step == 2:
    # Demographics step...
    if st.button("← Back"):
        st.session_state.current_step = 1
        st.rerun()
    if st.button("Next →"):
        st.session_state.current_step = 3
        st.rerun()

elif st.session_state.current_step == 3:
    # Preferences step...
    if st.button("Submit"):
        # Save to submissions list
        if "submissions" not in st.session_state:
            st.session_state.submissions = []
        st.session_state.submissions.append(st.session_state.form_data.copy())
        st.success("Submitted!")
        st.session_state.current_step = 1
        st.session_state.form_data = {}
        st.rerun()
```

### Common Mistakes
- Not calling `st.rerun()` after step change
- Losing form data between steps (not storing in session_state)
- Showing all steps at once instead of one at a time

### Grading Notes (25 marks)
- Full marks: 3-step wizard with navigation, data persistence, submit
- 18 marks: Steps work but data loss between steps
- 10 marks: Steps visible but navigation broken

---

## Challenge 3: Undo/Redo Text Editor

### Expected Approach
Three stacks: `text_content`, `undo_stack`, `redo_stack`. "Save Snapshot" pushes to undo, clears redo. Undo pops undo, pushes current to redo.

### Key Code
```python
if "text_content" not in st.session_state:
    st.session_state.text_content = ""
    st.session_state.undo_stack = []
    st.session_state.redo_stack = []

st.session_state.text_content = st.text_area(
    "Edit text", value=st.session_state.text_content, height=200
)

if st.button("Save Snapshot"):
    st.session_state.undo_stack.append(st.session_state.text_content)
    st.session_state.redo_stack.clear()
    st.success("Snapshot saved")

col1, col2, col3 = st.columns(3)
with col1:
    if st.button("Undo"):
        if st.session_state.undo_stack:
            st.session_state.redo_stack.append(st.session_state.text_content)
            st.session_state.text_content = st.session_state.undo_stack.pop()
            st.rerun()
        else:
            st.warning("Nothing to undo")

with col2:
    if st.button("Redo"):
        if st.session_state.redo_stack:
            st.session_state.undo_stack.append(st.session_state.text_content)
            st.session_state.text_content = st.session_state.redo_stack.pop()
            st.rerun()
        else:
            st.warning("Nothing to redo")

with col3:
    if st.button("Clear All"):
        st.session_state.text_content = ""
        st.session_state.undo_stack.clear()
        st.session_state.redo_stack.clear()
        st.rerun()

st.write(f"Undo steps: {len(st.session_state.undo_stack)} · Redo steps: {len(st.session_state.redo_stack)}")
```

### Grading Notes (25 marks)
- Full marks: Undo, redo, save snapshot, clear all work correctly
- 18 marks: Undo/redo work, snapshot or clear has issues
- 10 marks: Basic editing works but stacks broken

---

## Challenge 4: Shopping Cart

### Expected Approach
Cart stored as list of dicts in session_state. Product selectbox + quantity input + add button. Display cart with remove buttons and total.

### Key Code
```python
if "cart" not in st.session_state:
    st.session_state.cart = []

products = {"Apple": 1.50, "Banana": 0.75, "Orange": 1.00, "Grapes": 2.50}

product = st.selectbox("Product", list(products.keys()))
qty = st.number_input("Quantity", 1, 20, 1)

if st.button("Add to Cart"):
    # Check if already in cart
    for item in st.session_state.cart:
        if item["name"] == product:
            item["quantity"] += qty
            break
    else:
        st.session_state.cart.append({"name": product, "price": products[product], "quantity": qty})
    st.success(f"Added {qty}x {product}")

if st.session_state.cart:
    total = sum(item["price"] * item["quantity"] for item in st.session_state.cart)
    st.metric("Cart Total", f"${total:.2f}")

    for i, item in enumerate(st.session_state.cart):
        col1, col2, col3 = st.columns([3, 1, 1])
        with col1:
            st.write(f"{item['name']} × {item['quantity']} = ${item['price'] * item['quantity']:.2f}")
        with col2:
            if st.button("➖", key=f"dec_{i}"):
                if item["quantity"] > 1:
                    item["quantity"] -= 1
                else:
                    st.session_state.cart.pop(i)
                st.rerun()
        with col3:
            if st.button("➕", key=f"inc_{i}"):
                item["quantity"] += 1
                st.rerun()
```

### Common Mistakes
- Not using unique keys for buttons in a loop
- Not updating existing items (adding duplicates)
- Forgetting to handle empty cart state

### Grading Notes (25 marks)
- Full marks: Add, remove, increment, total all work
- 18 marks: Add and total work, increment/decrement partial
- 10 marks: Basic add works

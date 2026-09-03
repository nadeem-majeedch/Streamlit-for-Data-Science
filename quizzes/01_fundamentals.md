# Quiz 01 — Streamlit Fundamentals

> **📝 Post-Quiz · Module 01 · Beginner**
> *Test your understanding of Streamlit basics, text elements, and app structure.*
> ⏱ Time: 10 minutes · 📊 Points: 20 · Bloom's: Remember, Understand

---

## Part A: Multiple Choice (2 points each)

### Q1. What is the first Streamlit call that must appear in your script?

(a) `st.title()`
(b) `st.write()`
(c) `st.set_page_config()`
(d) `import streamlit`

**CLO:** CLO1

---

### Q2. How do you run a Streamlit app from the terminal?

(a) `python app.py`
(b) `streamlit run app.py`
(c) `streamlit start app.py`
(d) `run streamlit app.py`

**CLO:** CLO1

---

### Q3. What does `st.write("Hello", "World")` display?

(a) Two separate lines
(b) "Hello World" on one line
(c) A tuple `("Hello", "World")`
(d) An error

**CLO:** CLO1

---

### Q4. Which function renders a LaTeX formula?

(a) `st.latex()`
(b) `st.math()`
(c) `st.formula()`
(d) `st.equation()`

**CLO:** CLO1

---

### Q5. What happens when you modify a `.py` file while `streamlit run` is active?

(a) Nothing — you must restart manually
(b) The app automatically reruns
(c) The browser refreshes
(d) You get an error

**CLO:** CLO1

---

## Part B: Multiple Select (2 points each)

### Q6. Which of these are valid Streamlit text elements? (Select all that apply)

(a) `st.title()`
(b) `st.header()`
(c) `st.text()`
(d) `st.heading()`
(e) `st.caption()`
(f) `st.label()`

**CLO:** CLO1

---

## Part C: True/False (1 point each)

### Q7. `st.markdown()` supports bold text using `**bold**` syntax.

**CLO:** CLO1

---

### Q8. `st.code()` automatically syntax-highlights Python code.

**CLO:** CLO1

---

## Part D: Short Answer (3 points each)

### Q9. Explain what happens when a user clicks a button in a Streamlit app. What is the "rerun" model?

**CLO:** CLO1

---

### Q10. A student writes this code and reports that the title appears below the data:

```python
import streamlit as st
import pandas as pd

df = pd.DataFrame({"A": [1, 2, 3]})
st.dataframe(df)
st.title("My Dashboard")
```

What is wrong and how do you fix it?

**CLO:** CLO1, CLO2

---

## Answer Key

> ⚠️ **Instructor copy**

| Q | Answer | Explanation | Bloom's |
|---|--------|-------------|---------|
| Q1 | **(c) `st.set_page_config()`** | Must be the first Streamlit call; raises exception otherwise. | Remember |
| Q2 | **(b) `streamlit run app.py`** | The `run` subcommand starts the development server. | Remember |
| Q3 | **(b) "Hello World" on one line** | `st.write` concatenates multiple arguments with spaces. | Understand |
| Q4 | **(a) `st.latex()`** | Renders LaTeX math expressions. | Remember |
| Q5 | **(b) The app automatically reruns** | Streamlit watches for file changes and reruns the script. | Understand |
| Q6 | **(a), (b), (c), (e)** | `st.heading()` and `st.label()` are not Streamlit functions. | Remember |
| Q7 | **True** | Markdown syntax `**text**` renders as bold. | Remember |
| Q8 | **True** | `st.code()` detects language and applies syntax highlighting. | Remember |
| Q9 | When a button is clicked, Streamlit reruns the entire script from top to bottom. The button returns `True` only during the rerun triggered by the click. This is the "rerun model" — the script is the rendering logic, not a persistent loop. | Understand |
| Q10 | The code works correctly — Streamlit renders elements top-to-bottom as they appear in the script. The issue is ordering: `st.dataframe()` is called before `st.title()`. Fix: move `st.title()` before `st.dataframe()`. Streamlit does NOT auto-order elements. | Understand |

---

## CLO Mapping

| CLO | Questions |
|-----|-----------|
| CLO1 — Explain Streamlit core concepts | Q1–Q10 |
| CLO2 — Build interactive applications | Q10 |

---

## Related Materials

- 📖 Reading: [Streamlit Introduction](../readings/01_streamlit_introduction.md)
- 📖 Reading: [First Streamlit App](../readings/02_first_streamlit_app.md)
- 📓 Notebook: [01 — Introduction](../notebooks/01_Streamlit_Introduction.ipynb)
- ✏️ Exercise: [01 — Hello Streamlit](../exercises/01_hello_streamlit.py)

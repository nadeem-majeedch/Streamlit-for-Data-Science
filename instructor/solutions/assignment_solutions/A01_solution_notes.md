# A01 — Personal Dashboard: Solution Notes

> **👩‍🏫 Instructor Reference**
> *Architecture, key implementation, grading breakdown, and common errors.*

---

## Expected Architecture

```
A01_yourname.py          # Single-file app (acceptable for beginner level)
README.md                # Documentation with screenshots
screenshots/
  ├── dashboard_1.png
  └── dashboard_2.png
```

For a beginner assignment, a single well-organized file is acceptable. Multi-file is bonus.

---

## Expected Approach

### Task 1: Profile Section (15 marks)

**What to look for:**
- `st.title()` with student name
- `st.markdown()` with bold/italic text
- `st.image()` or emoji as avatar
- `st.code()` with a Python snippet
- Contact info in columns or `st.write()`
- `st.latex()` with any valid formula
- `st.caption()` with today's date
- 2+ additional text elements

**Sample code a strong student might write:**
```python
st.title("Jane Smith's Dashboard")
st.markdown("*Data Science Student at University*")
st.markdown("**Python enthusiast** · **ML learner** · **Streamlit fan**")
st.image("https://via.placeholder.com/150", width=150)
st.code('import streamlit as st\nst.write("Hello!")', language="python")

col1, col2 = st.columns(2)
with col1:
    st.write("**Email:** jane@university.edu")
with col2:
    st.write("**GitHub:** github.com/janesmith")

st.latex(r"y = mx + b")
st.caption(f"Last updated: {date.today()}")
```

**Common deductions:**
- (-2) Missing `st.latex()`
- (-2) No bold/italic in markdown
- (-1) Missing caption with date

---

### Task 2: Interactive Widgets (15 marks)

**What to look for:**
- 5 different widget types in sidebar
- Each widget connected to visible behavior
- Clear labels and defaults

**Common deductions:**
- (-2) Widgets not in sidebar
- (-3) Widgets not connected to any behavior
- (-2) Missing labels or poor defaults

---

### Task 3: Data Display (20 marks)

**What to look for:**
- DataFrame with 5+ rows, 4+ columns
- Both `st.dataframe()` and `st.table()` used
- 3+ metric cards
- Data changes based on widget selection
- Meaningful data (not just random numbers)

**Common deductions:**
- (-4) No metrics
- (-3) Data doesn't change with widgets
- (-2) Data is meaningless random numbers

---

### Task 4: Layout & Structure (20 marks)

**What to look for:**
- `st.columns()` for side-by-side content
- `st.tabs()` or `st.expander()`
- Sidebar separates controls from content
- `st.divider()` between sections
- `st.set_page_config()` as first call

**Common deductions:**
- (-2) Missing `st.set_page_config()` as first call
- (-3) No column layout
- (-2) No tabs or expanders

---

### Task 5: Code Quality (10 marks)

**What to look for:**
- Functions for repeated logic
- Comments on non-obvious code
- PEP 8 naming conventions
- No magic numbers

---

### Task 6: Creativity & Polish (10 marks)

**Subjective — look for:**
- Custom theme or consistent color scheme
- Emoji usage that enhances UX
- At least one element that surprised you
- Professional overall appearance

---

### Task 7: Documentation (10 marks)

**What to look for:**
- Title and clear description
- At least 2 screenshots
- Feature list
- Run instructions
- What they learned

---

## Alternative Valid Approaches

1. **Data source:** Students may use any data — generated, from an API, or hardcoded
2. **Widget combinations:** Any mix of 5+ sidebar widgets is acceptable
3. **Layout:** Tabs, expanders, or columns — all valid
4. **Creativity:** Many valid approaches to "surprise and delight"

---

## Grading Strategy

1. Run the app first — does it work without errors?
2. Check each task systematically against the rubric
3. Test widget interactions — do they affect the display?
4. Read README — is it complete?
5. Award partial credit generously for attempts

**Estimated grading time:** 5-8 minutes per student

---

## Common Class-Wide Issues

After grading all submissions, prepare feedback on:
1. Most common missing element
2. Best creative approaches to share as examples
3. Code quality patterns to address in class

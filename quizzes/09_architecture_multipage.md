# Quiz 09: Architecture & Multipage Apps

> **📝 Quiz · Module 09 · Advanced**  
> *Test your understanding of Streamlit application architecture and multipage apps.*

---

## Multiple Choice

### Q1. What is the recommended approach for creating multipage Streamlit apps?

a) Using multiple `st.set_page_config()` calls  
b) Using `st.navigation` and `st.Page`  
c) Using if/else statements to show different content  
d) Using separate Streamlit processes

---

### Q2. What does `st.Page` do?

a) Configures the entire app's navigation  
b) Initializes a page object for use with `st.navigation`  
c) Creates a new browser tab  
d) Saves the current page state

---

### Q3. How do you execute the selected page in a multipage app?

a) `st.run()`  
b) `pg.run()`  
c) `st.page.run()`  
d) Pages execute automatically

---

### Q4. What is the entry point file's role in a multipage app using `st.navigation`?

a) It's just the home page  
b) It acts as a router and shared frame for all pages  
c) It only contains configuration  
d) It's optional

---

### Q5. How do you create grouped navigation sections?

```python
# Option A
pg = st.navigation([
    st.Page("page1.py"),
    st.Page("page2.py")
])

# Option B
pg = st.navigation({
    "Section 1": [st.Page("page1.py")],
    "Section 2": [st.Page("page2.py")]
})
```

---

### Q6. What is the recommended file structure for a medium-sized Streamlit app (300-1000 lines)?

a) Everything in `app.py`  
b) `app.py` + `pages/` directory + `utils/` directory  
c) Just `pages/` directory  
d) Multiple entry points

---

### Q7. Where should business logic be placed?

a) Inside UI callbacks (button clicks)  
b) In separate functions or modules  
c) In `st.session_state`  
d) In the `pages/` directory only

---

### Q8. What is the benefit of a `config.py` module?

a) It makes the app run faster  
b) It centralizes settings and constants  
c) It's required by Streamlit  
d) It replaces `st.set_page_config()`

---

### Q9. How should you import from utility modules?

```python
# Option A
from utils.helpers import *

# Option B
from utils.helpers import format_currency, validate_email

# Option C
import utils.helpers

# Option D
exec(open("utils/helpers.py").read())
```

---

### Q10. When should you refactor a single-file app into multiple modules?

a) Never — single files are always better  
b) When the app exceeds ~300-500 lines  
c) Only when working with a team  
d) Only for production apps

---

### Q11. What is the correct naming convention for a page file?

a) `Page1.py`  
b) `page1.py` or `01_page_name.py`  
c) `PAGE_1.PY`  
d) `mypage.PY`

---

### Q12. How do you share widgets across pages in a multipage app?

a) You can't — each page is independent  
b) Define widgets in the entry point file with keys  
c) Use `st.cache_data` for widget state  
d) Copy widget code to each page

---

## Short Answer

### Q13. Explain the concept of "separation of concerns" in Streamlit applications. What are the three main layers and why is separation important?

---

### Q14. Compare the `pages/` directory approach vs. `st.navigation` approach for multipage apps. When would you use each?

---

### Q15. A developer has a 1500-line `app.py` file with data loading, business logic, and UI all mixed together. Describe how you would refactor this into a maintainable structure.

---

## Code Completion

### Q16. Complete the multipage navigation setup:

```python
import streamlit as st

# TODO: Define pages with icons and titles
pages = {
    "Data": [
        # TODO: Add Home page
        # TODO: Add Explore page
    ],
    "Analysis": [
        # TODO: Add Statistics page
        # TODO: Add Reports page
    ]
}

# TODO: Create navigation
# pg = st.navigation(...)

# TODO: Run the selected page
# pg.run()
```

---

### Q17. Complete the reusable component:

```python
import streamlit as st

def metric_card(label, value, delta=None, delta_color="normal"):
    """
    Render a consistent metric card.
    
    Args:
        label: Metric label
        value: Metric value
        delta: Optional change indicator
        delta_color: "normal" or "inverse"
    """
    # TODO: Implement the metric card
    pass

# Usage
# metric_card("Revenue", "$1.2M", "+12%")
```

---

## Answer Key

### Multiple Choice

1. **B** - `st.navigation` and `st.Page` is the preferred and most flexible approach
2. **B** - `st.Page` initializes a page object for use with `st.navigation`
3. **B** - Call `.run()` on the page object returned by `st.navigation`
4. **B** - Entry point acts as router and shared frame (header, footer, sidebar widgets)
5. **B** - Dictionary with section labels as keys and lists of pages as values
6. **B** - Separate files for entry point, pages, and utilities
7. **B** - Business logic should be in separate functions, not mixed with UI
8. **B** - Config centralizes settings — change once, update everywhere
9. **B** - Explicit imports only — no star imports
10. **B** - Refactor when code becomes hard to navigate (300-500 lines)
11. **B** - Lowercase with underscores or numbered prefix
12. **B** - Define shared widgets in entry point with session state keys

### Short Answer

**Q13.** Separation of concerns means dividing code into distinct sections, each with a single responsibility:
- **UI Layer:** Display elements, user interaction
- **Data Layer:** Loading, processing, transformation
- **Business Logic:** Rules, calculations, validation

This makes code easier to test, maintain, and understand. Changes to one layer don't affect others.

**Q14.** 
- **pages/ directory:** Simple, automatic navigation. Good for quick prototypes or simple apps. Limited customization.
- **st.navigation:** More flexible, explicit control. Supports grouped navigation, custom titles/icons, dynamic navigation. Recommended for production apps.

Use `pages/` for simple apps, `st.navigation` for complex or production apps.

**Q15.** Refactoring steps:
1. Create `config.py` for all settings/constants
2. Create `data_loader.py` for data functions
3. Create `components.py` for reusable UI
4. Create `utils/helpers.py` for business logic
5. Create `pages/` directory with individual pages
6. Slim down `app.py` to just entry point and navigation

### Code Completion

**Q16.**
```python
pages = {
    "Data": [
        st.Page("pages/home.py", title="Home", icon="🏠"),
        st.Page("pages/explore.py", title="Explore", icon="📊"),
    ],
    "Analysis": [
        st.Page("pages/statistics.py", title="Statistics", icon="📈"),
        st.Page("pages/reports.py", title="Reports", icon="📄"),
    ]
}

pg = st.navigation(pages)
pg.run()
```

**Q17.**
```python
def metric_card(label, value, delta=None, delta_color="normal"):
    """Render a consistent metric card."""
    st.metric(
        label=label,
        value=value,
        delta=delta,
        delta_color=delta_color
    )
```

---

## Related Materials

- 📖 Reading: [13 — Application Architecture](../readings/13_application_architecture.md)
- 📓 Notebook: [13 — Application Architecture](../notebooks/13_application_architecture.ipynb)
- ✏️ Exercise: [13 — Architecture Workshop](../exercises/13_architecture_workshop.py)
- 🖥️ Demo App: [13 — Modular App](../apps/13_modular_app/app.py)

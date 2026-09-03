# 📝 Solution Guide

> **Streamlit for Data Science — Learn, Build, Deploy**
> *Walkthrough of all exercise and assignment solutions.*

---

## How to Use This Guide

This document provides a **high-level walkthrough** of each solution. For the actual code, see `solutions/`.

### Before Grading
1. Run each solution yourself to verify it works
2. Note the key implementation points listed below
3. Review the "alternative approaches" section
4. Check the "common student mistakes" in `common_student_mistakes.md`

### During Grading
1. Compare student code against the expected approach
2. Award credit for alternative valid approaches (listed below)
3. Use the partial credit guidelines for incomplete work

---

## Exercise Solutions

### Exercise 01 — Hello Streamlit (M01)
**File:** `solutions/exercises_solutions/01_hello_streamlit_solution.py`
**Difficulty:** ★☆☆☆☆

**Expected approach:**
1. `st.set_page_config()` at top
2. `st.title()`, `st.header()`, `st.subheader()`, `st.caption()`, `st.markdown()`
3. Create a Pandas DataFrame and display with `st.dataframe()`
4. Combine into a mini report card

**Alternative approaches:**
- Using `st.write()` instead of specific text elements (acceptable but less clean)
- Using `st.metric()` for report card values

**Partial credit:**
- 50%: At least 3 text elements work
- 75%: DataFrame displays correctly
- 100%: All elements present and report card is complete

---

### Exercise 03 — Widget Mastery (M02)
**File:** `solutions/exercises_solutions/03_widget_mastery_solution.py`
**Difficulty:** ★★☆☆☆

**Expected approach:**
1. Each widget type in its own section
2. Return values captured and displayed
3. At minimum: button, checkbox, slider, selectbox, text_input, number_input, radio
4. Registration form combining multiple widgets

**Alternative approaches:**
- Using `st.form()` for the registration form (preferred but not required)
- Adding widgets beyond the required set (bonus credit)

**Partial credit:**
- 50%: At least 4 widget types used correctly
- 75%: 6+ widget types with return values displayed
- 100%: All required widgets + working registration form

---

### Exercise 04 — Dataset Filter (M02)
**File:** `solutions/exercises_solutions/04_dataset_filter_solution.py`
**Difficulty:** ★★☆☆☆

**Expected approach:**
1. Load a dataset (Iris or similar)
2. Sidebar with filter widgets (selectbox, slider, checkbox)
3. Filters connected to DataFrame display
4. Summary statistics shown

**Key implementation point:** Filters must actually filter the data — not just exist as widgets.

---

### Exercise 05 — Layout Basics (M03)
**File:** `solutions/exercises_solutions/05_layout_basics_solution.py`
**Difficulty:** ★★☆☆☆

**Expected approach:**
1. Sidebar with at least 2 widgets
2. 2+ columns with content
3. At least 1 tab with different views
4. At least 1 expander with details

---

### Exercise 06 — Dashboard Builder (M03)
**File:** `solutions/exercises_solutions/06_dashboard_builder_solution.py`
**Difficulty:** ★★★☆☆

**Expected approach:**
1. Complete dashboard with sidebar, columns, tabs
2. KPI metrics at the top
3. Charts in the main area
4. Data table in a tab
5. Self-contained and runnable

---

### Exercise 07 — Data Display (M04)
**File:** `solutions/exercise_notes/07_data_display_notes.md`
**Difficulty:** ★★☆☆☆

**Expected approach:**
1. `st.dataframe()` with `column_config` for interactive display
2. `st.table()` for a small summary
3. Pandas Styler for formatted output
4. Dynamic column selection

**Key concept:** `st.dataframe` is interactive (sort, filter), `st.table` is static HTML.

---

### Exercise 08 — Visualization (M04)
**File:** `solutions/exercise_notes/08_visualization_notes.md`
**Difficulty:** ★★★☆☆

**Expected approach:**
1. At least 3 different chart types (bar, line, scatter, histogram)
2. User can select columns to plot
3. Matplotlib and/or Plotly integration
4. Proper labels and titles

**Key concept:** Chart selection matters — justify why each chart type is appropriate.

---

### Exercise 09 — File Upload (M06)
**File:** `solutions/exercise_notes/09_file_upload_notes.md`
**Difficulty:** ★★★☆☆

**Expected approach:**
1. File upload with type validation
2. Read CSV, Excel, or JSON
3. Display shape, columns, dtypes
4. Data quality summary (missing values, types)
5. Error handling for invalid files

---

### Exercise 09 — API Connectors (M09)
**File:** `solutions/exercises_solutions/09_api_connectors_solution.py`
**Difficulty:** ★★★☆☆

**Expected approach:**
1. Fetch data from a public API (e.g., JSONPlaceholder)
2. Parse JSON response into DataFrame
3. Handle API errors gracefully
4. Cache the API response
5. Display in a clean format

---

### Exercise 10 — Dashboard Workshop (M06)
**File:** `solutions/exercise_notes/10_dashboard_workshop_notes.md`
**Difficulty:** ★★★★☆

**Expected approach:**
1. File upload + dynamic filters
2. 3+ chart types
3. KPI metrics
4. Session state for filter persistence
5. Download button
6. Functions for data processing (not all inline)

---

### Exercise 11 — State Management (M07)
**File:** `solutions/exercise_notes/11_state_management_notes.md`
**Difficulty:** ★★★☆☆

**Expected approach:**
1. Counter using session_state
2. Multi-step wizard with state tracking
3. Undo/redo or comparison feature
4. Reset functionality

**Key concept:** Session state is per-session and persists across reruns.

---

### Exercise 12 — Caching (M07)
**File:** `solutions/exercise_notes/12_caching_notes.md`
**Difficulty:** ★★★★☆

**Expected approach:**
1. `@st.cache_data` for DataFrames and computations
2. `@st.cache_resource` for models and connections
3. TTL for time-sensitive data
4. Performance measurement (before/after)

---

### Exercise 13 — Architecture (M08)
**File:** `solutions/exercise_notes/13_architecture_notes.md`
**Difficulty:** ★★★★☆

**Expected approach:**
1. Refactored into multiple files
2. Shared utilities module
3. Clean separation: UI, data, logic
4. Multipage navigation

---

### Exercise 14 — Database (M10)
**File:** `solutions/exercise_notes/14_database_notes.md`
**Difficulty:** ★★★★☆

**Expected approach:**
1. SQLite connection with context manager
2. CRUD operations
3. Parameterized queries (NO SQL injection)
4. Error handling for database operations
5. Cache the connection or queries

---

### Exercise 15 — ML Workshop (M12)
**File:** `solutions/exercise_notes/15_ml_notes.md`
**Difficulty:** ★★★★☆

**Expected approach:**
1. Model saved with joblib
2. Loaded with `@st.cache_resource`
3. Input validation for all features
4. Prediction + probability display
5. Batch prediction option

---

### Exercise 16 — Production Ready (M16)
**File:** `solutions/exercises_solutions/16_production_ready_solution.py`
**Difficulty:** ★★★★☆

**Expected approach:**
1. Structured logging with Python logging module
2. Error handling patterns (try/except with specific exceptions)
3. Health check endpoint
4. Configuration management
5. Graceful degradation

---

### Exercise 17 — NLP Workshop (M13)
**File:** `solutions/exercise_notes/17_nlp_notes.md`
**Difficulty:** ★★★★☆

**Expected approach:**
1. Text preprocessing pipeline
2. TF-IDF vectorization
3. Model training and prediction
4. Confidence display
5. Batch text prediction

---

### Exercise 18 — LLM Workshop (M14)
**File:** `solutions/exercise_notes/18_llm_notes.md`
**Difficulty:** ★★★★★

**Expected approach:**
1. Chat interface with `st.chat_message`
2. API key via `st.secrets`
3. Conversation history in session state
4. Provider abstraction (openai/local)
5. Error handling for API failures

---

## Assignment Solutions

### A01 — Personal Dashboard
**File:** `solutions/assignment_solutions/A01_solution_notes.md`
**Weight:** 4%

**Expected structure:**
```
a01_dashboard/
├── app.py           # Main app with navigation
├── requirements.txt # streamlit, pandas, plotly
└── README.md        # Setup instructions
```

**Key grading focus:** Does the app work? Is the layout clean? Are widgets connected to data?

---

### A02 — Data Explorer
**File:** `solutions/assignment_solutions/A02_solution_notes.md`
**Weight:** 4%

**Expected structure:**
```
a02_explorer/
├── app.py           # File upload + filters + charts
├── utils.py         # Data processing functions
├── requirements.txt
└── README.md
```

**Key grading focus:** Does it work with ANY CSV file? Are filters dynamic?

---

### A03 — Multipage Application
**File:** `solutions/assignment_solutions/A03_solution_notes.md`
**Weight:** 4%

**Expected structure:**
```
a03_multipage/
├── app.py           # Navigation
├── config.py        # Settings
├── utils/
│   ├── data.py      # Data access
│   └── ui.py        # Shared UI components
├── pages/
│   ├── 1_📊_Home.py
│   ├── 2_📈_Analysis.py
│   └── 3_⚙️_Settings.py
├── requirements.txt
└── README.md
```

**Key grading focus:** Is the architecture clean? Is code modular?

---

### A04 — ML Production App
**File:** `solutions/assignment_solutions/A04_solution_notes.md`
**Weight:** 8%

**Expected structure:**
```
a04_ml_app/
├── app.py           # Main app
├── config.py        # Model paths, feature names
├── model_utils.py   # Train, load, predict
├── data_processing.py  # Preprocessing pipeline
├── security.py      # Input validation
├── tests/
│   ├── test_model.py
│   └── test_app.py
├── models/
│   └── model.joblib
├── requirements.txt
├── .streamlit/
│   └── config.toml
├── .gitignore
└── README.md
```

**Key grading focus:** Does it deploy and work in production? Is preprocessing consistent?

---

## Grading Consistency Checklist

Before returning graded work, verify:

- [ ] All students received the same rubric
- [ ] Partial credit is consistent across submissions
- [ ] Feedback is specific (not just "good job" or "needs work")
- [ ] Point deductions match the stated policy
- [ ] Alternative valid approaches are credited
- [ ] Academic integrity concerns are noted

---

## Related Materials

- [Exercise Guide](exercise_guide.md) — Detailed per-exercise grading notes
- [Common Mistakes](common_student_mistakes.md) — Error patterns
- [Solutions Index](solutions/README.md) — File listing
- [Assessment Strategy](assessment_strategy.md) — Overall grading policy

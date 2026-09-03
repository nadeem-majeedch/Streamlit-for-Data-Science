# Instructor Exercise & Assignment Guide

> **👩‍🏫 Instructor Reference — Grading Guide**
> *Expected solutions, common issues, and grading notes for all exercises and assignments.*

---

## Exercise Overview

| # | Exercise | Module | Level | Difficulty | Key Concepts |
|---|----------|--------|-------|------------|--------------|
| 01 | Hello Streamlit | M01 | Beginner | ★☆☆☆☆ | Text elements, data display, app structure |
| 03 | Widget Mastery | M02 | Beginner | ★★☆☆☆ | All widget types, return values, interaction |
| 04 | Dataset Filter | M02 | Beginner | ★★☆☆☆ | Sidebar filters, DataFrame display |
| 05 | Layout Basics | M03 | Beginner | ★★☆☆☆ | Sidebar, columns, tabs, expanders |
| 06 | Dashboard Builder | M03 | Beginner | ★★★☆☆ | Complete dashboard layout |
| 07 | Data Display | M04 | Intermediate | ★★☆☆☆ | DataFrame, column_config, Styler |
| 08 | Visualization | M04 | Intermediate | ★★★☆☆ | Chart selection, Matplotlib, Plotly |
| 09 | API Connectors | M09 | Advanced | ★★★☆☆ | REST API, JSON parsing, caching |
| 09 | File Upload | M06 | Intermediate | ★★★☆☆ | File handling, validation, cleaning |
| 10 | Dashboard Workshop | M06 | Intermediate | ★★★★☆ | Complete interactive dashboard |
| 11 | State Management | M07 | Advanced | ★★★☆☆ | Session state, multi-step workflows |
| 12 | Caching | M07 | Advanced | ★★★★☆ | cache_data, cache_resource, TTL |
| 13 | Architecture | M08 | Advanced | ★★★★☆ | Multipage, modules, separation of concerns |
| 14 | Database | M10 | Advanced | ★★★★☆ | SQLite, CRUD, parameterized queries |
| 15 | ML Workshop | M12 | Advanced | ★★★★☆ | Model deployment, preprocessing |
| 16 | Production Ready | M16 | Production | ★★★★☆ | Error handling, logging, monitoring |
| 17 | NLP Workshop | M13 | Advanced | ★★★★☆ | Text classification, TF-IDF |
| 18 | LLM Workshop | M14 | Advanced | ★★★★★ | LLM providers, RAG, security |
| — | Security Exercises | M14 | Advanced | ★★★★☆ | Secrets, SQL injection, file security |
| — | Deployment Exercises | M15 | Deployment | ★★★☆☆ | Deployment prep, debugging |

---

## Assignment Overview

| # | Assignment | Modules | Weight | Difficulty | Submission |
|---|-----------|---------|--------|------------|------------|
| A01 | Personal Dashboard | M01–M03 | 4% | ★☆☆☆☆ | Individual |
| A02 | Data Explorer | M04–M06 | 4% | ★★☆☆☆ | Individual |
| A03 | Multipage App | M07–M10 | 4% | ★★★☆☆ | Individual/Pair |
| A04 | ML Production App | M11–M16 | 8% | ★★★★☆ | Individual |

---

## Grading Notes by Exercise

### Exercise 01 — Hello Streamlit
- **Common issue:** Students forget `st.set_page_config()` as first call
- **Grade easily:** Text elements are pass/fail — either present or missing
- **Watch for:** Students copying from notebook instead of writing independently

### Exercise 03 — Widget Mastery
- **Common issue:** Using `key` parameter incorrectly
- **Key concept:** Each widget returns its current value
- **Grade easily:** Count widget types used — need all core types

### Exercise 04 — Dataset Filter
- **Common issue:** Filters not connected to DataFrame display
- **Key concept:** Widget return values must be used to filter data
- **Award partial credit:** For working filters even if UI is rough

### Exercise 05 — Layout Basics
- **Common issue:** Sidebar widgets mixed with main area widgets
- **Key concept:** Sidebar is separate from main content area
- **Award partial credit:** For using at least 2 layout elements correctly

### Exercise 06 — Dashboard Builder
- **Common issue:** No error handling for empty data
- **Key concept:** Dashboard must be self-contained and runnable
- **Grade holistically:** Overall appearance and completeness

### Exercise 07 — Data Display
- **Common issue:** Using `st.table()` when `st.dataframe()` is needed (or vice versa)
- **Key concept:** `st.dataframe` is interactive, `st.table` is static

### Exercise 08 — Visualization
- **Common issue:** Wrong chart type for data (pie chart for time series)
- **Key concept:** Chart selection matters — justify choices
- **Award creativity points:** For unexpected but appropriate visualizations

### Exercise 09 — API Connectors
- **Common issue:** No error handling for failed API calls
- **Key concept:** Always handle network failures gracefully
- **Award partial credit:** For working fetch even without caching

### Exercise 09 — File Upload
- **Common issue:** No file type validation
- **Key concept:** Always validate before processing

### Exercise 10 — Dashboard Workshop
- **Common issue:** All code in one file with no functions
- **Key concept:** Modular code structure matters at this level
- **Grade holistically:** Architecture + functionality combined

### Exercise 11 — State Management
- **Common issue:** Using global variables instead of session_state
- **Key concept:** session_state is per-session, not global

### Exercise 12 — Caching
- **Common issue:** Using `cache_data` for models, `cache_resource` for DataFrames
- **Key concept:** `cache_data` = copies, `cache_resource` = singletons

### Exercise 13 — Architecture
- **Common issue:** Tight coupling between pages
- **Key concept:** Shared logic in modules, not duplicated across pages

### Exercise 14 — Database
- **Common issue:** SQL injection with f-strings
- **Key concept:** ALWAYS use parameterized queries

### Exercise 15 — ML Workshop
- **Common issue:** Training model on every Streamlit rerun
- **Key concept:** Train once, save, load with caching

### Exercise 16 — Production Ready
- **Common issue:** No actual logging implementation
- **Key concept:** Production apps need monitoring

### Exercise 17 — NLP Workshop
- **Common issue:** Preprocessing mismatch between training and inference
- **Key concept:** Same preprocessing function for both

### Exercise 18 — LLM Workshop
- **Common issue:** Hardcoded API keys
- **Key concept:** ALWAYS use st.secrets

### Security Exercises
- **Common issue:** Students treat security as optional
- **Key concept:** Security is a requirement, not a nice-to-have

### Deployment Exercises
- **Common issue:** Missing requirements.txt
- **Key concept:** Community Cloud REQUIRES requirements.txt

---

## Grading Notes by Assignment

### A01 — Personal Dashboard (100 marks, 4%)

**Grade distribution expectation:**
- A (90–100): Full functionality, creative design, clean code
- B (80–89): All core features, acceptable design
- C (70–79): Most features working, basic design
- D (60–69): Some features, incomplete
- F (<60): Non-functional or not submitted

**Common deductions:**
- (-5) Missing `st.set_page_config()`
- (-5) No sidebar
- (-3) Widgets not connected to app behavior
- (-5) All code in one long script with no functions
- (-10) Copied from notebook verbatim

### A02 — Data Explorer (100 marks, 4%)

**Key grading focus:** Does the app work with ANY CSV file?

**Common deductions:**
- (-5) Hardcoded column names that break with different data
- (-5) No file type validation
- (-5) Charts don't update with filters
- (-3) No session state
- (-5) Missing download button

### A03 — Multipage Application (100 marks, 4%)

**Key grading focus:** Is the architecture clean and modular?

**Common deductions:**
- (-10) All code in one file
- (-5) SQL injection vulnerabilities
- (-5) No cache invalidation after writes
- (-5) Database queries in page files
- (-3) Missing error handling

### A04 — ML Production App (100 marks, 8%)

**Key grading focus:** Does it deploy and work in production?

**Common deductions:**
- (-10) Not deployed to Community Cloud
- (-5) Preprocessing mismatch
- (-10) Hardcoded secrets
- (-5) No tests
- (-5) Model trained on every rerun
- (-5) Missing requirements.txt

---

## Solution Architecture Notes

### Exercise 01 Expected Structure
```python
# Part 1: Text elements (straightforward)
# Part 2: DataFrame creation and display
# Part 3: Mini report card combining all skills
# Part 4-5: Theory questions (no code)
```

### Exercise 03 Expected Structure
```python
# Each widget type in its own section
# Return values used in st.write() to demonstrate
# At least: button, checkbox, slider, selectbox,
#           text_input, number_input, radio
```

### Exercise 10 Expected Structure
```python
# Functions: load_data(), filter_data(), create_charts(), get_kpis()
# Sidebar with 4+ filters
# 3+ tabs for different views
# Export button
# Session state for filter persistence
```

### A03 Expected Architecture
```python
# app.py: st.navigation() with grouped pages
# config.py: DATABASE_PATH = "experiments.db"
# data_access.py: CRUD functions with parameterized SQL
# components.py: metric_card(), data_preview()
# pages/: home.py, data_entry.py, analysis.py, reports.py
```

### A04 Expected Architecture
```python
# app.py: Navigation + page routing
# config.py: MODEL_PATH, FEATURE_NAMES, CLASS_NAMES
# model_utils.py: train_model(), load_model(), predict()
# data_processing.py: preprocess_input(), validate_features()
# security.py: sanitize_input(), check_file_type()
# tests/: Unit tests + AppTest tests
```

---

## Academic Integrity Notes

- Exercises are intentionally different from notebook examples
- Students must write their own code — not copy from notebooks
- Pair assignments (A03) require both students to contribute
- All code is checked for similarity during grading
- Deployed apps are verified to match submitted code

---

## Related Materials

- 📋 Full Curriculum: [docs/curriculum.md](../docs/curriculum.md)
- 📋 Learning Outcomes: [docs/learning_outcomes.md](../docs/learning_outcomes.md)
- 📋 Course Blueprint: [docs/course_blueprint.md](../docs/course_blueprint.md)

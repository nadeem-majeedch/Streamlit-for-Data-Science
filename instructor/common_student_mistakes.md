# ⚠️ Common Student Mistakes

> **Streamlit for Data Science — Learn, Build, Deploy**
> *Error catalog with causes, fixes, and intervention strategies.*

---

## How to Use This Document

- **During grading:** Quickly identify error patterns and award consistent partial credit
- **During lectures:** Address the top mistakes proactively
- **During office hours:** Guide students to the right section
- **After grading:** Add new patterns you observe

---

## Phase 1 — Foundation (M01–M03)

### M01: Streamlit Fundamentals

#### Mistake: `st.set_page_config()` not called first
**Symptoms:** `StreamlitAPIException: st.set_page_config() can only be called once`
**Cause:** Students put `set_page_config` after other Streamlit commands
**Fix:** Always put `st.set_page_config()` at the top of the file, before any other `st.*` calls
**Intervention:** Make this Rule #1 on Day 1. Show the error message and what causes it.

#### Mistake: Forgetting to save before running
**Symptoms:** App shows old code, student thinks "nothing changed"
**Cause:** Streamlit only reads the file at startup or on save (with `--autoReload`)
**Fix:** Enable `--autoReload 1` or remind students to save
**Intervention:** Show the `.streamlit/config.toml` setting: `server.autoRerun = true`

#### Mistake: Using `print()` instead of `st.write()`
**Symptoms:** Output appears in terminal but not in the browser
**Cause:** Students think Streamlit works like a regular Python script
**Fix:** Replace `print()` with `st.write()` or `st.text()`
**Intervention:** Show side-by-side: `print()` in terminal vs `st.write()` in browser

#### Mistake: Importing Streamlit in wrong namespace
**Symptoms:** `AttributeError: module 'streamlit' has no attribute 'write'`
**Cause:** `import streamlit` without alias, or using `st` without importing
**Fix:** Always use `import streamlit as st`
**Intervention:** Standardize the import convention on Day 1

---

### M02: Widgets & Input

#### Mistake: Not using widget return values
**Symptoms:** Widget appears but doesn't affect anything
**Cause:** Students create widgets but don't capture or use their output
**Fix:** `value = st.slider(...)` then use `value` in subsequent code
**Intervention:** Draw a diagram: Widget → Return Value → Use in Code

#### Mistake: Using `key` as a variable name
**Symptoms:** Confusion about `key` parameter vs. Python variable
**Cause:** Overloading the term "key"
**Fix:** Explain: `key` is Streamlit's internal identifier, not related to your Python variables
**Intervention:** Use different variable names: `my_value = st.slider("Label", key="slider1")`

#### Mistake: Form submission logic inside the form
**Symptoms:** Form doesn't submit properly, or submits on every interaction
**Cause:** Putting `st.form_submit_button` logic in the wrong place
**Fix:** Use `with st.form("my_form"): ... if submitted: ...` pattern
**Intervention:** Show the form pattern explicitly. Draw the flow diagram.

#### Mistake: Selectbox with mutable default
**Symptoms:** `st.selectbox` shows wrong value after rerun
**Cause:** Using a list that changes on every rerun as options
**Fix:** Define options outside the rerun (or use `key` parameter)
**Intervention:** Show the "stable options" pattern

---

### M03: Layouts & Dashboard UI

#### Mistake: Sidebar vs. main area confusion
**Symptoms:** Widgets appear in wrong location
**Cause:** Not using `with st.sidebar:` context manager
**Fix:** Wrap sidebar widgets in `with st.sidebar:`
**Intervention:** Draw the page layout: sidebar | main area

#### Mistake: Columns not sized properly
**Symptoms:** Uneven column widths, content overflowing
**Cause:** Not specifying column widths or using wrong ratio
**Fix:** Use `st.columns([2, 1, 1])` for specific ratios
**Intervention:** Show the ratio system: equal by default, customizable

#### Mistake: Putting everything in one column
**Symptoms:** Long scrolling page, hard to read
**Cause:** Not using layout elements to organize content
**Fix:** Use columns for KPIs, tabs for different views, expanders for details
**Intervention:** Show the "dashboard pattern": metrics → charts → details

---

## Phase 2 — Data & Visualization (M04–M06)

### M04: DataFrames & Visualization

#### Mistake: Using `st.table()` for large datasets
**Symptoms:** Slow rendering, page becomes unresponsive
**Cause:** `st.table` renders all rows as HTML (no virtualization)
**Fix:** Use `st.dataframe()` for interactive display of large data
**Intervention:** Show the performance difference with a 1000-row dataset

#### Mistake: Wrong chart type for data
**Symptoms:** Misleading visualization, stakeholder confusion
**Cause:** Using pie charts for time series, bar charts for distributions
**Fix:** Match chart type to data type and question
**Intervention:** Create a "chart selection guide" handout

#### Mistake: Not labeling axes
**Symptoms:** Charts look nice but are uninterpretable
**Cause:** Forgetting `xlabel`, `ylabel`, or chart titles
**Fix:** Always label axes and add a title
**Intervention:** Make it a checklist item for every chart

#### Mistake: Hardcoded column names
**Symptoms:** App breaks with different datasets
**Cause:** `df["specific_column"]` instead of dynamic selection
**Fix:** Use `st.selectbox("Choose column", df.columns)` for dynamic selection
**Intervention:** Emphasize "apps should work with ANY valid CSV"

---

### M05: Session State & Reruns

#### Mistake: Using global variables for state
**Symptoms:** State resets on every interaction
**Cause:** `count = 0` at module level, then incrementing
**Fix:** Use `st.session_state.count` instead of a plain variable
**Intervention:** This is THE hardest concept. Spend extra time. Draw the execution model.

#### Mistake: Not initializing session state
**Symptoms:** `KeyError` when accessing session state
**Cause:** Accessing `st.session_state.key` before it's set
**Fix:** Check existence: `if "key" not in st.session_state: st.session_state.key = default`
**Intervention:** Provide a boilerplate snippet for initialization

#### Mistake: Forgetting that forms batch submissions
**Symptoms:** Widget inside form doesn't update until submit
**Cause:** Confusion about when form values are available
**Fix:** Explain: form values are only available after `st.form_submit_button` is pressed
**Intervention:** Show the form execution diagram

#### Mistake: Callbacks that modify state the callback is reading
**Symptoms:** Unexpected behavior, values not updating
**Cause:** Callback modifies the same state it's observing
**Fix:** Use `on_change` callbacks carefully; prefer direct state modification
**Intervention:** Keep callbacks simple. If complex, use direct state modification instead.

---

### M06: File Upload & Dashboards

#### Mistake: No file type validation
**Symptoms:** App crashes on non-CSV upload, or processes binary garbage
**Cause:** Not checking `file.type` or extension
**Fix:** Check file type: `if uploaded_file.type == "text/csv":`
**Intervention:** Make validation a mandatory step in every upload exercise

#### Mistake: Reading the entire file into memory
**Symptoms:** App crashes with large files
**Cause:** `pd.read_csv(file)` without size limits
**Fix:** Add file size check: `if file.size > MAX_SIZE: st.error("File too large")`
**Intervention:** Discuss memory limitations in Community Cloud (1GB RAM)

#### Mistake: Download button produces empty file
**Symptoms:** User clicks download, gets empty or corrupt file
**Cause:** Wrong data type passed to `download_button`
**Fix:** Convert to CSV string: `df.to_csv(index=False).encode('utf-8')`
**Intervention:** Show the exact pattern with proper encoding

---

## Phase 3 — Architecture & Performance (M07–M09)

### M07: Caching

#### Mistake: Caching mutable objects incorrectly
**Symptoms:** Cached data changes when source changes
**Cause:** Caching a reference to a mutable object (dict, list)
**Fix:** Use `@st.cache_data` which serializes (copies) the data
**Intervention:** Explain: `cache_data` = copy, `cache_resource` = singleton

#### Mistake: Using `cache_data` for model objects
**Symptoms:** Model behaves unexpectedly after caching
**Cause:** `cache_data` serializes/deserializes models, which may not work
**Fix:** Use `@st.cache_resource` for models and database connections
**Intervention:** Rule of thumb: data → cache_data, objects → cache_resource

#### Mistake: Cache never invalidates
**Symptoms:** App shows stale data even after database update
**Cause:** No TTL or hash_func configured
**Fix:** Add `ttl=3600` (1 hour) or custom hash function
**Intervention:** Discuss cache invalidation strategies

#### Mistake: Forgetting the hash function
**Symptoms:** Cache hit when it should miss
**Cause:** Default hash function doesn't detect input changes
**Fix:** Use `hash_funcs` parameter for custom objects
**Intervention:** Show when default hashing works and when it doesn't

---

### M08: Architecture

#### Mistake: All code in one file
**Symptoms:** `app.py` is 500+ lines, hard to maintain
**Cause:** Starting simple and never refactoring
**Fix:** Extract functions, create modules, use multipage
**Intervention:** The "refactor live" demo is powerful — show pain before solution

#### Mistake: Tight coupling between pages
**Symptoms:** Changing one page breaks another
**Cause:** Pages import from each other or share global state
**Fix:** Shared logic in utils, state in session_state, no circular imports
**Intervention:** Draw the dependency graph for a well-structured app

#### Mistake: Duplicated code across pages
**Symptoms:** Same function defined in 3 different page files
**Cause:** Copy-paste between pages
**Fix:** Extract to shared module, import once
**Intervention:** DRY principle enforcement during code review

---

### M09–M10: APIs & Databases

#### Mistake: No error handling for API calls
**Symptoms:** App crashes when API is down
**Cause:** No try/except around requests
**Fix:** Always wrap API calls in try/except with user-friendly error messages
**Intervention:** Show what happens when an API returns 500

#### Mistake: SQL injection with f-strings
**Symptoms:** Security vulnerability, potential data loss
**Cause:** `f"SELECT * FROM users WHERE name = '{user_input}'"`
**Fix:** `cursor.execute("SELECT * FROM users WHERE name = ?", (user_input,))`
**Intervention:** Show a live demo of SQL injection. It's unforgettable.

#### Mistake: Not closing database connections
**Symptoms:** File locks, connection pool exhaustion
**Cause:** Using `sqlite3.connect()` without context manager
**Fix:** Use `with sqlite3.connect(db_path) as conn:` or cache the connection
**Intervention:** Show the context manager pattern

#### Mistake: Hardcoded file paths
**Symptoms:** App works locally but fails on Community Cloud
**Cause:** `pd.read_csv("/Users/me/data/file.csv")`
**Fix:** Use relative paths: `pd.read_csv("data/file.csv")` or `Path(__file__).parent / "data"`
**Intervention:** Test on a different machine or OS to catch this

---

## Phase 4 — Machine Learning (M10–M12)

### Mistake: Training model on every rerun
**Symptoms:** App takes 30+ seconds to load, high CPU usage
**Cause:** Model training inside the Streamlit script without caching
**Fix:** Train once, save with joblib, load with `@st.cache_resource`
**Intervention:** Show the timing difference: 30s → 0.1s with caching

### Mistake: Preprocessing mismatch
**Symptoms:** Predictions are wrong or garbage
**Cause:** Different preprocessing for training vs. inference
**Fix:** Save the entire pipeline (scaler + model) as one object
**Intervention:** Show a side-by-side: training pipeline vs. inference pipeline

### Mistake: Not handling categorical inputs
**Symptoms:** `ValueError: could not convert string to float`
**Cause:** User enters text but model expects numbers
**Fix:** Map categorical inputs or use `st.selectbox` with valid options
**Intervention:** Always validate input types before prediction

### Mistake: No input validation
**Symptoms:** Model receives impossible values (negative age, >100% probability)
**Cause:** No range checks on numeric inputs
**Fix:** Use `min_value`, `max_value` on sliders, validate before prediction
**Intervention:** Define valid ranges for each feature

---

## Phase 5 — AI/LLM & Production (M13–M16)

### Mistake: Hardcoded API keys
**Symptoms:** Security vulnerability, key exposed in GitHub
**Cause:** `api_key = "sk-abc123..."` in source code
**Fix:** Use `st.secrets["api_key"]` or environment variables
**Intervention:** Scan GitHub repos for API keys. Show real examples of leaked keys.

### Mistake: Not handling API rate limits
**Symptoms:** App fails intermittently with 429 errors
**Cause:** No retry logic or rate limiting
**Fix:** Implement retry with exponential backoff
**Intervention:** Show how to handle 429 responses gracefully

### Mistake: Exposing sensitive data in URLs
**Symptoms:** API keys visible in browser history or logs
**Cause:** Passing secrets as query parameters
**Fix:** Use headers or POST body for sensitive data
**Intervention:** Review all URL construction in student code

### Mistake: No `.gitignore` for secrets
**Symptoms:** `.env` or `secrets.toml` committed to GitHub
**Cause:** Forgetting to add files to `.gitignore`
**Fix:** Add `.env`, `secrets.toml`, `*.env` to `.gitignore`
**Intervention:** Make `.gitignore` the first file in every project

### Mistake: Community Cloud deployment fails
**Symptoms:** Build error or app won't start on Community Cloud
**Cause:** Missing requirements.txt, wrong Python version, hardcoded paths
**Fix:** Check requirements.txt, use relative paths, verify Python version
**Intervention:** Walk through deployment checklist before submitting

### Mistake: No testing
**Symptoms:** Bugs found only by users
**Cause:** Students skip testing entirely
**Fix:** Write at least basic tests: does the app render? Do predictions work?
**Intervention:** Provide test templates. Grade testing as part of assignments.

---

## Intervention Strategies

### Preventive (Before Mistakes Happen)
- Show the error before students encounter it
- Provide boilerplate templates with correct patterns
- Create a "cheat sheet" of common patterns
- Pair experienced students with beginners

### Corrective (During Grading)
- Use consistent rubrics so partial credit is fair
- Point to specific resources when marking errors
- Provide personalized feedback, not just point deductions
- Group feedback for common patterns

### Remediative (After Mistakes Are Found)
- Address top 3 mistakes in the next lecture
- Create targeted exercises for persistent errors
- Offer office hours focused on specific topics
- Update this document with new patterns

---

## Related Materials

- [Exercise Guide](exercise_guide.md) — Per-exercise grading notes
- [Assessment Strategy](assessment_strategy.md) — Grading rubrics
- [Session Plans](2_hour_lecture_plan.md) — When to address each mistake
- [Solution Guide](solution_guide.md) — Correct implementations

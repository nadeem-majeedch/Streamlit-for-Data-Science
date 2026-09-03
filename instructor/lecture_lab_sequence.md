# 📋 Complete Lecture/Lab Sequence

> **Streamlit for Data Science — Learn, Build, Deploy**
> *Every session mapped to learning outcomes, repository resources, and assessment.*

---

## Overview

| | Count | Total Time |
|---|---|---|
| **Lecture sessions** (120 min) | 16 | 32 hours |
| **Lab sessions** (50 min) | 4 | 3.3 hours |
| **Total contact hours** | 20 | ~35 hours |
| **CLOs covered** | 12 | — |
| **Repository resources mapped** | 120+ | — |

### Session Index

| # | Title | Type | Week | CLOs | Bloom's |
|---|-------|------|------|------|---------|
| S01 | Streamlit Fundamentals | Lecture | 1 | CLO1, CLO2 | L1–L2 |
| S02 | Widgets & User Input | Lecture | 2 | CLO1, CLO2 | L2–L3 |
| S03 | Layouts & Dashboard UI | Lecture | 3 | CLO2, CLO6 | L2–L3 |
| **L1** | **Lab 1: Personal Dashboard** | **Lab** | **3** | **CLO2** | **L3** |
| S04 | DataFrames & Visualization | Lecture | 4 | CLO3 | L3 |
| S05 | Session State & Reruns | Lecture | 5 | CLO1, CLO4 | L2–L3 |
| S06 | File Upload & Dashboards | Lecture | 6 | CLO3, CLO4 | L3 |
| **L2** | **Lab 2: Interactive Dashboard** | **Lab** | **6** | **CLO3, CLO4** | **L3–L4** |
| S07 | Caching & Performance | Lecture | 7 | CLO4, CLO5 | L3–L4 |
| S08 | Architecture & Multipage | Lecture | 8 | CLO5, CLO6 | L3–L4 |
| **L3** | **Lab 3: Multipage Architecture** | **Lab** | **8** | **CLO6** | **L3–L4** |
| S09 | APIs & Databases | Lecture | 9 | CLO6, CLO7 | L3–L4 |
| S10 | Intro to ML with Streamlit | Lecture | 10 | CLO8 | L3–L4 |
| S11 | ML Model Deployment | Lecture | 11 | CLO8 | L3–L5 |
| **L4** | **Lab 4: ML Prediction App** | **Lab** | **11** | **CLO8** | **L3–L4** |
| S12 | NLP & Text Analysis | Lecture | 12 | CLO8, CLO9 | L3–L4 |
| S13 | LLM & RAG Applications | Lecture | 13 | CLO9 | L3–L4 |
| S14 | Security & Deployment | Lecture | 14 | CLO10, CLO11 | L4–L5 |
| S15 | Production & Capstone Work | Lecture | 15 | CLO10–CLO12 | L4–L6 |
| S16 | Capstone Presentations | Lecture | 16 | CLO12 | L5–L6 |

---

## Workload Summary

| Week | Lecture (2h) | Lab (50m) | Self-Study | Reading | Notebook | Exercise | Total |
|------|-------------|-----------|------------|---------|----------|----------|-------|
| 1 | S01 | — | 1.5h | 01, 02 | 01, 02 | 01 | ~5.5h |
| 2 | S02 | — | 2.0h | 03, 04 | 03, 04 | 03, 04 | ~6.5h |
| 3 | S03 | **L1** | 1.5h | 05, 06 | 05, 06 | 05, 06 | ~7h |
| 4 | S04 | — | 2.0h | 07, 08 | 07, 08 | 07, 08 | ~7h |
| 5 | S05 | — | 1.5h | 11 | 11 | 11 | ~6h |
| 6 | S06 | **L2** | 1.5h | 09, 10 | 09, 10 | 09, 10 | ~7h |
| 7 | S07 | — | 1.5h | 12 | 12 | 12 | ~6h |
| 8 | S08 | **L3** | 1.5h | 13 | 13 | 13 | ~7h |
| 9 | S09 | — | 2.0h | 13, 14 | 14 | 09-API, 14 | ~7.5h |
| 10 | S10 | — | 2.0h | 15 | 15 | 15 | ~6.5h |
| 11 | S11 | **L4** | 2.0h | 15 | 15 | 15 | ~7h |
| 12 | S12 | — | 1.5h | 17 | 17 | 17 | ~6h |
| 13 | S13 | — | 2.0h | 18 | 18 | 18 | ~6.5h |
| 14 | S14 | — | 2.0h | deploy, sec | deploy | deploy, 16 | ~7h |
| 15 | S15 | — | 2.5h | — | — | — | ~6.5h |
| 16 | S16 | — | 1.0h | — | — | — | ~3.5h |

**Average weekly workload: ~6.5 hours** (within 150-hour semester target for a 4-credit course)

---

## Detailed Session Plans

---

### Session S01 — Streamlit Fundamentals

**Week 1 · 120 min · CLO1, CLO2 · Bloom's: L1–L2**

| | |
|---|---|
| **Learning Outcomes** | Explain what Streamlit is and how it differs from Jupyter/Dash/Flask; build and run a first application; understand the top-to-bottom rerun model |
| **Prerequisites** | Python basics, Pandas basics |

#### Concepts
- What is Streamlit? Philosophy and design goals
- Streamlit vs Jupyter / Dash / Flask / Gradio (conceptual comparison)
- The execution model: script reruns top-to-bottom on every interaction
- `st.set_page_config` must be first
- Text elements: `st.title`, `st.header`, `st.subheader`, `st.caption`, `st.markdown`, `st.write`
- Displaying data: `st.dataframe`, `st.table`, `st.metric`

#### Live Coding (30 min)
Build together from scratch:
```python
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Hello Streamlit", layout="wide")
st.title("My First Streamlit App")

st.header("Why Streamlit?")
st.write("One-line API calls. Instant interactivity. No HTML/JS/CSS.")

df = pd.DataFrame({"Name": ["Alice", "Bob", "Charlie"], "Score": [85, 92, 78]})
st.dataframe(df)

if st.button("Say Hello"):
    st.write("Hello, Data Science!")
```
**Demo the rerun:** Click the button, show how the whole script re-executes.

#### Demonstration (5 min)
Run the existing demo app:
- `apps/01_introduction_demo.py` — show what a polished first app looks like
- Side-by-side: show the same data in Jupyter vs Streamlit

#### Student Activity (20 min)
- Modify the live-coded app: change text, add a chart (`st.line_chart(df)`), add `st.metric`
- Create a "report card" displaying 3 metrics using `st.metric`

#### Related Repository Resources

| Type | File | Purpose |
|------|------|---------|
| Reading | `readings/01_streamlit_introduction.md` | Conceptual foundation |
| Reading | `readings/02_first_streamlit_app.md` | Installation, first app |
| Notebook | `notebooks/01_Streamlit_Introduction.ipynb` | Concepts, comparisons |
| Notebook | `notebooks/02_First_Streamlit_App.ipynb` | Hands-on first app |
| Exercise | `exercises/01_hello_streamlit.py` | Text, data display, report card |
| Demo App | `apps/01_introduction_demo.py` | Polished demo |
| Demo App | `apps/hello.py` | Environment check |
| Quiz | `quizzes/01_fundamentals.md` | Post-session quiz |

#### Discussion (10 min)
"Why does Streamlit rerun the entire script on every interaction? What are the implications for code design?"

#### Homework
- Read `readings/01_streamlit_introduction.md` and `readings/02_first_streamlit_app.md`
- Complete `notebooks/01_Streamlit_Introduction.ipynb` and `notebooks/02_First_Streamlit_App.ipynb`
- Complete Exercise 01

#### Assessment
- Quiz Q01 administered at start of next session

---

### Session S02 — Widgets & User Input

**Week 2 · 120 min · CLO1, CLO2 · Bloom's: L2–L3**

| | |
|---|---|
| **Learning Outcomes** | Use all major widget types; understand return values and `key` parameter; build interactive forms; connect widget output to application behavior |
| **Prerequisites** | S01 |

#### Concepts
- Widgets as Streamlit's input mechanism: each returns a value
- Core widgets: `st.button`, `st.checkbox`, `st.slider`, `st.selectbox`, `st.multiselect`, `st.radio`, `st.text_input`, `st.text_area`, `st.number_input`, `st.date_input`, `st.time_input`
- The `key` parameter: widget identity across reruns
- `st.form` and `st.form_submit_button`: batched submissions
- Widget return value flow: widget → variable → conditional/display

#### Live Coding (30 min)
Build a dataset filter app:
```python
import streamlit as st
import pandas as pd
from sklearn.datasets import load_iris

st.set_page_config(page_title="Widget Demo", layout="wide")
st.title("Widgets & User Input")

iris = load_iris(as_frame=True).frame
iris.columns = ["sepal_length", "sepal_width", "petal_length", "petal_width", "species"]

with st.sidebar:
    st.header("Filters")
    species = st.multiselect("Species", iris["species"].unique(), default=iris["species"].unique())
    min_sepal = st.slider("Min Sepal Length", 4.0, 8.0, 4.0)

filtered = iris[iris["species"].isin(species) & (iris["sepal_length"] >= min_sepal)]
st.write(f"Showing **{len(filtered)}** of **{len(iris)}** rows")
st.dataframe(filtered)
```
**Key insight:** Show how changing a slider immediately reruns the script and filters the data.

#### Demonstration (5 min)
- `apps/03_widgets_demo.py` — showcase all widget types in one app
- `apps/04_forms_demo.py` — show form-based input patterns

#### Student Activity (20 min)
- Add `st.text_input` for name search, `st.checkbox` for toggling chart view
- Build a "registration form" using `st.form` with validation

#### Related Repository Resources

| Type | File | Purpose |
|------|------|---------|
| Reading | `readings/03_streamlit_widgets_and_input.md` | All widget types, forms |
| Reading | `readings/04_widget_keys_and_behavior.md` | Keys, identity, callbacks |
| Notebook | `notebooks/03_streamlit_widgets.ipynb` | Every widget type |
| Notebook | `notebooks/04_interactive_ds_controls.ipynb` | DS filter controls |
| Exercise | `exercises/03_widget_mastery.py` | All widget types + form |
| Exercise | `exercises/04_dataset_filter_app.py` | Sidebar filters + DataFrame |
| Demo App | `apps/03_widgets_demo.py` | Widget showcase |
| Demo App | `apps/04_forms_demo.py` | Form patterns |
| Quiz | `quizzes/02_widgets_input.md` | Post-session quiz |

#### Discussion (10 min)
"When should you use a `st.form` vs. direct widgets? What are the tradeoffs?"

#### Homework
- Read `readings/03_streamlit_widgets_and_input.md` and `readings/04_widget_keys_and_behavior.md`
- Complete `notebooks/03_streamlit_widgets.ipynb` and `notebooks/04_interactive_ds_controls.ipynb`
- Complete Exercise 03 and 04

#### Assessment
- Quiz Q02 administered at start of next session

---

### Session S03 — Layouts & Dashboard UI

**Week 3 · 120 min · CLO2, CLO6 · Bloom's: L2–L3**

| | |
|---|---|
| **Learning Outcomes** | Use sidebar, columns, tabs, expanders, and containers; design readable dashboard layouts; understand that "A DS app is not a notebook in a web page" |
| **Prerequisites** | S02 |

#### Concepts
- Layout hierarchy: page → sidebar → columns → containers → tabs → expanders
- `st.sidebar` for persistent controls
- `st.columns` with ratios: `st.columns([2, 1, 1])`
- `st.tabs` for alternate views
- `st.expander` for progressive disclosure
- `st.container` for logical grouping
- `st.popover` and `st.dialog` for overlays
- `st.metric` for KPI cards
- Dashboard UX: readability, information hierarchy, avoiding clutter

#### Live Coding (30 min)
Build a complete dashboard skeleton:
```python
st.set_page_config(page_title="Sales Dashboard", page_icon="📊", layout="wide")

with st.sidebar:
    st.header("⚙️ Settings")
    region = st.selectbox("Region", ["All", "North", "South", "East", "West"])
    date_range = st.date_input("Date Range", [])

st.title("📊 Sales Dashboard")

col1, col2, col3, col4 = st.columns(4)
col1.metric("Revenue", "$1.2M", "+12%")
col2.metric("Orders", "8,432", "+5%")
col3.metric("Customers", "2,145", "+3%")
col4.metric("Avg Order", "$142", "-2%")

tab1, tab2, tab3 = st.tabs(["📈 Charts", "📋 Data", "ℹ️ Details"])
with tab1:
    st.line_chart(...)
with tab2:
    st.dataframe(...)
with tab3:
    with st.expander("Methodology"):
        st.write("...")
```

#### Demonstration (5 min)
- `apps/05_layouts_demo.py` — layout elements showcase
- `apps/06_dashboard_demo.py` — complete Sales Analytics Dashboard
- Show a "bad" dashboard (everything in one column, no metrics) vs. the well-designed one

#### Student Activity (20 min)
- Redesign the demo layout: swap tabs for columns, add expanders
- Build a 3-column KPI section with `st.metric` cards

#### Related Repository Resources

| Type | File | Purpose |
|------|------|---------|
| Reading | `readings/05_layouts_and_containers.md` | Sidebar, columns, tabs, expanders |
| Reading | `readings/06_dashboard_design_ui_ux.md` | DS dashboard design philosophy |
| Notebook | `notebooks/05_layouts_and_containers.ipynb` | Interactive layout exploration |
| Notebook | `notebooks/06_data_science_dashboards.ipynb` | Dashboard design patterns |
| Exercise | `exercises/05_layout_basics.py` | Sidebar, columns, tabs, expanders |
| Exercise | `exercises/06_dashboard_builder.py` | Complete dashboard layout |
| Demo App | `apps/05_layouts_demo.py` | Layout showcase |
| Demo App | `apps/06_dashboard_demo.py` | Complete dashboard |
| Quiz | `quizzes/03_layouts_uiux.md` | Post-session quiz |

#### Discussion (10 min)
"What makes a Data Science dashboard readable? How is it different from a notebook?"

#### Homework
- A01 (Personal Dashboard) assigned — **due end of Week 3**
- Read `readings/05_layouts_and_containers.md` and `readings/06_dashboard_design_ui_ux.md`
- Complete Exercises 05 and 06

#### Assessment
- Quiz Q03 at start of next session
- **A01 due this week** (4% of grade)

---

### Lab L1 — Personal Dashboard (Week 3)

**Week 3 · 50 min · CLO2 · Bloom's: L3**

| | |
|---|---|
| **Learning Outcomes** | Independently build a complete dashboard; integrate widgets, layouts, and data display |
| **Prerequisites** | S01–S03 |
| **Related Assignment** | A01 — Personal Dashboard (due this week) |

#### Activities

| Time | Task | Details |
|------|------|---------|
| 0:00–0:03 | Setup | Open IDE, verify `streamlit run apps/hello.py` works |
| 0:03–0:08 | Briefing | Show expected outcome, review A01 requirements |
| 0:08–0:20 | **Task 1: Skeleton** | `st.set_page_config`, sidebar with 3+ widgets, 3 columns with `st.metric`, 2+ tabs |
| 0:20–0:35 | **Task 2: Data** | Load a CSV, display with `st.dataframe`, connect filters, show summary stats |
| 0:35–0:43 | **Task 3: Polish** | Add download button, expander, ensure layout is readable |
| 0:43–0:48 | Review | Share 2–3 student dashboards, discuss approaches |
| 0:48–0:50 | Wrap-up | Submit work, remind A01 deadline |

#### Related Repository Resources

| Type | File |
|------|------|
| Lab guide | `instructor/lab_activities.md` § Lab 1 |
| Exercise | `exercises/05_layout_basics.py` |
| Exercise | `exercises/06_dashboard_builder.py` |
| Demo | `apps/06_dashboard_demo.py` |
| Assignment | `assignments/A01_personal_dashboard.md` |
| Instructor notes | `instructor/common_student_mistakes.md` § M03 |
| Grading | `instructor/exercise_guide.md` § Exercise 05, 06 |

---

### Session S04 — DataFrames & Visualization

**Week 4 · 120 min · CLO3 · Bloom's: L3**

| | |
|---|---|
| **Learning Outcomes** | Display DataFrames with column configuration; choose appropriate chart types; integrate Matplotlib and Plotly with Streamlit |
| **Prerequisites** | S01–S03 |

#### Concepts
- `st.dataframe` (interactive) vs. `st.table` (static)
- `column_config`: hiding, renaming, formatting, type-specific configs
- Pandas `Styler` for conditional formatting
- Native Streamlit charts: `st.line_chart`, `st.bar_chart`, `st.area_chart`, `st.scatter_chart`, `st.map`
- Matplotlib integration: `st.pyplot(fig)`
- Plotly integration: `st.plotly_chart(fig, use_container_width=True)`
- Altair integration: `st.altair_chart(chart, use_container_width=True)`
- Chart selection: matching data type and question to chart type

#### Live Coding (30 min)
Build an EDA view with the Iris dataset:
```python
import streamlit as st
import pandas as pd
import plotly.express as px
from sklearn.datasets import load_iris

st.set_page_config(page_title="EDA View", layout="wide")
st.title("📊 Exploratory Data Analysis")

iris = load_iris(as_frame=True).frame

# Column-configured DataFrame
st.dataframe(iris, column_config={
    "sepal_length": st.column_config.NumberColumn("Sepal Length", format="%.1f"),
    "species": st.column_config.TextColumn("Species"),
}, use_container_width=True)

# Chart selection
chart_type = st.selectbox("Chart Type", ["Histogram", "Scatter", "Box"])
x = st.selectbox("X axis", iris.columns[:-1])
if chart_type == "Histogram":
    fig = px.histogram(iris, x=x, color="species", barmode="group")
elif chart_type == "Scatter":
    y = st.selectbox("Y axis", iris.columns[:-1], index=1)
    fig = px.scatter(iris, x=x, y=y, color="species")
st.plotly_chart(fig, use_container_width=True)
```

#### Demonstration (5 min)
- `apps/07_data_display_demo.py` — Data Display & Visualization Dashboard

#### Student Activity (20 min)
- Add a correlation heatmap (Matplotlib or Plotly)
- Switch between Matplotlib and Plotly for the same chart
- Add `st.metric` cards showing dataset statistics

#### Related Repository Resources

| Type | File | Purpose |
|------|------|---------|
| Reading | `readings/07_data_display_dataframes.md` | column_config, Styler, filtering |
| Reading | `readings/08_visualization_matplotlib_plotly.md` | Chart types, integration |
| Notebook | `notebooks/07_DataFrames_Tables_Pandas.ipynb` | DataFrame display |
| Notebook | `notebooks/08_Interactive_Visualization.ipynb` | All chart types |
| Exercise | `exercises/07_data_display_challenges.py` | DataFrame skills |
| Exercise | `exercises/08_visualization_workshop.py` | Chart selection |
| Demo App | `apps/07_data_display_demo.py` | Visualization dashboard |
| Quiz | `quizzes/04_dataframes_visualization.md` | Post-session quiz |
| Project | `projects/P09_visualization_dashboard.md` | Visualization project spec |

#### Discussion (10 min)
"When would you choose Plotly over Matplotlib? When would you use native `st.bar_chart`?"

#### Homework
- Read readings 07 and 08
- Complete notebooks 07 and 08
- Complete exercises 07 and 08

#### Assessment
- Quiz Q04 at start of next session

---

### Session S05 — Session State & Reruns

**Week 5 · 120 min · CLO1, CLO4 · Bloom's: L2–L3**

| | |
|---|---|
| **Learning Outcomes** | Explain why Streamlit reruns and when state is needed; initialize and use `st.session_state`; use callbacks; debug common state bugs |
| **Prerequisites** | S03 |

#### Concepts
- **The core problem:** every interaction reruns the entire script from top to bottom
- `st.session_state`: per-session dictionary that persists across reruns
- Initialization pattern: `if "key" not in st.session_state: st.session_state.key = default`
- Modifying state: `st.session_state.key = new_value`
- Callbacks: `on_change` parameter for widget-based state modification
- Forms and state interaction
- Common bugs: uninitialized state, using global variables, callback conflicts

#### Live Coding (30 min)
**The counter bug — live demonstration:**
```python
# BROKEN — explain why
count = 0
if st.button("Increment"):
    count += 1
st.write(f"Count: {count}")

# FIXED
if "count" not in st.session_state:
    st.session_state.count = 0
if st.button("Increment"):
    st.session_state.count += 1
st.write(f"Count: {st.session_state.count}")
```
**Then build a multi-step wizard:**
```python
if "step" not in st.session_state:
    st.session_state.step = 1

if st.session_state.step == 1:
    st.header("Step 1: Choose Data")
    dataset = st.selectbox("Dataset", ["Iris", "Titanic", "Housing"])
    if st.button("Next"):
        st.session_state.dataset = dataset
        st.session_state.step = 2
        st.rerun()

elif st.session_state.step == 2:
    st.header("Step 2: Configure")
    # ... configure parameters ...
    if st.button("Next"):
        st.session_state.step = 3
        st.rerun()

elif st.session_state.step == 3:
    st.header("Step 3: Results")
    # ... show results ...
    if st.button("Start Over"):
        st.session_state.step = 1
        st.rerun()
```

#### Demonstration (5 min)
- `apps/11_session_state_demo.py` — Session State & Execution Model Demo

#### Student Activity (20 min)
- Add a "comparison" feature: save results to session_state, compare multiple runs
- Add a "Reset All" button that clears session_state
- Debug a provided buggy app (3 intentional state bugs)

#### Related Repository Resources

| Type | File | Purpose |
|------|------|---------|
| Reading | `readings/11_session_state_and_execution.md` | Reruns, state, workflows |
| Notebook | `notebooks/11_session_state_execution_model.ipynb` | State patterns |
| Exercise | `exercises/11_state_management_workshop.py` | Counter, wizard, undo/redo, cart |
| Demo App | `apps/11_session_state_demo.py` | State demo |
| Quiz | `quizzes/05_session_state.md` | Post-session quiz |
| Project | `projects/P02_data_explorer.md` | Uses session state |

#### Discussion (10 min)
"What other stateful patterns do you see in apps? (shopping cart, multi-step form, undo/redo, user preferences)"

#### Homework
- Read `readings/11_session_state_and_execution.md`
- Complete `notebooks/11_session_state_execution_model.ipynb`
- Complete Exercise 11

#### Assessment
- Quiz Q05 at start of next session

---

### Session S06 — File Upload & Dashboards

**Week 6 · 120 min · CLO3, CLO4 · Bloom's: L3**

| | |
|---|---|
| **Learning Outcomes** | Handle file uploads (CSV, Excel, JSON); process and validate uploaded data; build a complete interactive dashboard; use download buttons |
| **Prerequisites** | S04, S05 |

#### Concepts
- `st.file_uploader`: accept types, multiple files, size limits
- Reading uploaded files: `pd.read_csv(file)`, `pd.read_excel(file)`, `json.load(file)`
- Validation: file type, size, required columns
- The full workflow: UPLOAD → VALIDATE → READ → CLEAN → ANALYZE → VISUALIZE → DOWNLOAD
- `st.download_button`: exporting processed data
- Error handling for bad uploads

#### Live Coding (30 min)
Build a data explorer:
```python
st.set_page_config(page_title="Data Explorer", layout="wide")
st.title("📁 Data Explorer")

uploaded = st.file_uploader("Upload CSV", type=["csv"])
if uploaded:
    try:
        df = pd.read_csv(uploaded)
        st.success(f"Loaded {len(df)} rows × {len(df.columns)} columns")

        with st.sidebar:
            st.header("Filters")
            for col in df.select_dtypes(include="number").columns:
                min_val, max_val = float(df[col].min()), float(df[col].max())
                lo, hi = st.slider(col, min_val, max_val, (min_val, max_val))
                df = df[df[col].between(lo, hi)]

        tab1, tab2, tab3 = st.tabs(["Data", "Charts", "Stats"])
        with tab1:
            st.dataframe(df, use_container_width=True)
        with tab2:
            col = st.selectbox("Column", df.columns)
            st.bar_chart(df[col].value_counts())
        with tab3:
            st.write(df.describe())

        csv = df.to_csv(index=False).encode("utf-8")
        st.download_button("Download Filtered Data", csv, "filtered.csv", "text/csv")
    except Exception as e:
        st.error(f"Error reading file: {e}")
else:
    st.info("Upload a CSV file to begin exploring.")
```

#### Demonstration (5 min)
- `apps/09_file_upload_demo.py` — File Upload & Processing Dashboard
- `apps/10_interactive_data_explorer.py` — Interactive Data Explorer Dashboard

#### Student Activity (20 min)
- Add Excel upload support (`st.file_uploader(type=["csv", "xlsx"])`)
- Add a data quality summary section (missing values, dtypes)
- Add a correlation matrix chart

#### Related Repository Resources

| Type | File | Purpose |
|------|------|---------|
| Reading | `readings/09_file_upload_and_processing.md` | Upload, validation, cleaning |
| Reading | `readings/10_interactive_dashboard.md` | Dashboard architecture |
| Notebook | `notebooks/09_file_upload_and_processing.ipynb` | Upload pipeline |
| Notebook | `notebooks/10_interactive_dashboard.ipynb` | Dashboard patterns |
| Exercise | `exercises/09_file_upload_workshop.py` | Multi-format upload |
| Exercise | `exercises/10_dashboard_workshop.py` | Complete dashboard |
| Demo App | `apps/09_file_upload_demo.py` | Upload dashboard |
| Demo App | `apps/10_interactive_data_explorer.py` | Data explorer |
| Quiz | `quizzes/06_file_upload.md` | Post-session quiz |
| Project | `projects/P01_csv_data_viewer.md` | CSV viewer project |
| Project | `projects/P02_data_explorer.md` | Data explorer project |
| Project | `projects/P05_eda_dashboard.md` | EDA dashboard project |

#### Discussion (10 min)
"Dashboard design review: show your dashboards. What makes them usable vs. cluttered?"

#### Homework
- A02 (Data Explorer) assigned — **due end of Week 6**
- Read readings 09 and 10
- Complete notebooks 09 and 10
- Complete exercises 09 (file upload) and 10 (dashboard workshop)

#### Assessment
- Quiz Q06 at start of next session
- **A02 due this week** (4% of grade)

---

### Lab L2 — Interactive Dashboard (Week 6)

**Week 6 · 50 min · CLO3, CLO4 · Bloom's: L3–L4**

| | |
|---|---|
| **Learning Outcomes** | Build a complete data exploration dashboard from scratch; integrate upload, filtering, visualization, and export |
| **Prerequisites** | S04–S06 |
| **Related Assignment** | A02 — Data Explorer (due this week) |

#### Activities

| Time | Task | Details |
|------|------|---------|
| 0:00–0:03 | Setup | Verify environment, open previous exercise |
| 0:03–0:08 | Briefing | Show expected outcome, review A02 deliverables |
| 0:08–0:18 | **Task 1: Upload Pipeline** | Accept CSV, validate, display shape/columns/dtypes, show first 5 rows |
| 0:18–0:33 | **Task 2: Dynamic Filters** | Auto-detect column types, create filters, apply simultaneously, show row count |
| 0:33–0:43 | **Task 3: Charts & Export** | 3 chart types, column selection, correlation matrix, download button |
| 0:43–0:48 | Review | Share approaches, common patterns, design discussion |
| 0:48–0:50 | Wrap-up | Submit, remind A02 deadline |

#### Related Repository Resources

| Type | File |
|------|------|
| Lab guide | `instructor/lab_activities.md` § Lab 2 |
| Exercise | `exercises/09_file_upload_workshop.py` |
| Exercise | `exercises/10_dashboard_workshop.py` |
| Demo | `apps/10_interactive_data_explorer.py` |
| Assignment | `assignments/A02_data_explorer.md` |
| Grading | `instructor/exercise_guide.md` § Exercise 10 |

---

### Session S07 — Caching & Performance

**Week 7 · 120 min · CLO4, CLO5 · Bloom's: L3–L4**

| | |
|---|---|
| **Learning Outcomes** | Explain why caching matters; use `st.cache_data` and `st.cache_resource` correctly; implement TTL; measure and improve performance |
| **Prerequisites** | S05 |

#### Concepts
- The performance problem: expensive computation on every rerun
- `@st.cache_data`: serializes and copies return values (for DataFrames, computed data)
- `@st.cache_resource`: returns the same object (for models, database connections, connections)
- TTL: `@st.cache_data(ttl=3600)` for time-sensitive data
- Cache invalidation: when and how to clear caches
- `st.fragment` for partial reruns (advanced optimization)
- Measuring performance: `time.time()` before/after

#### Live Coding (30 min)
**Performance experiment — the "before and after":**
```python
import time
import pandas as pd
import streamlit as st

st.title("Caching Experiment")

# WITHOUT caching
start = time.time()
df = pd.read_csv("large_dataset.csv")  # simulate slow load
time.sleep(2)  # simulate expensive computation
summary = df.groupby("category").agg({"value": ["mean", "std", "count"]})
st.write(f"Without cache: {time.time()-start:.2f}s")

# WITH caching
@st.cache_data(ttl=3600)
def load_data():
    time.sleep(2)
    return pd.read_csv("large_dataset.csv")

start = time.time()
df = load_data()
st.write(f"With cache: {time.time()-start:.2f}s")
```
Then show `cache_resource` for a model object.

#### Demonstration (5 min)
- `apps/12_caching_performance_demo.py` — Caching & Performance Demo

#### Student Activity (20 min)
- Add `@st.cache_data` to their A02 dashboard data loading
- Measure before/after with `time.time()`
- Add TTL to time-sensitive data
- Experiment: what happens when you cache a mutable object?

#### Related Repository Resources

| Type | File | Purpose |
|------|------|---------|
| Reading | `readings/12_caching_and_performance.md` | cache_data, cache_resource, TTL |
| Notebook | `notebooks/12_caching_performance.ipynb` | Caching experiments |
| Exercise | `exercises/12_caching_workshop.py` | Optimization, design decisions |
| Demo App | `apps/12_caching_performance_demo.py` | Performance demo |
| Quiz | `quizzes/08_caching_performance.md` | Post-session quiz |
| Project | `projects/P18_production_dashboard.md` | Performance requirements |

#### Discussion (10 min)
"When should you NOT cache? (real-time data, security-sensitive, frequently changing data)"

#### Homework
- Read `readings/12_caching_and_performance.md`
- Complete `notebooks/12_caching_performance.ipynb`
- Complete Exercise 12

#### Assessment
- Quiz Q08 at start of next session

---

### Session S08 — Architecture & Multipage

**Week 8 · 120 min · CLO5, CLO6 · Bloom's: L3–L4**

| | |
|---|---|
| **Learning Outcomes** | Refactor a monolithic app into modular components; build multipage applications; use `st.navigation`; apply separation of concerns |
| **Prerequisites** | S03, S07 |

#### Concepts
- Why modularize: maintainability, reusability, team collaboration
- Progression: single file → functions → modules → pages
- `st.navigation` for multipage routing
- File structure: `app.py`, `pages/`, `utils/`, `config.py`
- Shared logic in utility modules
- Avoiding circular imports
- Separation of concerns: UI / data processing / business logic

#### Live Coding (30 min)
**Refactor live — take a 200-line `app.py` and break it up:**
Before (monolith):
```python
# 200 lines in one file — loading, filtering, charting, settings, all mixed
```
After (modular):
```
my_app/
├── app.py              # st.navigation() only
├── config.py           # DATABASE_PATH, FEATURE_NAMES
├── utils/
│   ├── data.py         # load_data(), filter_data()
│   ├── charts.py       # create_bar_chart(), create_line_chart()
│   └── formatting.py   # metric_card(), format_number()
└── pages/
    ├── 1_📊_Overview.py
    ├── 2_📈_Analysis.py
    └── 3_⚙️_Settings.py
```

#### Demonstration (5 min)
- `apps/13_modular_app/` — complete modular multipage app example

#### Student Activity (20 min)
- Add a new page to the refactored app
- Move a shared function to `utils/`
- Verify all pages still work after refactoring

#### Related Repository Resources

| Type | File | Purpose |
|------|------|---------|
| Reading | `readings/13_application_architecture.md` | Architecture, modules, multipage |
| Notebook | `notebooks/13_application_architecture.ipynb` | Architecture patterns |
| Exercise | `exercises/13_architecture_workshop.py` | Refactoring, components |
| Demo App | `apps/13_modular_app/` | Complete modular example |
| Quiz | `quizzes/09_architecture_multipage.md` | Post-session quiz |
| Project | `projects/P14_database_dashboard.md` | Multipage + DB project |
| Project | `projects/P18_production_dashboard.md` | Architecture requirements |

#### Discussion (10 min)
"What goes in a shared module vs. a page file? When does a utility module become too large?"

#### Homework
- A03 (Multipage Application) assigned — **due end of Week 13**
- Read `readings/13_application_architecture.md`
- Complete `notebooks/13_application_architecture.ipynb`
- Complete Exercise 13

#### Assessment
- Quiz Q09 at start of next session

---

### Lab L3 — Multipage Architecture (Week 8)

**Week 8 · 50 min · CLO6 · Bloom's: L3–L4**

| | |
|---|---|
| **Learning Outcomes** | Independently refactor a monolithic app; implement multipage navigation with shared utilities |
| **Prerequisites** | S07, S08 |

#### Activities

| Time | Task | Details |
|------|------|---------|
| 0:00–0:03 | Setup | Open the provided monolith `app.py` |
| 0:03–0:08 | Briefing | Show expected folder structure, review refactoring goals |
| 0:08–0:20 | **Task 1: Analyze & Plan** | Identify logical sections, draw page structure, list shared functions |
| 0:20–0:38 | **Task 2: Refactor** | Create `pages/` (3+ files), move shared logic to `utils/`, create `config.py`, implement `st.navigation` |
| 0:38–0:45 | **Task 3: Add Caching** | Cache data loading, add TTL, verify with timer |
| 0:45–0:48 | Review | Share refactored structures, discuss challenges |
| 0:48–0:50 | Wrap-up | Submit, preview mid-course assessment |

#### Related Repository Resources

| Type | File |
|------|------|
| Lab guide | `instructor/lab_activities.md` § Lab 3 |
| Demo | `apps/13_modular_app/` |
| Exercise | `exercises/13_architecture_workshop.py` |
| Grading | `instructor/exercise_guide.md` § Exercise 13 |

---

### Session S09 — APIs & Databases

**Week 9 · 120 min · CLO6, CLO7 · Bloom's: L3–L4**

| | |
|---|---|
| **Learning Outcomes** | Fetch data from REST APIs; connect Streamlit to SQLite; perform CRUD operations; use parameterized queries for security |
| **Prerequisites** | S06 |

#### Concepts
- REST API basics: GET, POST, status codes, JSON
- `requests` library: `requests.get(url)`, error handling, headers
- Displaying API data in Streamlit
- SQLite: creating tables, inserting, querying
- Parameterized queries: preventing SQL injection
- CRUD: Create, Read, Update, Delete
- Connection management: context managers, caching connections

#### Live Coding (30 min)
**API portion:**
```python
import requests
import streamlit as st

st.title("API Integration")
url = st.text_input("API URL", "https://jsonplaceholder.typicode.com/users")
if st.button("Fetch"):
    try:
        resp = requests.get(url, timeout=10)
        resp.raise_for_status()
        data = resp.json()
        st.dataframe(pd.json_normalize(data))
    except requests.RequestException as e:
        st.error(f"API error: {e}")
```
**Database portion:**
```python
import sqlite3

conn = sqlite3.connect("app_data.db")
conn.execute("""
    CREATE TABLE IF NOT EXISTS entries (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        value REAL
    )
""")

name = st.text_input("Name")
value = st.number_input("Value")
if st.button("Save"):
    conn.execute("INSERT INTO entries (name, value) VALUES (?, ?)", (name, value))
    conn.commit()
    st.success("Saved!")

rows = conn.execute("SELECT * FROM entries").fetchall()
st.dataframe(pd.DataFrame(rows, columns=["ID", "Name", "Value"]))
```
**Security demo:** Show SQL injection with f-strings, then fix with parameterized queries.

#### Demonstration (5 min)
- `apps/14_database_dashboard.py` — SQLite Database Dashboard

#### Student Activity (20 min)
- Fetch data from a public API and display in a DataFrame
- Create a database table and implement CRUD
- Combine: fetch API data → store in database → query and display

#### Related Repository Resources

| Type | File | Purpose |
|------|------|---------|
| Reading | `readings/13_application_architecture.md` | Architecture (API integration) |
| Reading | `readings/14_databases_and_persistence.md` | SQLite, SQL, CRUD, security |
| Notebook | `notebooks/14_databases_persistence.ipynb` | SQL basics, CRUD |
| Exercise | `exercises/09_api_connectors.py` | API fetch, JSON, design |
| Exercise | `exercises/14_database_workshop.py` | SQL, CRUD, parameterized queries |
| Demo App | `apps/14_database_dashboard.py` | Database dashboard |
| Quiz | `quizzes/10_databases_persistence.md` | Post-session quiz |
| Project | `projects/P14_database_dashboard.md` | Database + multipage project |

#### Discussion (10 min)
"Why must we ALWAYS use parameterized queries? Live demo: SQL injection."

#### Homework
- Read `readings/14_databases_and_persistence.md`
- Complete `notebooks/14_databases_persistence.ipynb`
- Complete exercises 09 (API) and 14 (database)
- **Mid-Course Assessment next week** (M01–M08)

#### Assessment
- Quiz Q10 at start of next session
- **Mid-Course Assessment at end of Week 9** (10% of grade)

---

### Session S10 — Intro to ML with Streamlit

**Week 10 · 120 min · CLO8 · Bloom's: L3–L4**

| | |
|---|---|
| **Learning Outcomes** | Train a simple model with scikit-learn; visualize evaluation metrics; understand the pipeline: train → save → load → predict |
| **Prerequisites** | S04–S07 |

#### Concepts
- ML in Streamlit: the key insight — don't retrain on every rerun
- Train once, save with `joblib`, load with `@st.cache_resource`
- Building a prediction UI: feature inputs → model → prediction + probability
- Visualizing model evaluation: confusion matrix, classification report, ROC curve
- Input validation for prediction features

#### Live Coding (30 min)
Build an Iris classifier:
```python
import streamlit as st
import pandas as pd
import numpy as np
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
import joblib

st.set_page_config(page_title="ML Classifier", layout="wide")
st.title("🤖 Iris Classifier")

# Train and save (runs once, cached)
@st.cache_resource
def train_model():
    iris = load_iris()
    X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.2)
    model = DecisionTreeClassifier()
    model.fit(X_train, y_train)
    accuracy = model.score(X_test, y_test)
    return model, accuracy

model, accuracy = train_model()
st.metric("Model Accuracy", f"{accuracy:.1%}")

# Prediction UI
st.subheader("Make a Prediction")
col1, col2, col3, col4 = st.columns(4)
sl = col1.slider("Sepal Length", 4.0, 8.0, 5.0)
sw = col2.slider("Sepal Width", 2.0, 4.5, 3.0)
pl = col3.slider("Petal Length", 1.0, 7.0, 3.5)
pw = col4.slider("Petal Width", 0.1, 2.5, 1.0)

if st.button("Predict"):
    features = np.array([[sl, sw, pl, pw]])
    pred = model.predict(features)[0]
    proba = model.predict_proba(features)[0]
    species = load_iris().target_names
    st.success(f"Prediction: **{species[pred]}**")
    st.bar_chart(pd.DataFrame({"Probability": proba}, index=species))
```

#### Demonstration (5 min)
- `apps/15_classification_app.py` — Iris Classification App
- `apps/15_regression_app.py` — California Housing Regression App

#### Student Activity (20 min)
- Change the model type (RandomForest, SVM)
- Add feature importance chart
- Try a regression model instead of classification
- Display the confusion matrix

#### Related Repository Resources

| Type | File | Purpose |
|------|------|---------|
| Reading | `readings/15_machine_learning_streamlit.md` | ML deployment patterns |
| Notebook | `notebooks/15_ml_streamlit.ipynb` | ML pipeline |
| Exercise | `exercises/15_ml_workshop.py` | Model deployment, preprocessing |
| Demo App | `apps/15_classification_app.py` | Classification demo |
| Demo App | `apps/15_regression_app.py` | Regression demo |
| Quiz | `quizzes/11_machine_learning.md` | Post-session quiz |
| Project | `projects/P06_ml_model_playground.md` | ML playground project |
| Project | `projects/P11_ml_prediction_app.md` | ML prediction project |

#### Discussion (10 min)
"What could go wrong in production with this model? (data drift, feature mismatch, stale data)"

#### Homework
- Read `readings/15_machine_learning_streamlit.md`
- Complete `notebooks/15_ml_streamlit.ipynb`
- Complete Exercise 15

#### Assessment
- Quiz Q11 at start of next session

---

### Session S11 — ML Model Deployment

**Week 11 · 120 min · CLO8 · Bloom's: L3–L5**

| | |
|---|---|
| **Learning Outcomes** | Save and load models correctly; build preprocessing pipelines matching training; handle invalid inputs; build batch prediction interfaces |
| **Prerequisites** | S10 |

#### Concepts
- The preprocessing trap: training vs. inference mismatch
- Saving entire pipelines (scaler + model) with `joblib`
- Model versioning: naming, metadata, timestamps
- Batch prediction: upload CSV → validate → preprocess → predict → download
- Input validation: range checks, type checks, missing values
- Confidence thresholds: when to show "uncertain" instead of a prediction

#### Live Coding (30 min)
Build a batch predictor:
```python
@st.cache_resource
def load_model():
    return joblib.load("model_pipeline.joblib")  # includes scaler

pipeline = load_model()

uploaded = st.file_uploader("Upload CSV for batch prediction", type=["csv"])
if uploaded:
    df = pd.read_csv(uploaded)
    required_cols = ["sepal_length", "sepal_width", "petal_length", "petal_width"]
    missing = [c for c in required_cols if c not in df.columns]
    if missing:
        st.error(f"Missing columns: {missing}")
    else:
        predictions = pipeline.predict(df[required_cols])
        df["prediction"] = predictions
        st.dataframe(df)
        csv = df.to_csv(index=False).encode("utf-8")
        st.download_button("Download Predictions", csv, "predictions.csv")
```

#### Demonstration (5 min)
- Show the classification app from S10 with batch upload added
- Show the preprocessing mismatch problem: wrong scaler → garbage predictions

#### Student Activity (20 min)
- Add confidence scores and uncertainty thresholds
- Add a confusion matrix visualization
- Handle edge cases: missing values, wrong types, out-of-range inputs

#### Related Repository Resources

| Type | File | Purpose |
|------|------|---------|
| Reading | `readings/15_machine_learning_streamlit.md` | ML deployment (continued) |
| Notebook | `notebooks/15_ml_streamlit.ipynb` | ML pipeline (continued) |
| Exercise | `exercises/15_ml_workshop.py` | ML workshop (continued) |
| Quiz | `quizzes/12_ml_deployment.md` | Post-session quiz |
| Project | `projects/P12_model_evaluation_dashboard.md` | Model evaluation project |
| Project | `projects/P13_batch_prediction.md` | Batch prediction project |

#### Discussion (10 min)
"What's the difference between a notebook and a deployed model? What changes?"

#### Homework
- Continue Exercise 15 (batch prediction)
- Start A04 (ML Production App) if ready

#### Assessment
- Quiz Q12 at start of next session

---

### Lab L4 — ML Prediction App (Week 11)

**Week 11 · 50 min · CLO8 · Bloom's: L3–L4**

| | |
|---|---|
| **Learning Outcomes** | Independently build a complete ML prediction app with input validation and batch processing |
| **Prerequisites** | S10, S11 |

#### Activities

| Time | Task | Details |
|------|------|---------|
| 0:00–0:03 | Setup | Verify scikit-learn and joblib installed |
| 0:03–0:08 | Briefing | Show expected outcome, review ML pipeline steps |
| 0:08–0:18 | **Task 1: Train & Save** | Train model on Titanic, save with joblib, verify loads |
| 0:18–0:33 | **Task 2: Prediction UI** | Feature inputs (selectbox for categorical, slider for numeric), validate, predict, show confidence |
| 0:33–0:43 | **Task 3: Batch** | File upload, validate columns, predict all rows, download results |
| 0:43–0:48 | Review | Share predictions, discuss preprocessing choices |
| 0:48–0:50 | Wrap-up | Submit, remind practical exam next week |

#### Related Repository Resources

| Type | File |
|------|------|
| Lab guide | `instructor/lab_activities.md` § Lab 4 |
| Demo | `apps/15_classification_app.py` |
| Demo | `apps/15_regression_app.py` |
| Exercise | `exercises/15_ml_workshop.py` |
| Grading | `instructor/exercise_guide.md` § Exercise 15 |

---

### Session S12 — NLP & Text Analysis

**Week 12 · 120 min · CLO8, CLO9 · Bloom's: L3–L4**

| | |
|---|---|
| **Learning Outcomes** | Apply text preprocessing; build a text classification pipeline; deploy NLP models in Streamlit; handle text input validation |
| **Prerequisites** | S11 |

#### Concepts
- NLP pipeline: text → preprocessing → features → model → prediction
- Text preprocessing: lowercase, tokenization, stopword removal, stemming/lemmatization
- TF-IDF vectorization: `TfidfVectorizer`
- Text classification: TF-IDF + Logistic Regression
- Sentiment analysis as a classification problem
- Batch text prediction
- Limitations of simple NLP models

#### Live Coding (30 min)
Build a sentiment analyzer:
```python
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline

# Train on sample data
texts = ["Great product!", "Terrible experience", "Love it", "Worst ever", ...]
labels = [1, 0, 1, 0, ...]  # 1=positive, 0=negative

@st.cache_resource
def train_nlp():
    pipe = Pipeline([("tfidf", TfidfVectorizer()), ("clf", LogisticRegression())])
    pipe.fit(texts, labels)
    return pipe

model = train_nlp()

text = st.text_area("Enter text to analyze")
if st.button("Analyze"):
    pred = model.predict([text])[0]
    proba = model.predict_proba([text])[0]
    label = "Positive 😊" if pred == 1 else "Negative 😞"
    st.write(f"**{label}** (confidence: {max(proba):.1%})")
```

#### Demonstration (5 min)
- `apps/17_sentiment_app.py` — Sentiment Analysis App

#### Student Activity (20 min)
- Try different preprocessing steps
- Add batch text prediction (textarea with one text per line)
- Analyze a real dataset (customer reviews)

#### Related Repository Resources

| Type | File | Purpose |
|------|------|---------|
| Reading | `readings/17_nlp_ai_applications.md` | NLP, TF-IDF, sentiment |
| Notebook | `notebooks/17_nlp_applications.ipynb` | NLP workflow |
| Exercise | `exercises/17_nlp_workshop.py` | Text classification |
| Demo App | `apps/17_sentiment_app.py` | Sentiment analyzer |
| Quiz | `quizzes/13_nlp_ai.md` | Post-session quiz |
| Project | `projects/P15_nlp_application.md` | NLP project spec |

#### Discussion (10 min)
"What are the limitations of simple NLP models? When would you need transformers/LLMs?"

#### Homework
- Read `readings/17_nlp_ai_applications.md`
- Complete `notebooks/17_nlp_applications.ipynb`
- Complete Exercise 17
- **Practical Exam this week** (10% of grade)

#### Assessment
- Quiz Q13 at start of next session
- **Practical Exam at end of Week 12** (3-hour timed coding, 100 marks)

---

### Session S13 — LLM & RAG Applications

**Week 13 · 120 min · CLO9 · Bloom's: L3–L4**

| | |
|---|---|
| **Learning Outcomes** | Build a chat interface; integrate with an LLM provider (or local alternative); understand RAG architecture; be aware of prompt injection and AI safety |
| **Prerequisites** | S12 |

#### Concepts
- LLM application architecture: prompt → model → response
- Streamlit chat interface: `st.chat_message`, `st.chat_input`
- Conversation state management with `st.session_state`
- Streaming responses
- Secrets management: `st.secrets["api_key"]`
- RAG: documents → chunks → embeddings → vector store → retrieve → augment prompt → LLM
- Prompt injection awareness
- Local/open-source model alternatives (when possible, avoid paid APIs for core lesson)

#### Live Coding (30 min)
Build a chat app (mock LLM for teaching, real API optional):
```python
import streamlit as st

st.set_page_config(page_title="LLM Chat", layout="wide")
st.title("💬 AI Chat")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# User input
if prompt := st.chat_input("Ask me anything"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

    # Mock response (replace with real API call)
    response = f"You asked: {prompt}. Here is a thoughtful response..."

    st.session_state.messages.append({"role": "assistant", "content": response})
    with st.chat_message("assistant"):
        st.write(response)
```
Show secrets management:
```python
# In .streamlit/secrets.toml: api_key = "sk-..."
api_key = st.secrets["api_key"]  # NEVER hardcode
```

#### Demonstration (5 min)
- `apps/18_llm_chat.py` — LLM Chat App (Demo/OpenAI/Local)
- `apps/18_rag_app.py` — RAG Document Q&A App (if available)

#### Student Activity (20 min)
- Add a system prompt selector
- Try a local/open-source alternative
- Modify the chat interface (add clear history button)

#### Related Repository Resources

| Type | File | Purpose |
|------|------|---------|
| Reading | `readings/18_llm_rag_applications.md` | LLM, RAG, chat, streaming |
| Reading | `readings/security_and_secrets.md` | Secrets management |
| Notebook | `notebooks/18_llm_applications.ipynb` | LLM providers, chat, RAG |
| Exercise | `exercises/18_llm_workshop.py` | LLM integration, RAG |
| Demo App | `apps/18_llm_chat.py` | Chat app |
| Demo App | `apps/18_rag_app.py` | RAG app |
| Quiz | `quizzes/14_llm_rag.md` | Post-session quiz |
| Project | `projects/P16_llm_chat.md` | LLM chat project |
| Project | `projects/P17_document_qa.md` | Document Q&A project |

#### Discussion (10 min)
"What are the risks of building LLM applications? Prompt injection, hallucination, data privacy."

#### Homework
- A03 (Multipage Application) **due end of this week** (4% of grade)
- Read readings 18 and security
- Complete notebooks 18 and security lab
- Complete Exercise 18

#### Assessment
- Quiz Q14 at start of next session
- **A03 due this week** (4% of grade)

---

### Session S14 — Security & Deployment

**Week 14 · 120 min · CLO10, CLO11 · Bloom's: L4–L5**

| | |
|---|---|
| **Learning Outcomes** | Apply security best practices; deploy to Streamlit Community Cloud; monitor and debug deployed applications; implement testing and logging |
| **Prerequisites** | S08 |

#### Concepts
- **Security:** API keys via `st.secrets`, `.gitignore`, input validation, SQL injection, file upload risks, LLM prompt injection
- **Deployment workflow:** local → git → GitHub → Community Cloud → deploy → monitor → update
- Repository structure for deployment: `requirements.txt`, `.gitignore`, `.streamlit/config.toml`
- Community Cloud: connecting repo, setting entry point, adding secrets
- Deployment debugging: build logs, runtime errors, dependency issues
- Resource limits and sleep behavior
- Basic testing with `st.testing.AppTest`
- Structured logging with Python `logging` module

#### Live Coding (30 min)
**Deploy together — end-to-end:**
1. Take a working app
2. Add `requirements.txt`
3. Add `.gitignore` (exclude `.env`, `secrets.toml`, `__pycache__`)
4. Push to GitHub
5. Deploy on Community Cloud
6. Test in browser
7. Break one thing → fix → redeploy
8. Show logs

**Security demo:**
```python
# BAD — hardcoded key
api_key = "sk-abc123..."  # NEVER DO THIS

# GOOD — secrets
api_key = st.secrets["api_key"]

# BAD — SQL injection
query = f"SELECT * FROM users WHERE name = '{user_input}'"

# GOOD — parameterized
query = "SELECT * FROM users WHERE name = ?"
cursor.execute(query, (user_input,))
```

#### Demonstration (5 min)
- `apps/deployable_app/` — Complete app ready for Community Cloud
- Show the deployed app on Community Cloud (if available)

#### Student Activity (20 min)
- Deploy their own app (or a practice app) to Community Cloud
- Instructor helps with failures
- Scan their own code for security issues

#### Related Repository Resources

| Type | File | Purpose |
|------|------|---------|
| Reading | `readings/security_and_secrets.md` | Security, secrets, validation |
| Reading | `readings/deployment_guide.md` | Deployment workflow, Community Cloud |
| Notebook | `notebooks/deployment_tutorial.ipynb` | Step-by-step deployment |
| Notebook | `notebooks/security_practical_lab.ipynb` | Security exercises |
| Exercise | `exercises/deployment_exercises.py` | Deployment preparation |
| Exercise | `exercises/16_production_ready.py` | Error handling, logging |
| Exercise | `exercises/security_exercises.md` | Security audit |
| Demo App | `apps/deployable_app/` | Deployable app reference |
| Quiz | `quizzes/15_deployment.md` | Post-session quiz |
| Quiz | `quizzes/16_production_maintenance.md` | Post-session quiz |
| Docs | `docs/deployment_checklist.md` | Pre-deployment checklist |
| Docs | `docs/deployment_troubleshooting.md` | Common deployment issues |
| Project | `projects/P18_production_dashboard.md` | Production dashboard |

#### Discussion (10 min)
"What breaks in production that works locally? (paths, memory, secrets, dependencies)"

#### Homework
- A04 (ML Production App) **due end of this week** (8% of grade)
- Read deployment and security readings
- Complete deployment exercises and security exercises
- Start capstone project (proposal due next week)

#### Assessment
- Quiz Q15 and Q16 at start of next session
- **A04 due this week** (8% of grade)

---

### Session S15 — Production & Capstone Work

**Week 15 · 120 min · CLO10–CLO12 · Bloom's: L4–L6**

| | |
|---|---|
| **Learning Outcomes** | Apply all course skills to a complete project; debug and optimize a non-trivial application; prepare for deployment and presentation |
| **Prerequisites** | All previous sessions |

#### Concepts (Quick Review)
- Testing with `st.testing.AppTest`
- Error handling patterns
- Logging best practices
- Performance profiling
- Documentation standards

#### Live Coding (10 min)
Quick demo: writing a basic `AppTest` test
```python
from streamlit.testing.v1 import AppTest

def test_app_renders():
    at = AppTest.from_file("app.py")
    at.run()
    assert not at.exception  # no errors
    assert at.title[0].value == "My App"

def test_prediction():
    at = AppTest.from_file("app.py")
    at.run()
    at.number_input[0].set_value(5.0)
    at.button[0].click()
    at.run()
    assert "Prediction" in at.markdown[0].value
```

#### Student Activity (100 min)
**Capstone work session:**
- 0:10–0:20: Capstone milestone check-in (each student reports progress)
- 0:20–0:50: Guided work (instructor circulates, helps debug)
- 0:50–0:55: Break
- 0:55–1:25: Independent work
- 1:25–1:40: Deployment help session
- 1:40–1:50: Presentation prep review

#### Related Repository Resources

| Type | File | Purpose |
|------|------|---------|
| Project | `projects/final_capstone.md` | Definitive capstone spec |
| Project | `projects/capstone_rubric.md` | Grading rubric |
| Project | `projects/capstone_submission_checklist.md` | Submission checklist |
| Project | `projects/capstone_presentation.md` | Presentation guide |
| Exercise | `exercises/16_production_ready.py` | Production patterns |
| Docs | `docs/deployment_checklist.md` | Deployment checklist |
| **Final Practical Assessment** | `assessments/final_practical_assessment.md` | 4-hour comprehensive exam |

#### Homework
- Complete capstone development
- Prepare 10-minute presentation with live demo
- Review `projects/capstone_submission_checklist.md`

#### Assessment
- **Final Practical Assessment** (15% of grade) — administered separately or at start

---

### Session S16 — Capstone Presentations

**Week 16 · 120 min · CLO12 · Bloom's: L5–L6**

| | |
|---|---|
| **Learning Outcomes** | Present a complete application to an audience; answer technical questions; provide peer feedback |
| **Prerequisites** | All sessions |

#### Presentation Format (per student, 10 min)

| Time | Content |
|------|---------|
| 0:00–1:00 | Problem statement and motivation |
| 1:00–3:00 | **Live demo** of the application |
| 3:00–5:00 | Technical overview (architecture, key decisions) |
| 5:00–7:00 | Challenges and what you learned |
| 7:00–8:00 | Future improvements |
| 8:00–10:00 | Q&A from instructor and peers |

#### Time Plan

| Time | Activity |
|------|----------|
| 0:00–0:05 | Setup, test projector, arrange room |
| 0:05–1:30 | **Presentations** (~12 students at 10 min each) |
| 1:30–1:40 | Peer feedback forms (2 peers each) |
| 1:40–1:50 | **Course wrap-up:** key takeaways, where to go next, course evaluation |

#### Related Repository Resources

| Type | File | Purpose |
|------|------|---------|
| Project | `projects/capstone_presentation.md` | Presentation guide |
| Project | `projects/capstone_rubric.md` | Grading rubric |
| Assessment | `assessments/final_project_assessment.md` | Capstone assessment rubric |
| Post-course | `quizzes/post_course_assessment.md` | Growth measurement |

---

## CLO Coverage Matrix

Every CLO is covered by at least 3 sessions (lecture + lab + homework/assessment):

| CLO | Sessions | Labs | Assessment |
|-----|----------|------|------------|
| **CLO1** Explain core concepts | S01, S02, S05 | — | Q01, Q02, Q05, Midterm |
| **CLO2** Build interactive apps | S01, S02, S03 | L1 | A01, Q01–Q03 |
| **CLO3** Implement visualization | S04, S06 | L2 | A02, Q04, Q06 |
| **CLO4** Manage application state | S05, S06 | L2 | A02, Q05, Q06 |
| **CLO5** Optimize performance | S07 | — | Q08, Midterm |
| **CLO6** Design well-architected apps | S03, S08 | L3 | A03, Q03, Q09 |
| **CLO7** Connect to data sources | S09 | — | Q10, Midterm |
| **CLO8** Deploy ML models | S10, S11, S12 | L4 | A04, Q11–Q13, Practical Exam |
| **CLO9** Build AI-powered apps | S12, S13 | — | A03, Q13, Q14 |
| **CLO10** Test and secure apps | S14, S15 | — | A04, Q15, Q16, Final Practical |
| **CLO11** Deploy to production | S14, S15 | — | A04, Q15, Final Practical |
| **CLO12** Execute full lifecycle | S15, S16 | — | Capstone, Final Practical |

---

## Bloom's Taxonomy Progression

| Bloom's Level | Sessions Emphasized | Activities |
|---|---|---|
| **L1 Remember** | S01 | Terminology, API names |
| **L2 Understand** | S01, S02, S05 | Explain execution model, describe caching |
| **L3 Apply** | S02–S12 | Build apps, implement widgets, connect APIs |
| **L4 Analyze** | S07–S14 | Compare strategies, choose architecture, debug |
| **L5 Evaluate** | S11, S14, S15 | Review security, assess deployment, critique design |
| **L6 Create** | S15, S16 | Capstone project, design original application |

---

## Assessment Milestones

| Week | Assessment | Weight | CLOs |
|------|-----------|--------|------|
| 1–16 | Weekly Quizzes (best 14/16) | 10% | CLO1–CLO11 |
| 3 | Lab 1: Personal Dashboard | 3.3% | CLO2 |
| 3 | A01 Due: Personal Dashboard | 4% | CLO2, CLO6 |
| 6 | Lab 2: Interactive Dashboard | 3.3% | CLO3, CLO4 |
| 6 | A02 Due: Data Explorer | 4% | CLO3, CLO4 |
| 8 | Lab 3: Multipage Architecture | 3.4% | CLO6 |
| 9 | Mid-Course Assessment | 10% | CLO1–CLO7 |
| 11 | Lab 4: ML Prediction App | — | CLO8 |
| 12 | Practical Exam | 10% | CLO2–CLO8 |
| 13 | A03 Due: Multipage App | 4% | CLO6–CLO9 |
| 14 | A04 Due: ML Production App | 8% | CLO8–CLO11 |
| 15 | Final Practical Assessment | 15% | CLO2–CLO11 |
| 16 | Capstone Project + Presentation | 15% | CLO1–CLO12 |
| 1–16 | Participation | 5% | — |
| 1, 16 | Pre/Post Assessment | 5% | CLO1 |

---

## Pacing Adjustments

### If Behind Schedule
| Weeks Saved | Action |
|-------------|--------|
| 0.5 week | Combine S09 (APIs + Databases) into a faster session; assign one reading as homework |
| 1 week | Make S12 (NLP) lecture-only with demo; skip independent work |
| 1 week | Merge S14 and S15: cover security + deployment in one session, capstone work in the other |
| 0.5 week | Reduce Lab 3 time from 50 min to 30 min |

### If Ahead of Schedule
| Opportunity | Activity |
|-------------|----------|
| 0.5 week | Debugging workshop: review common mistakes from `common_student_mistakes.md` |
| 0.5 week | Mini-hackathon: build a simple app in 90 minutes using M04–M06 skills |
| 1 week | Early capstone proposal workshop |
| 0.5 week | Peer code review session |

---

## Related Materials

- [Course Plan](course_plan.md) — Weekly schedule overview
- [Teaching Roadmap](teaching_roadmap.md) — Module dependencies
- [Lab Activities](lab_activities.md) — Detailed lab task breakdowns
- [Common Mistakes](common_student_mistakes.md) — Error catalog by module
- [Assessment Strategy](assessment_strategy.md) — Grading policies and rubrics
- [Solution Guide](solution_guide.md) — Exercise solution walkthroughs
- [Curriculum](../docs/curriculum.md) — Full curriculum design
- [Learning Outcomes](../docs/learning_outcomes.md) — CLO definitions and traceability

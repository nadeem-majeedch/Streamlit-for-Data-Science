# 🔬 Lab Activities

> **Streamlit for Data Science — Learn, Build, Deploy**
> *Hands-on lab guides with timing, objectives, and solutions.*

---

## Lab Structure

Each lab is a **50-minute supervised practical session**. Students work on exercises or mini-projects while the instructor and TAs circulate to help.

| Phase | Time | Activity |
|-------|------|----------|
| Setup | 0:00–0:03 | Students open IDE, verify environment |
| Briefing | 0:03–0:08 | Review lab objectives, show expected outcome |
| Work | 0:08–0:40 | Students work on tasks, instructor helps |
| Review | 0:40–0:48 | Share solutions, discuss approaches |
| Wrap-up | 0:48–0:50 | Submit work, preview next lab |

---

## Lab 1 — Personal Dashboard (Week 3)

**Prerequisites:** M01–M03 (Fundamentals, Widgets, Layouts)
**Related Assignment:** A01 — Personal Dashboard (due this week)

### Objectives
- Build a complete dashboard from scratch
- Use sidebar, columns, tabs, and widgets together
- Apply dashboard design principles

### Activities

#### Task 1 (15 min): Build the Skeleton
Create a dashboard with:
- `st.set_page_config` with a custom title and icon
- Sidebar with at least 3 different widget types
- 3 columns displaying metric cards
- Tabs for different views

**Expected structure:**
```python
st.set_page_config(page_title="My Dashboard", page_icon="📊", layout="wide")

with st.sidebar:
    st.header("Filters")
    # 3+ widgets here

col1, col2, col3 = st.columns(3)
# Metric cards in columns

tab1, tab2, tab3 = st.tabs(["Overview", "Details", "About"])
# Content in tabs
```

#### Task 2 (15 min): Add Real Data
- Load a CSV file or create sample data with Pandas
- Display a DataFrame in one of the tabs
- Connect sidebar filters to the displayed data
- Show summary statistics

#### Task 3 (10 min): Polish
- Add a download button for filtered data
- Use `st.metric()` for KPI cards
- Add an expander for additional details
- Ensure the layout is readable

#### Bonus (10 min)
- Add a chart using `st.plotly_chart` or `st.line_chart`
- Use `st.session_state` to remember filter selections
- Add a "Reset Filters" button

### Common Issues & Solutions

| Issue | Cause | Fix |
|-------|-------|-----|
| Sidebar widgets don't affect main area | Filters not connected to data | Pass widget values to DataFrame filter |
| Columns look uneven | Content differs in length | Use `st.metric` for consistent card heights |
| Charts too small | Default size | Use `use_container_width=True` |

---

## Lab 2 — Interactive Dashboard (Week 6)

**Prerequisites:** M04–M06 (Data Display, Session State, File Upload)
**Related Assignment:** A02 — Data Explorer (due this week)

### Objectives
- Build a complete data exploration dashboard
- Handle file uploads and dynamic data
- Implement session state for persistence

### Activities

#### Task 1 (10 min): File Upload Pipeline
Create a file upload workflow:
- Accept CSV files
- Validate file type
- Display shape, columns, dtypes
- Show first 5 rows

#### Task 2 (15 min): Dynamic Filters
- Auto-detect column types (numeric, categorical, date)
- Create appropriate filters for each type
- Apply all filters simultaneously
- Show filtered row count

#### Task 3 (15 min): Visualization Suite
- Add 3 different chart types
- Let the user select which columns to plot
- Show a correlation matrix for numeric data
- Add summary statistics

#### Task 4 (10 min): Export & Polish
- Add a download button for filtered data
- Use session state to preserve filter state
- Add a data quality summary section
- Ensure graceful error handling

### Assessment Criteria
- ✅ File upload works with any valid CSV
- ✅ Filters are dynamic (not hardcoded columns)
- ✅ At least 3 chart types
- ✅ Download button works
- ✅ Error handling for empty files

---

## Lab 3 — Multipage App Architecture (Week 8)

**Prerequisites:** M07–M08 (Caching, Architecture)

### Objectives
- Refactor a single-file app into a multipage structure
- Use `st.navigation` for page routing
- Implement shared utilities

### Activities

#### Task 1 (15 min): Analyze and Plan
Given a 300-line `app.py` (provided), students:
- Identify logical sections (data loading, filtering, visualization, settings)
- Draw a page structure diagram
- List shared functions that belong in a utility module

#### Task 2 (20 min): Refactor
- Create `pages/` directory with 3+ page files
- Move shared logic to `utils/`
- Create `config.py` for settings
- Implement `st.navigation` in `app.py`
- Verify all pages still work

**Expected structure:**
```
my_app/
├── app.py              # Navigation only
├── config.py           # Constants, paths
├── utils/
│   ├── data.py         # Data loading functions
│   ├── charts.py       # Chart creation functions
│   └── formatting.py   # Display helpers
└── pages/
    ├── 1_📊_Overview.py
    ├── 2_📈_Analysis.py
    └── 3_⚙️_Settings.py
```

#### Task 3 (15 min): Add Caching
- Cache the data loading function
- Cache any expensive computations
- Add TTL to time-sensitive data
- Verify caching works (add a timer to prove it)

### Common Issues & Solutions

| Issue | Cause | Fix |
|-------|-------|-----|
| Pages can't access shared variables | No shared state | Use `st.session_state` or import from utils |
| `st.navigation` doesn't show pages | Pages not in `pages/` directory | Check file naming and location |
| Import errors between pages | Circular imports | Restructure imports, avoid circular dependencies |

---

## Lab 4 — ML Prediction App (Week 11)

**Prerequisites:** M11–M12 (ML Intro, ML Deployment)

### Objectives
- Build a complete ML prediction application
- Handle preprocessing correctly
- Implement input validation

### Activities

#### Task 1 (10 min): Train and Save
- Train a classification model on the Titanic dataset
- Save the model and preprocessing pipeline with `joblib`
- Verify the model loads correctly

#### Task 2 (15 min): Build Prediction UI
- Create input fields for all required features
- Validate inputs (check ranges, required fields)
- Load the model with `@st.cache_resource`
- Display prediction and probability

#### Task 3 (15 min): Batch Prediction
- Add file upload for batch predictions
- Validate uploaded file has correct columns
- Process all rows and display results
- Add a download button for predictions

#### Task 4 (10 min): Error Handling & Polish
- Handle missing model file gracefully
- Validate feature types match training data
- Add confidence thresholds
- Show model metadata (training date, accuracy)

### Key Validation Checklist
- ✅ Model loads without retraining on rerun
- ✅ Input validation catches invalid values
- ✅ Batch prediction handles edge cases
- ✅ Graceful error messages (no stack traces)
- ✅ Download button works for batch results

---

## Instructor Tips for Labs

### Before the Lab
- Test the environment on one student machine
- Have a backup dataset ready
- Prepare a "golden solution" to show at the end

### During the Lab
- Circulate every 5 minutes
- Ask "What have you tried?" before giving answers
- Note common struggles for the review phase
- Pair struggling students with those who are ahead

### After the Lab
- Collect submission links
- Note which tasks were hardest
- Update `common_student_mistakes.md` if new patterns emerge

---

## Related Materials

- [Session Plans](2_hour_lecture_plan.md) — Lecture companion
- [Exercise Guide](exercise_guide.md) — Grading notes
- [Common Mistakes](common_student_mistakes.md) — Error patterns
- [Assessment Strategy](assessment_strategy.md) — Lab grading rubrics

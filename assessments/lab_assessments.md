# Lab Assessments

> **🔬 Lab Assessments · In-Class Practical Sessions**
> *Hands-on assessments completed during lab sessions with instructor observation.*
> Total: 10% of course grade (3 labs × ~3.3% each)

---

## Lab 1: Streamlit Fundamentals Lab

> **Week 3 · Beginner · M01–M03**
> ⏱ Duration: 50 minutes · 📊 Points: 30

---

### Learning Outcomes

| CLO | Outcome | Bloom's | Marks |
|-----|---------|---------|-------|
| CLO1 | Explain Streamlit's execution model | Understand | 5 |
| CLO2 | Build interactive data applications | Apply | 20 |
| CLO2 | Use widgets, layouts, and state | Apply | 5 |

### Prerequisites

- Completed Modules 01–03
- Laptop with Python and Streamlit installed

### Scenario

You are a Data Science intern at a retail company. Your manager asks you to build a **quick prototype** of a product search tool that lets warehouse staff look up products by name, filter by category, and see stock levels.

**This is NOT a polished app** — it's a rapid prototype to demonstrate feasibility.

### Tasks

#### Task 1: Basic App Setup (5 marks)

1. Create a new file `lab1_product_search.py`
2. Set page config with title "Product Search Prototype"
3. Add a title and a brief description using markdown
4. Display a hardcoded list of 10 products as a DataFrame with columns: Name, Category, Price, Stock

**Deliverable:** Running app with product table displayed

---

#### Task 2: Interactive Filters (10 marks)

1. Add a sidebar with:
   - `st.text_input` for product name search (placeholder: "Search products...")
   - `st.selectbox` for category filter (options from the data)
   - `st.slider` for price range (min to max of the data)
2. Filter the DataFrame based on all three inputs
3. Display the filtered results
4. Show a metric card with the count of matching products

**Deliverable:** Working filters that update the displayed data

---

#### Task 3: Layout & Polish (10 marks)

1. Use `st.columns()` to display:
   - Left column (70%): Filtered product table
   - Right column (30%): Summary statistics (avg price, total stock, product count)
2. Add an expander with "Export Options" containing a `st.download_button` for CSV
3. Add a footer with your name and the date

**Deliverable:** Complete layout with columns, expander, and download

---

#### Task 4: Code Quality (5 marks)

- Functions used for data loading and filtering
- Comments explaining non-obvious sections
- No hardcoded magic numbers
- Clean, readable code

### Assessment Method

- **Live demo:** Student demonstrates app to instructor
- **Code review:** Instructor reviews submitted file
- **Q&A:** Instructor asks 1-2 follow-up questions about design choices

### Grading Rubric

| Criteria | Excellent (5) | Good (3-4) | Adequate (1-2) | Poor (0) |
|----------|---------------|------------|-----------------|----------|
| App runs | Runs perfectly | Minor issues | Major issues | Doesn't run |
| Filters work | All 3 filters correct | 2 filters work | 1 filter works | No filters |
| Layout | Columns + expander + download | Columns work | Partial layout | No layout |
| Code quality | Functions, comments, clean | Mostly clean | Some structure | No structure |

---

## Lab 2: Stateful Application Lab

> **Week 8 · Intermediate · M04–M06**
> ⏱ Duration: 50 minutes · 📊 Points: 30

---

### Learning Outcomes

| CLO | Outcome | Bloom's | Marks |
|-----|---------|---------|-------|
| CLO3 | Implement data visualization strategies | Apply | 10 |
| CLO4 | Design and manage application state | Apply | 15 |
| CLO2 | Handle file uploads and processing | Apply | 5 |

### Prerequisites

- Completed Modules 04–06
- Understanding of session state and file upload

### Scenario

You are building a **data quality checker** for your university's research lab. Researchers upload CSV files and the tool should:
- Show a preview of the data
- Report data quality issues (nulls, duplicates, types)
- Let them clean the data interactively
- Download the cleaned version

### Tasks

#### Task 1: File Upload & Preview (8 marks)

1. Create a `st.file_uploader` accepting CSV files
2. When a file is uploaded:
   - Display file name, size, and row/column count
   - Show first 5 rows with `st.dataframe()`
   - Show column names and data types
3. If no file is uploaded, show a helpful message with instructions

**Deliverable:** Working upload with preview

---

#### Task 2: Quality Report (10 marks)

After upload, create a quality report with:

1. **Overview tab:** Total rows, columns, null cells, duplicate rows, memory usage
2. **Nulls tab:** DataFrame showing each column's null count and percentage
3. **Types tab:** Column names, data types, non-null count, sample values
4. Use `st.tabs()` to organize the report

**Deliverable:** 3-tab quality report

---

#### Task 3: Interactive Cleaning (12 marks)

Build a cleaning interface with:

1. **Cleaning options** using checkboxes:
   - Remove duplicate rows
   - Standardize column names (lowercase, strip, replace spaces with underscores)
   - Drop columns with >50% null values
   - Fill remaining numeric nulls with median

2. **Before/After comparison** using tabs or columns:
   - Show original data shape vs cleaned shape
   - Show cleaning summary (what was changed)

3. **Download** the cleaned data as CSV

4. Use `st.session_state` to store cleaning choices

**Deliverable:** Interactive cleaning with before/after comparison and download

---

### Assessment Method

- **Live demo** with instructor testing edge cases
- **Code review** for session state usage and function organization
- **Stress test:** Instructor uploads a file with many nulls/duplicates

---

## Lab 3: ML Deployment Lab

> **Week 13 · Advanced · M10–M12**
> ⏱ Duration: 50 minutes · 📊 Points: 30

---

### Learning Outcomes

| CLO | Outcome | Bloom's | Marks |
|-----|---------|---------|-------|
| CLO7 | Connect to databases | Apply | 5 |
| CLO8 | Deploy ML models as interactive apps | Apply | 20 |
| CLO6 | Design well-structured applications | Analyze | 5 |

### Prerequisites

- Completed Modules 10–12
- Scikit-learn basics, SQLite, joblib

### Scenario

Your team has trained a **customer churn prediction model**. You need to build a Streamlit app that:
- Loads the pre-trained model
- Lets business analysts input customer features
- Shows predictions with confidence
- Accepts batch predictions from CSV upload
- Displays model information

### Setup

The instructor provides a pre-trained model file (`churn_model.joblib`) and scaler (`churn_scaler.joblib`). Student must NOT retrain.

### Tasks

#### Task 1: Model Loading & Info (5 marks)

1. Load the model and scaler using `@st.cache_resource`
2. Display model metadata: type, feature count, accuracy
3. Handle the case where model files are missing (show error, stop)

**Deliverable:** Model loads correctly, info displayed

---

#### Task 2: Single Prediction (10 marks)

1. Create input widgets for 5 customer features:
   - `tenure_months` (slider: 1–72)
   - `monthly_charges` (slider: 20–120)
   - `total_charges` (number_input)
   - `contract_type` (selectbox: Month-to-month, One year, Two year)
   - `payment_method` (selectbox: Electronic check, Mailed check, Bank transfer, Credit card)

2. Validate inputs (no negative values, required fields)

3. On "Predict" button click:
   - Preprocess with saved scaler (NOT fit_transform)
   - Show predicted class (Churn/No Churn)
   - Show probability for each class
   - Display prediction in a styled card

**Deliverable:** Working single prediction with validation

---

#### Task 3: Batch Prediction (10 marks)

1. Create a file uploader for CSV
2. Validate that uploaded CSV has expected columns
3. Process all rows through the model
4. Add prediction and probability columns to the DataFrame
5. Display results with `st.dataframe()`
6. Add download button for results CSV

**Deliverable:** Batch prediction with validation and download

---

#### Task 4: Code Quality (5 marks)

- Model loaded with caching (not retrained)
- Preprocessing consistent (transform, not fit_transform)
- Error handling for missing files and bad inputs
- Functions separated from UI code

---

## Lab Assessment Summary

| Lab | Week | Topics | Marks | Duration |
|-----|------|--------|-------|----------|
| Lab 1 | 3 | Fundamentals, widgets, layouts | 30 | 50 min |
| Lab 2 | 8 | Visualization, state, file handling | 30 | 50 min |
| Lab 3 | 13 | Database, ML deployment, architecture | 30 | 50 min |
| **Total** | | | **90** | **150 min** |

---

## Lab Assessment Strategy

### During Lab
1. Instructor circulates and observes progress
2. Students work individually
3. Instructor may ask clarifying questions
4. Students submit via GitHub before lab ends

### After Lab
1. Code review within 48 hours
2. Feedback provided via GitHub comments
3. Grades posted within 1 week

### Academic Integrity
- Students may NOT copy from notebooks or other students
- Instructor may ask students to explain their code
- Inconsistent code quality triggers a follow-up interview

---

## Related Materials

- 📋 Curriculum: [docs/curriculum.md](../docs/curriculum.md)
- 📋 Learning Outcomes: [docs/learning_outcomes.md](../docs/learning_outcomes.md)
- ✏️ Exercises: [exercises/](../exercises/)

# Practical Exam

> **🎯 Practical Examination · Week 12**
> *Timed coding assessment: build a functional Streamlit application under exam conditions.*
> ⏱ Duration: 3 hours · 📊 Total: 100 marks · Difficulty: ★★★★☆

---

## Course Information

| Field | Detail |
|-------|--------|
| **Course** | Streamlit for Data Science |
| **Assessment** | Practical Examination |
| **Weight** | 10% of course grade |
| **Duration** | 3 hours (180 minutes) |
| **Type** | Individual, timed, supervised |
| **Environment** | Local machine with Python 3.10+ and Streamlit installed |

---

## Learning Outcomes Assessed

| CLO | Outcome | Bloom's | Marks |
|-----|---------|---------|-------|
| CLO2 | Build interactive data applications | Apply | 25 |
| CLO3 | Implement data visualization | Apply | 15 |
| CLO4 | Manage application state | Apply | 15 |
| CLO5 | Optimize performance | Analyze | 10 |
| CLO8 | Deploy ML models | Apply | 20 |
| CLO6 | Design well-structured applications | Analyze | 15 |

---

## Instructions

1. You have **3 hours** to complete this exam
2. You may use **Python documentation** and **Streamlit documentation** (offline copies provided)
3. You may **NOT** access the internet, notebooks, or other course materials
4. You may **NOT** copy code from memory of course exercises
5. All code must be in a single directory with proper file structure
6. **Submit** your directory as a ZIP file before time expires
7. Your app must **run without errors** using `streamlit run app.py`

---

## Scenario

You are a Data Scientist at a healthcare startup. The CTO has asked you to build a **Patient Risk Assessment Dashboard** that:

1. Loads patient data from a CSV
2. Lets clinicians filter and explore the data
3. Trains a simple risk prediction model
4. Allows single-patient risk prediction
5. Supports batch prediction from uploaded files
6. Displays model performance metrics

The dataset is provided at the start of the exam.

---

## Dataset

Create a synthetic patient dataset (provided as a starter file):

```python
# exam_data.py — Students may import this but NOT modify it
import pandas as pd
import numpy as np

np.random.seed(42)
n = 500

df = pd.DataFrame({
    "patient_id": [f"P{i:04d}" for i in range(1, n+1)],
    "age": np.random.randint(18, 85, n),
    "gender": np.random.choice(["Male", "Female"], n),
    "bmi": np.random.uniform(18, 40, n).round(1),
    "blood_pressure_systolic": np.random.randint(90, 180, n),
    "cholesterol": np.random.randint(150, 300, n),
    "glucose": np.random.randint(70, 200, n),
    "smoking": np.random.choice(["Yes", "No"], n, p=[0.3, 0.7]),
    "exercise_hours_weekly": np.random.uniform(0, 10, n).round(1),
    "family_history": np.random.choice(["Yes", "No"], n, p=[0.4, 0.6]),
})

# Risk score based on factors (not provided to students)
risk_factors = (
    (df["age"] > 50).astype(int) * 2 +
    (df["bmi"] > 30).astype(int) * 2 +
    (df["blood_pressure_systolic"] > 140).astype(int) * 2 +
    (df["cholesterol"] > 240).astype(int) * 1 +
    (df["glucose"] > 126).astype(int) * 2 +
    (df["smoking"] == "Yes").astype(int) * 2 +
    (df["exercise_hours_weekly"] < 2).astype(int) * 1 +
    (df["family_history"] == "Yes").astype(int) * 1
)
df["risk_level"] = pd.cut(risk_factors, bins=[-1, 3, 6, 100], labels=["Low", "Medium", "High"])
```

---

## Tasks

### Task 1: Data Loading & Exploration (15 marks)

1. (3 marks) Load the dataset and display basic info (shape, dtypes, head)
2. (4 marks) Build sidebar filters:
   - Age range (slider)
   - Gender (selectbox)
   - Risk level (multiselect)
   - Smoking status (radio)
3. (4 marks) Apply filters and show filtered row count
4. (4 marks) Display 4 KPI metrics: Total Patients, Avg Age, High Risk Count, Avg BMI

---

### Task 2: Visualization Dashboard (15 marks)

1. (5 marks) Create a tabbed view with 3 tabs:
   - "Demographics": Age distribution histogram + gender breakdown bar chart
   - "Risk Factors": Box plots of BMI and blood pressure by risk level
   - "Correlations": Scatter plot of BMI vs Cholesterol, colored by risk level

2. (5 marks) Use `st.columns()` for side-by-side charts where appropriate

3. (5 marks) All charts update when sidebar filters change

---

### Task 3: ML Model (25 marks)

1. (5 marks) Train a RandomForest classifier:
   - Features: age, bmi, blood_pressure_systolic, cholesterol, glucose, exercise_hours_weekly
   - Target: risk_level
   - Use `train_test_split` with `test_size=0.2, random_state=42`

2. (5 marks) Save the model and scaler using `joblib`

3. (10 marks) Single prediction interface:
   - Input widgets for all features
   - Preprocess with saved scaler (NOT fit_transform)
   - Show predicted risk level and probabilities
   - Handle edge cases (out-of-range values)

4. (5 marks) Display model info: accuracy, feature importances (bar chart)

---

### Task 4: Batch Prediction (10 marks)

1. (3 marks) File uploader for CSV with expected columns
2. (3 marks) Validate uploaded file columns
3. (2 marks) Process all rows through the model
4. (2 marks) Display results and download as CSV

---

### Task 5: Session State & UX (10 marks)

1. (3 marks) Filter selections persist across reruns
2. (3 marks) Loading spinner shown during model training
3. (2 marks) Clear error messages for invalid inputs
4. (2 marks) Overall UX is intuitive (labels, descriptions, flow)

---

### Task 6: Architecture & Code Quality (15 marks)

1. (5 marks) Code organized into functions (not one giant script)
2. (5 marks) Model training separate from UI code
3. (3 marks) `st.set_page_config()` as first Streamlit call
4. (2 marks) No hardcoded file paths or magic numbers

---

### Task 7: Documentation (10 marks)

1. (3 marks) README.md with app description and how to run
2. (3 marks) Screenshot of the running app
3. (2 marks) List of features implemented
4. (2 marks) Any limitations or known issues

---

## Submission

```
practical_exam/
├── app.py                    # Main application
├── exam_data.py              # Provided data (do NOT modify)
├── requirements.txt          # Dependencies
├── README.md                 # Documentation
├── screenshots/
│   └── app_screenshot.png
└── models/                   # Saved model artifacts
    ├── model.joblib
    └── scaler.joblib
```

---

## Marking Guide

| Task | Marks | Bloom's | Key Criteria |
|------|-------|---------|--------------|
| 1. Data Loading | 15 | Apply | Filters work, data displays correctly |
| 2. Visualization | 15 | Apply | Charts render, tabs work, update with filters |
| 3. ML Model | 25 | Apply, Analyze | Model trains, prediction works, preprocessing correct |
| 4. Batch Prediction | 10 | Apply | Upload, validate, predict, download |
| 5. Session State | 10 | Apply | State persists, UX is smooth |
| 6. Architecture | 15 | Analyze | Functions, separation, clean code |
| 7. Documentation | 10 | Understand | README, screenshots, description |
| **Total** | **100** | | |

---

## Grade Boundaries

| Grade | Score | Description |
|-------|-------|-------------|
| A | 85–100 | Complete app with ML, good architecture |
| B | 70–84 | Working app with most features |
| C | 55–69 | Partial app, basic functionality |
| D | 40–54 | Minimal functionality, major issues |
| F | < 40 | Does not run or minimal submission |

---

## Common Mistakes to Avoid

1. ❌ Training model on every rerun (use caching)
2. ❌ Using `fit_transform` at inference (use `transform` only)
3. ❌ Forgetting `st.set_page_config()` as first call
4. ❌ All code in one giant script with no functions
5. ❌ No error handling for file upload or predictions
6. ❌ Charts that don't update with filter changes
7. ❌ Missing requirements.txt

---

## Answer Key

> ⚠️ **Instructor copy — do not distribute**
> Reference implementation available in `assessments/rubrics/practical_exam_reference/`

---

## Related Materials

- 📋 Curriculum: [docs/curriculum.md](../docs/curriculum.md)
- 📋 Learning Outcomes: [docs/learning_outcomes.md](../docs/learning_outcomes.md)
- ✏️ Exercise: [15 — ML Workshop](../exercises/15_ml_workshop.py)
- 🖥️ Demo: [15 — Classification App](../apps/15_classification_app.py)

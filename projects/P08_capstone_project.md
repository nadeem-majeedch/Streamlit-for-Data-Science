# P08 — Capstone Project: Full-Stack Data Science Application

> **🚀 Project · Module 16 — Capstone**
> *Build, test, and deploy a complete Streamlit data science application.*

---

## Overview

Build a production-quality Streamlit application that demonstrates mastery of all course concepts. The application must be deployable, well-documented, and include tests.

**Duration:** 3 weeks
**Team Size:** 1–2 students
**Weight:** 15% of course grade

---

## Learning Outcomes

By completing this project you will demonstrate:

1. **Architecture** — Clean separation of UI, data, and business logic
2. **Widgets & State** — Interactive controls with proper session state management
3. **Visualization** — Multiple chart types with clear data communication
4. **Caching** — Performance optimization with `@st.cache_data` and `@st.cache_resource`
5. **Data Processing** — Upload, validate, clean, transform, and analyze data
6. **Security** — Secrets management, input validation, safe file handling
7. **Deployment** — Successfully deployed on Streamlit Community Cloud
8. **Documentation** — Comprehensive README and code documentation

---

## Requirements

### Functional Requirements

Your application must:

1. **Load or accept data** from at least one source (file upload, database, API, or built-in dataset)
2. **Process and transform** the data using Pandas/NumPy
3. **Display results** using at least 3 different visualization types
4. **Provide interactive controls** (sidebar filters, forms, or parameter inputs)
5. **Show KPIs/metrics** relevant to the data domain
6. **Include at least one ML model** (classification or regression) with:
   - Feature input UI
   - Prediction output with confidence scores
   - Model information display
7. **Allow data export** (download processed data or results)
8. **Handle errors gracefully** — no crashes on invalid input

### Technical Requirements

1. **Modular structure** — No single `app.py` with all code (use functions, modules, or pages)
2. **Session state** — Persistent state where needed (filter selections, prediction history)
3. **Caching** — Expensive computations cached appropriately
4. **Secrets** — If using external APIs, configure via `st.secrets`
5. **requirements.txt** — All dependencies listed
6. **.gitignore** — Secrets, cache, and large files excluded

### Deployment Requirements

1. **Successfully deployed** on Streamlit Community Cloud
2. **Public URL** working and accessible
3. **No hardcoded secrets** in source code
4. **App loads** within 30 seconds (cold start)
5. **All features work** in the deployed version

### Documentation Requirements

1. **README.md** with:
   - Project title and description
   - Features list
   - Screenshots (at least 2)
   - Setup instructions
   - Deployment link
   - Data sources
   - Author information
2. **Code comments** — Key functions documented
3. **In-line explanations** — Complex logic explained

---

## Project Ideas

### Domain-Specific Options

| Domain | Example Project | Key Features |
|--------|----------------|--------------|
| Healthcare | Patient Risk Calculator | Symptom input, risk score, data visualization |
| Finance | Portfolio Analyzer | Stock data, charts, risk metrics |
| Environment | Air Quality Dashboard | Map, time series, predictions |
| Education | Student Performance Tracker | Upload grades, trends, predictions |
| Retail | Sales Forecasting App | Historical data, predictions, KPIs |
| Sports | Player Statistics Explorer | Search, compare, visualize |

### Template Projects

If no domain is chosen, use one of these templates:

1. **Multi-Source Data Explorer** — Upload CSV/Excel/JSON, visualize, analyze, predict
2. **ML Model Dashboard** — Train/compare models, interactive predictions
3. **Text Analysis Tool** — Upload documents, sentiment analysis, word clouds

---

## Implementation Guide

### Week 1: Planning & Core Functionality

- [ ] Choose domain and data sources
- [ ] Design application architecture (draw a diagram)
- [ ] Set up project structure (modules, pages, components)
- [ ] Implement data loading and processing
- [ ] Build basic UI layout

### Week 2: Features & Polish

- [ ] Add interactive widgets and controls
- [ ] Implement visualizations
- [ ] Add ML model(s) with prediction UI
- [ ] Implement session state for persistence
- [ ] Add caching for performance
- [ ] Handle error cases

### Week 3: Testing & Deployment

- [ ] Write tests using `st.testing.AppTest`
- [ ] Fix any bugs found in testing
- [ ] Prepare README with screenshots
- [ ] Deploy to Community Cloud
- [ ] Verify all features work in deployed version
- [ ] Final polish and code review

---

## Testing Requirements

Your project must include at least:

1. **Unit tests** for data processing functions (using pytest)
2. **App tests** using `st.testing.AppTest`:
   - Test page loads without error
   - Test widget interactions
   - Test form submissions
   - Test file uploads (if applicable)

### Example App Test

```python
import pytest
from streamlit.testing.v1 import AppTest

def test_app_loads():
    at = AppTest.from_file("app.py")
    at.run()
    assert not at.exception

def test_sidebar_filter():
    at = AppTest.from_file("app.py")
    at.run()
    # Interact with sidebar
    at.selectbox[0].set_value("Option A")
    at.run()
    assert at.dataframe[0].value is not None

def test_prediction():
    at = AppTest.from_file("app.py")
    at.run()
    # Fill in feature inputs
    at.number_input[0].set_value(5.0)
    at.run()
    assert at.success[0].value == "Prediction: ..."
```

---

## Grading Rubric

| Component | Points | Criteria |
|-----------|--------|----------|
| **Functionality** | 30 | All requirements met, features work correctly |
| **Code Quality** | 20 | Clean, modular, well-documented code |
| **UI/UX Design** | 15 | Intuitive layout, clear visualizations, good UX |
| **Data Processing** | 15 | Proper validation, cleaning, transformation |
| **Deployment** | 10 | Successfully deployed, loads fast, no errors |
| **Documentation** | 5 | Clear README, code comments, screenshots |
| **Testing** | 5 | Unit tests and app tests present |
| **Total** | **100** | |

### Grade Boundaries

| Grade | Score | Description |
|-------|-------|-------------|
| A | 90–100 | Exceptional — production-ready quality |
| B | 80–89 | Strong — all requirements met with some polish |
| C | 70–79 | Satisfactory — most requirements met |
| D | 60–69 | Below expectations — missing key features |
| F | < 60 | Incomplete — fails to meet basic requirements |

---

## Common Mistakes

1. **❌ No error handling** — App crashes on invalid input
2. **❌ All code in one file** — 500+ lines in `app.py`
3. **❌ No caching** — Slow performance on every rerun
4. **❌ Hardcoded paths** — Works locally but breaks in cloud
5. **❌ Missing requirements** — Build fails on Community Cloud
6. **❌ No tests** — Code quality unverified
7. **❌ Poor README** — No screenshots, no setup instructions
8. **❌ Secrets in code** — API keys visible in source

---

## Submission

### What to Submit

1. **GitHub Repository URL** (deployed app link in README)
2. **README.md** with screenshots and deployment link
3. **Live deployment URL** on Community Cloud

### Submission Checklist

- [ ] Repository is public (or shared with instructor)
- [ ] App is deployed and accessible via URL
- [ ] README is complete with screenshots
- [ ] All tests pass locally
- [ ] No hardcoded secrets
- [ ] `requirements.txt` is correct
- [ ] Code is clean and documented

---

## Related Materials

- 📖 Reading: [Application Architecture](../readings/13_application_architecture.md)
- 📖 Reading: [Deployment Guide](../readings/deployment_guide.md)
- 📋 Checklist: [Deployment Checklist](../docs/deployment_checklist.md)
- 🖥️ Example: [Deployable App](../apps/deployable_app/)
- 📓 Notebook: [Deployment Tutorial](../notebooks/deployment_tutorial.ipynb)

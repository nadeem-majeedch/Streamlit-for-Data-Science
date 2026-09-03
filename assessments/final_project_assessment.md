# Final Project Assessment (Capstone)

> **🚀 Capstone Project · Week 16 · End of Course**
> *Comprehensive project demonstrating mastery of all course learning outcomes.*
> ⏱ Duration: 3 weeks (assigned Week 13, due Week 16) · 📊 Total: 200 marks · Difficulty: ★★★★★

---

## Course Information

| Field | Detail |
|-------|--------|
| **Course** | Streamlit for Data Science |
| **Assessment** | Capstone Project (P08) |
| **Weight** | 15% of course grade |
| **Duration** | 3 weeks development + final presentation |
| **Type** | Individual (or pair, max 2 students) |
| **Deliverables** | Application, documentation, presentation, deployment |

---

## Learning Outcomes Assessed

| CLO | Outcome | Bloom's | Marks |
|-----|---------|---------|-------|
| CLO1 | Explain Streamlit's execution model | Understand | 10 |
| CLO2 | Build interactive data applications | Apply | 25 |
| CLO3 | Implement data visualization | Apply | 20 |
| CLO4 | Manage application state | Apply | 15 |
| CLO5 | Optimize performance | Analyze | 15 |
| CLO6 | Design well-structured applications | Analyze | 20 |
| CLO7 | Connect to data sources | Apply | 15 |
| CLO8 | Deploy ML models | Apply | 25 |
| CLO9 | Build AI-powered applications | Apply | 15 |
| CLO10 | Apply testing and security | Evaluate | 15 |
| CLO11 | Deploy to production | Evaluate | 15 |
| CLO12 | Execute full development lifecycle | Create | 10 |
| **Total** | | | **200** |

---

## Prerequisites

- Completed all 16 modules
- All assignments submitted
- Community Cloud account set up
- GitHub repository ready

---

## Project Requirements

### Core Requirements (100 marks)

Build a **complete, deployed Streamlit application** that solves a real-world Data Science problem. The application must demonstrate mastery of the full course curriculum.

#### 1. Application Functionality (40 marks)

| Requirement | Marks | Description |
|-------------|-------|-------------|
| Data loading | 5 | Load from file, API, or database with error handling |
| Interactive filters | 8 | Sidebar controls that update all views |
| KPI metrics | 7 | At least 4 relevant KPIs with formatting |
| Visualization | 10 | At least 4 different chart types, responsive to filters |
| ML/AI component | 10 | At least one model with prediction interface |

#### 2. Architecture & Code Quality (30 marks)

| Requirement | Marks | Description |
|-------------|-------|-------------|
| Modular structure | 10 | Separate files for data, UI, logic (not one giant script) |
| Functions | 8 | All logic in functions, not top-level code |
| Error handling | 7 | Graceful failure for all edge cases |
| Code style | 5 | PEP 8, docstrings, type hints, no magic numbers |

#### 3. State & Performance (20 marks)

| Requirement | Marks | Description |
|-------------|-------|-------------|
| Session state | 8 | Proper use of session_state for persistence |
| Caching | 7 | `@st.cache_data` and `@st.cache_resource` used correctly |
| Performance | 5 | App loads in <15 seconds, interactions respond in <3 seconds |

#### 4. Deployment (10 marks)

| Requirement | Marks | Description |
|-------------|-------|-------------|
| Deployed | 5 | Live on Community Cloud, accessible via URL |
| No errors | 5 | All features work in deployed version |

---

### Extended Requirements (60 marks)

#### 5. Testing & Security (20 marks)

| Requirement | Marks | Description |
|-------------|-------|-------------|
| Unit tests | 5 | At least 3 tests for data/logic functions |
| AppTest | 5 | At least 2 `st.testing.AppTest` tests |
| All tests pass | 5 | `pytest tests/ -v` passes cleanly |
| Security | 5 | No hardcoded secrets, validated inputs, safe SQL |

#### 6. Documentation (20 marks)

| Requirement | Marks | Description |
|-------------|-------|-------------|
| README | 5 | Complete with description, setup, features |
| Screenshots | 5 | At least 4 screenshots showing different views |
| Architecture | 5 | File structure diagram and explanation |
| Limitations | 5 | Known issues, future improvements |

#### 7. Innovation & Polish (20 marks)

| Requirement | Marks | Description |
|-------------|-------|-------------|
| Creative feature | 5 | At least one feature not taught in class |
| UX design | 5 | Intuitive navigation, clear labels, professional look |
| Responsive | 5 | Works on different screen sizes |
| Accessibility | 5 | Good contrast, readable fonts, meaningful labels |

---

### Presentation (40 marks)

#### 8. Live Demonstration (25 marks)

| Criteria | Marks | Description |
|----------|-------|-------------|
| App walkthrough | 10 | Demonstrate all major features |
| Architecture explanation | 8 | Explain design decisions and trade-offs |
| Technical depth | 7 | Answer questions about implementation details |

#### 9. Reflection (15 marks)

| Criteria | Marks | Description |
|----------|-------|-------------|
| What you learned | 5 | Key takeaways from the project |
| Challenges faced | 5 | Technical challenges and how you solved them |
| Future improvements | 5 | What you would do differently |

---

## Project Topics

Students may choose any domain, but the project must include:
1. A real or realistic dataset
2. Interactive filtering
3. Visualization
4. An ML/AI component
5. Deployment

### Suggested Topics

| Domain | Example Project | Key Features |
|--------|----------------|--------------|
| Healthcare | Patient Risk Dashboard | Prediction, trends, batch analysis |
| Finance | Stock Portfolio Tracker | Real-time data, charts, alerts |
| Education | Student Performance Analytics | Filters, predictions, reports |
| Environment | Air Quality Monitor | Time series, maps, alerts |
| Retail | Customer Segmentation Tool | Clustering, batch analysis |
| Sports | Player Performance Analyzer | Comparison, predictions |
| Social Media | Sentiment Analysis Dashboard | NLP, text processing |

---

## Timeline

| Week | Milestone | Deliverable |
|------|-----------|-------------|
| 13 | Project assigned | Topic selection, project plan |
| 14 | Development sprint 1 | Core functionality working |
| 15 | Development sprint 2 | Testing, documentation, deployment |
| 16 | Submission + Presentation | Final submission, 10-min presentation |

### Milestone 1: Project Plan (Due end of Week 13)
- Topic selection and justification
- Dataset description
- Feature list (prioritized)
- Architecture diagram
- Timeline with milestones

### Milestone 2: Working Prototype (Due end of Week 14)
- Core data loading and filtering
- At least 2 visualizations
- Basic ML component (can be simplified)
- Runs locally without errors

### Milestone 3: Final Submission (Due end of Week 16)
- Complete application deployed
- All tests passing
- Documentation complete
- Presentation prepared

---

## Submission Checklist

```
capstone_project/
├── app.py                    # Main entry point
├── config.py                 # Configuration
├── data_loader.py            # Data functions
├── components.py             # UI components
├── model_utils.py            # ML functions
├── requirements.txt          # Dependencies
├── .gitignore                # Ignored files
├── README.md                 # Documentation
├── pages/                    # Multipage structure
│   ├── __init__.py
│   ├── home.py
│   ├── explore.py
│   ├── predict.py
│   └── about.py
├── tests/                    # Test suite
│   ├── __init__.py
│   ├── test_data.py
│   ├── test_model.py
│   └── test_app.py
├── models/                   # Saved artifacts
│   └── .gitkeep
└── screenshots/              # Documentation images
    ├── overview.png
    ├── explore.png
    ├── predict.png
    └── deployed.png
```

### Submission Links
1. GitHub repository URL
2. Community Cloud deployment URL
3. Project plan (Milestone 1)
4. Presentation slides (if used)

---

## Marking Rubric

### Grade Boundaries

| Grade | Score | Percentage | Description |
|-------|-------|------------|-------------|
| A+ | 185–200 | 92.5–100% | Exceptional: innovative, production-ready, well-presented |
| A | 170–184 | 85–92% | Excellent: complete, deployed, well-tested |
| A- | 160–169 | 80–85% | Very Good: strong app, minor gaps |
| B+ | 145–159 | 72.5–80% | Good: working app, some gaps in testing/polish |
| B | 130–144 | 65–72.5% | Satisfactory: functional but incomplete |
| B- | 115–129 | 57.5–65% | Adequate: basic functionality, significant gaps |
| C+ | 100–114 | 50–57.5% | Marginal: partial app, major features missing |
| C | 80–99 | 40–50% | Below expectations: minimal functionality |
| D | 60–79 | 30–40% | Poor: app doesn't work properly |
| F | < 60 | < 30% | Failing: no submission or non-functional |

---

## Academic Integrity

### Acceptable
- Using course materials as reference
- Using official documentation
- Using Stack Overflow for syntax help
- Using AI assistants for code snippets (must declare)

### NOT Acceptable
- Copying code from other students
- Submitting someone else's project
- Using pre-built Streamlit templates without understanding
- Plagiarizing documentation

### Declaration
All submissions must include an academic integrity declaration:

```
I declare that this project is my own work. I have not copied
code from other students or unauthorized sources. I have used
AI assistants only for [specific purpose] and understand all
code I have submitted.
```

---

## Answer Key

> ⚠️ **Instructor copy — do not distribute**
> Grading rubric with point allocation in `assessments/rubrics/capstone_rubric.md`
> Sample projects and exemplary work in `assessments/rubrics/exemplary_projects/`

---

## Related Materials

- 📋 Project Spec: [projects/P08_capstone_project.md](../projects/P08_capstone_project.md)
- 📋 Deployment Checklist: [docs/deployment_checklist.md](../docs/deployment_checklist.md)
- 📋 Security Guide: [docs/security.md](../docs/security.md)
- 📋 Curriculum: [docs/curriculum.md](../docs/curriculum.md)

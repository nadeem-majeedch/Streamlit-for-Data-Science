# Streamlit for Data Science — Learn, Build, Deploy

> A comprehensive, hands-on course for building interactive Data Science, Machine Learning, and AI applications with Streamlit — from first app to production deployment.

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Streamlit](https://img.shields.io/badge/streamlit-%E2%89%A5%201.44-FF4B4B.svg)](https://streamlit.io)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

---

## 🎯 What This Course Covers

This repository contains everything needed to teach or self-study a **16-week university course** on building production-quality data apps with Streamlit. Students progress from "Hello World" to deploying full-stack ML/AI applications.

### Course Roadmap

The course is organized into **6 progression levels** across **16 modules**:

| Level | Modules | Weeks | Bloom's Focus |
|---|---|---|---|
| **[Beginner](docs/curriculum.md#level-1--beginner)** | M01 Fundamentals · M02 Widgets · M03 Layouts | 1–3 | Remember, Understand |
| **[Intermediate](docs/curriculum.md#level-2--intermediate)** | M04 Visualization · M05 Session State · M06 Forms & Files | 4–6 | Understand, Apply |
| **[Advanced](docs/curriculum.md#level-3--advanced)** | M07 Caching · M08 Multipage · M09 Architecture | 7–9 | Apply, Analyze |
| **[Machine Learning](docs/curriculum.md#level-4--machine-learning)** | M10 Databases · M11 APIs · M12 ML Deployment | 10–12 | Analyze, Evaluate |
| **[AI / NLP / LLM](docs/curriculum.md#level-5--ainlp--llm)** | M13 Chat, RAG & LLM Apps | 13 | Analyze, Create |
| **[Deployment & Production](docs/curriculum.md#level-6--deployment--production)** | M14 Testing & Security · M15 Cloud Deploy · M16 Maintenance | 14–16 | Evaluate, Create |

> 📋 **[Full Curriculum](docs/curriculum.md)** · **[Visual Roadmap](docs/roadmap.md)** · **[Learning Outcomes](docs/learning_outcomes.md)**

---

## 👥 Target Audience

| Who | Why |
|---|---|
| **BS Data Science / AI / CS students** (3rd–4th year) | Primary audience — builds on existing Python + ML knowledge |
| **Graduate students** | Rapid prototyping for research dashboards |
| **Industry professionals** | Transitioning from Jupyter notebooks to shareable apps |
| **Hackathon teams** | Fast UI layer for ML/AI demos |

### Prerequisites

**Hard requirements** — students must know:
- Python 3.10+ (functions, classes, file I/O, virtual environments)
- NumPy & Pandas (arrays, DataFrames, groupby, merge)
- Matplotlib or Plotly (basic charts)
- Introductory ML (train/test split, fit/predict, classification metrics)
- Git fundamentals (clone, commit, push, pull, branch)

**Soft requirements** (helpful but not mandatory):
- SQL basics (used in Module 10)
- REST API concepts (used in Module 11)
- Docker basics (used in Module 15)

---

## 🧠 Learning Philosophy

Every topic follows a **10-stage learning cycle**:

```
Concept → Intuition → Visual Explanation → Example → Code → Run
→ Experiment → Exercise → Assessment → Real-world Application
```

**Design principles:**
- **Progressive complexity** — each module builds on the last
- **Reproducibility first** — everything runs from `pip install -r requirements.txt`
- **Authentic data** — real-world datasets, not synthetic toys
- **Production mindset from Day 1** — folder structure, secrets, version control
- **≥ 70% hands-on** — students write more code than they listen to lectures

---

## 📁 Repository Navigation

```
Streamlit-for-Data-Science/
│
├── docs/                    📚 Course blueprint, syllabus, cheatsheets
│   ├── course_blueprint.md            # Internal course planning
│   ├── curriculum.md                  # Full curriculum details
│   ├── roadmap.md                     # Visual course progression
│   ├── learning_outcomes.md           # Learning outcomes & CLO mapping
│   ├── deployment_checklist.md       # Pre-deployment checklist & verification
│   ├── deployment_troubleshooting.md # Common deployment issues and solutions
│   └── security.md                    # Security guide & best practices
├── readings/                📖 Conceptual readings
│   ├── 01_streamlit_introduction.md   # What is Streamlit, comparisons
│   ├── 02_first_streamlit_app.md      # Installation, first app, execution model
│   ├── 03_streamlit_widgets_and_input.md  # All widget types, forms, validation
│   ├── 04_widget_keys_and_behavior.md # Keys, identity, session_state, callbacks
│   ├── 05_layouts_and_containers.md  # Sidebar, columns, tabs, expanders, containers
│   ├── 06_dashboard_design_ui_ux.md  # Status, metrics, accessibility, DS dashboard design
│   ├── 07_data_display_dataframes.md # st.dataframe, column_config, Styler, filtering
│   ├── 08_visualization_matplotlib_plotly.md # Native charts, Matplotlib, Plotly, chart selection
│   ├── 09_file_upload_and_processing.md    # st.file_uploader, validation, cleaning, download
│   ├── 10_interactive_dashboard.md         # Dashboard architecture, filters, KPIs, layout
│   ├── 11_session_state_and_execution.md  # Reruns, session state, multi-step workflows
│   ├── 12_caching_and_performance.md     # @st.cache_data, @st.cache_resource, TTL, invalidation
│   ├── 13_application_architecture.md   # Architecture, modules, multipage, testing
│   ├── 14_databases_and_persistence.md  # SQLite, SQL, CRUD, secrets, SQL injection
│   ├── 15_machine_learning_streamlit.md # ML deployment, preprocessing, classification, regression
│   ├── 17_nlp_ai_applications.md      # NLP, text classification, sentiment analysis, TF-IDF
│   ├── 18_llm_rag_applications.md    # LLM architecture, RAG, chat, streaming, security
│   ├── deployment_guide.md            # Deployment workflow, Community Cloud, secrets, troubleshooting
│   └── security_and_secrets.md       # Security best practices, secrets, validation, SQL injection
├── notebooks/               📓 Jupyter notebooks (primary learning)
│   ├── 01_Streamlit_Introduction.ipynb # Concepts, comparisons, intuition
│   ├── 02_First_Streamlit_App.ipynb    # Installation, text elements, rerun model
│   ├── 03_streamlit_widgets.ipynb      # Every widget type, keys, forms
│   ├── 04_interactive_ds_controls.ipynb # Dataset filters, ML params, validation
│   ├── 05_layouts_and_containers.ipynb  # Sidebar, columns, tabs, containers, popover, dialog
│   ├── 06_data_science_dashboards.ipynb # KPIs, status feedback, accessibility, dashboard design
│   ├── 07_dataframes_tables_pandas.ipynb # DataFrame display, column_config, filtering, Styler
│   ├── 08_interactive_visualization.ipynb # Native charts, Matplotlib, Plotly, chart selection
│   ├── 09_file_upload_and_processing.ipynb # Upload, validate, clean, analyze, download pipeline
│   ├── 10_interactive_dashboard.ipynb      # Dashboard architecture, filters, KPIs, layout
│   ├── 11_session_state_execution_model.ipynb # Reruns, session state, multi-step workflows
│   ├── 12_caching_performance.ipynb           # Cache basics, cache_data vs cache_resource, TTL
│   ├── 13_application_architecture.ipynb     # Architecture evolution, multipage, components
│   ├── 14_databases_persistence.ipynb        # SQLite, SQL basics, CRUD, connection caching
│   ├── 15_ml_streamlit.ipynb                # Model persistence, preprocessing, classification, regression
│   ├── 17_nlp_applications.ipynb            # NLP workflow, TF-IDF, text classification, batch processing
│   ├── 18_llm_applications.ipynb            # LLM providers, secrets, chat, RAG, streaming
│   ├── deployment_tutorial.ipynb          # Deployment step-by-step tutorial, debugging, best practices
│   └── security_practical_lab.ipynb        # Security exercises, validation, SQL injection, LLM security
├── exercises/               ✏️ Module exercises (one per module)
│   ├── 03_widget_mastery.py
│   ├── 04_dataset_filter_app.py
│   ├── 05_layout_basics.py
│   ├── 06_dashboard_builder.py
│   ├── 07_data_display_challenges.py
│   ├── 08_visualization_workshop.py
│   ├── 09_file_upload_workshop.py
│   ├── 10_dashboard_workshop.py
│   ├── 11_state_management_workshop.py
│   ├── 12_caching_workshop.py
│   ├── 13_architecture_workshop.py
│   ├── 14_database_workshop.py
│   ├── 15_ml_workshop.py
│   ├── 17_nlp_workshop.py
│   ├── 18_llm_workshop.py
│   ├── 01_hello_streamlit.py              # M01: Text, data display, structure, output prediction
│   ├── 09_api_connectors.py               # M09: API fetch, JSON parsing, nested data, design
│   ├── 16_production_ready.py             # M16: Error handling, logging, health checks, debugging
│   ├── deployment_exercises.py            # Deployment preparation, debugging, security exercises
│   └── security_exercises.md              # Security exercises (secrets, validation, SQL, file, LLM)
├── quizzes/                 📝 Weekly quizzes + assessments
│   ├── pre_course_assessment.md           # Placement test (Python, Pandas, ML basics, Git)
│   ├── 01_fundamentals.md                # M01: Streamlit basics, text elements, reruns
│   ├── 02_widgets_input.md               # M02: Widgets, forms, input handling
│   ├── 03_layouts_uiux.md                # M03: Sidebar, columns, tabs, layout design
│   ├── 04_dataframes_visualization.md    # M04: Data display, charts, Plotly, Matplotlib
│   ├── 05_session_state.md               # M05: Reruns, session state, callbacks, state patterns
│   ├── 06_file_upload.md                 # M06: File upload, validation, processing, download
│   ├── 07_session_state.md               # M07 (alt): Session state deep dive
│   ├── 08_caching_performance.md         # M07: cache_data, cache_resource, TTL, invalidation
│   ├── 09_architecture_multipage.md      # M08: Architecture, modules, multipage navigation
│   ├── 10_databases_persistence.md       # M10: SQLite, SQL, CRUD, parameterized queries
│   ├── 11_machine_learning.md            # M12: Model deployment, preprocessing, batch prediction
│   ├── 12_ml_deployment.md               # M12 (alt): ML deployment deep dive
│   ├── 13_nlp_ai.md                      # M13: NLP, text classification, sentiment analysis
│   ├── 14_llm_rag.md                     # M14: LLM providers, RAG, chat, security
│   ├── 15_deployment.md                  # M15: Deployment, Community Cloud, secrets, troubleshooting
│   ├── 16_production_maintenance.md      # M16: Production, monitoring, error handling, logging
│   ├── question_bank.md                  # 📚 Bloom's-tagged question bank for exam construction
│   ├── final_comprehensive_quiz.md       # 📝 Final exam covering all modules (100 pts)
│   └── post_course_assessment.md         # 📊 Post-course self-assessment (mirrors pre-course)
├── assignments/             📋 Graded assignments (4 per semester)
│   ├── A01_personal_dashboard.md         # Beginner: Personal dashboard (M01–M03, 4%)
│   ├── A02_data_explorer.md              # Intermediate: Data explorer with upload (M04–M06, 4%)
│   ├── A03_multipage_application.md      # Advanced: Multipage app with DB (M07–M10, 4%)
│   └── A04_ml_production_app.md          # Production: ML app + deploy (M11–M16, 8%)
├── assessments/             🎯 Course assessments and examinations
│   ├── midcourse_assessment.md       # Midterm: M01-M08, 2 hours, 100 marks
│   ├── lab_assessments.md            # 3 labs: Week 3, 8, 13 (50 min each)
│   ├── practical_exam.md             # Timed coding exam: Week 12, 3 hours, 100 marks
│   ├── final_practical_assessment.md # Final practical: Week 15, 4 hours, 150 marks
│   ├── final_project_assessment.md   # Capstone rubric: 3 weeks, 200 marks
│   └── rubrics/                      # Instructor grading guides and reference materials
├── projects/                🚀 Progressive project specs (P01–P20)
│   ├── README.md                     # Project index with progression map
│   ├── P01_csv_data_viewer.md        # Beginner: CSV upload and display
│   ├── P02_data_explorer.md          # Intermediate: Interactive data dashboard
│   ├── P03_calculator_statistics.md  # Beginner: Calculator and stats tool
│   ├── P04_data_cleaning_dashboard.md # Intermediate: Data cleaning and preprocessing
│   ├── P05_eda_dashboard.md          # Intermediate: Exploratory data analysis
│   ├── P06_ml_model_playground.md    # Advanced: ML model training and prediction
│   ├── P08_capstone_project.md       # Expert: Full capstone project spec
│   ├── P09_visualization_dashboard.md # Intermediate: Multi-chart visualization
│   ├── P10_student_performance.md    # Intermediate: Student analytics dashboard
│   ├── P11_ml_prediction_app.md      # Advanced: ML prediction pipeline
│   ├── P12_model_evaluation_dashboard.md # Advanced: Model comparison dashboard
│   ├── P13_batch_prediction.md       # Advanced: Batch prediction pipeline
│   ├── P14_database_dashboard.md     # Advanced: Database-powered dashboard
│   ├── P15_nlp_application.md        # AI/LLM: Text analysis application
│   ├── P16_llm_chat.md              # AI/LLM: LLM chat interface
│   ├── P17_document_qa.md           # AI/LLM: RAG document Q&A
│   ├── P18_production_dashboard.md  # Expert: Production-quality dashboard
│   ├── P19_ai_powered_app.md        # Expert: AI-powered data science app
│   └── P20_complete_deployed_app.md  # Expert: Complete deployed ML/AI app
├── instructor/              👩‍🏫 Instructor-only teaching materials (not for students)
│   ├── README.md                       # Instructor hub with navigation
│   ├── course_plan.md                  # 16-week semester schedule
│   ├── teaching_roadmap.md             # Module progression & prerequisites
│   ├── 2_hour_lecture_plan.md          # Session-by-session lecture plans
│   ├── lab_activities.md               # Hands-on lab guides with solutions
│   ├── discussion_questions.md         # Discussion prompts by topic
│   ├── assessment_strategy.md          # Grading policies, rubrics, CLO mapping
│   ├── common_student_mistakes.md      # Error catalog with interventions
│   ├── solution_guide.md               # Exercise & assignment solution walkthroughs
│   ├── exercise_guide.md               # Per-exercise grading notes
│   ├── deployment_troubleshooting.md   # Instructor guide for deployment issues
│   └── solutions/                      # Exercise & assignment solutions (do not share)
│       ├── exercises_solutions/        # Runnable .py solutions
│       ├── exercise_notes/             # Markdown grading guides
│       └── assignment_solutions/       # Assignment grading guides
├── apps/                    🖥️ Runnable Streamlit demo apps
│   ├── hello.py                        # Environment verification
│   ├── 01_introduction_demo.py         # Text elements, rerun model, data display
│   ├── 02_first_app_demo.py            # Complete first app with session state
│   ├── 03_widgets_demo.py              # Widgets showcase, session_state demo
│   ├── 04_forms_demo.py                # Forms, validation patterns
│   ├── 05_layouts_demo.py              # Layout elements showcase
│   ├── 06_dashboard_demo.py            # Complete Sales Analytics Dashboard
│   ├── 07_data_display_demo.py         # Data Display & Visualization Dashboard
│   ├── 09_file_upload_demo.py          # File Upload & Processing Dashboard
│   ├── 10_interactive_data_explorer.py # Interactive Data Explorer Dashboard
│   ├── 11_session_state_demo.py       # Session State & Execution Model Demo
│   ├── 12_caching_performance_demo.py # Caching & Performance Demo
│   ├── 13_modular_app/               # Modular multipage app example
│   ├── 14_database_dashboard.py      # SQLite Database Dashboard
│   ├── 15_classification_app.py      # Iris Classification App
│   ├── 15_regression_app.py          # California Housing Regression App
│   ├── 17_sentiment_app.py          # Sentiment Analysis App
│   ├── 18_llm_chat.py              # LLM Chat App (Demo/OpenAI/Local)
│   ├── 18_rag_app.py               # RAG Document Q&A App
│   └── deployable_app/              # Complete app ready for Community Cloud deployment
├── data/                    📊 Shared datasets
├── tests/                   🧪 Test examples using st.testing.AppTest
│
├── requirements.txt         Core dependencies (all students)
├── requirements-optional.txt  Per-module extras (install as needed)
├── requirements-dev.txt     Dev/test tools (TAs, contributors)
├── .streamlit/config.toml   Default Streamlit theme & server config
└── README.md                ← You are here
```

Each content file cross-links to related materials:

```markdown
## Related Materials
- 📓 Notebook: [Session State Deep Dive](../notebooks/11_session_state_execution_model.ipynb)
- ✏️ Exercise: [State Management Workshop](../exercises/11_state_management_workshop.py)
- 📖 Reading: [Session State & Execution](../readings/11_session_state_and_execution.md)
- 🚀 Project: [Data Explorer](../projects/P02_data_explorer.md)
- 🖥️ Demo App: [Run it](../apps/11_session_state_demo.py)
```

---

## 🚀 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/Streamlit-for-Data-Science.git
cd Streamlit-for-Data-Science
```

### 2. Create a Virtual Environment

```bash
# Using venv (recommended)
python -m venv .venv
source .venv/bin/activate        # macOS / Linux
.venv\Scripts\activate           # Windows

# OR using conda
conda create -n streamlit-course python=3.11
conda activate streamlit-course
```

### 3. Install Dependencies

```bash
# Core dependencies (required for all modules)
pip install -r requirements.txt

# Optional module-specific extras (install as needed)
pip install -r requirements-optional.txt    # all extras
# OR install per-module:
pip install altair seaborn                  # Module 04 only
pip install openpyxl                       # Module 06 (Excel upload)
pip install shap                           # Module 12 only
pip install openai langchain chromadb      # Module 13 only
```

### 4. Verify Your Environment

```bash
streamlit run apps/hello.py
```

If you see the welcome page, you're ready for Module 01! 🎉

---

## ▶️ How to Run Streamlit Apps

```bash
# Run any app
streamlit run apps/hello.py

# Run on a specific port
streamlit run apps/hello.py --server.port 8502

# Run in headless mode (for servers / cloud)
streamlit run apps/hello.py --server.headless true
```

**Key facts about Streamlit's execution model:**
- The script reruns top-to-bottom on every user interaction
- Use `st.session_state` to persist data across reruns
- Use `@st.cache_data` / `@st.cache_resource` for expensive computations
- `st.set_page_config()` must be the first Streamlit call in your script

---

## 🗺️ Course Modules

| Week | Module | Topic | Level | Materials |
|---|---|---|---|---|
| 1 | M01 | Streamlit Fundamentals | Beginner | [📖 Reading](readings/01_streamlit_introduction.md) · [📓 Notebook 01](notebooks/01_Streamlit_Introduction.ipynb) · [📓 Notebook 02](notebooks/02_First_Streamlit_App.ipynb) · [🖥️ Demo](apps/01_introduction_demo.py) |
| 1–2 | M02 | Widgets & User Input | Beginner | [📖 Reading 03](readings/03_streamlit_widgets_and_input.md) · [📖 Reading 04](readings/04_widget_keys_and_behavior.md) · [📓 Notebook 03](notebooks/03_streamlit_widgets.ipynb) · [📓 Notebook 04](notebooks/04_interactive_ds_controls.ipynb) · [🖥️ Demo](apps/03_widgets_demo.py) · [🖥️ Demo](apps/04_forms_demo.py) |
| 2–3 | M03 | Layouts, Containers & Pages | Beginner | [📖 Reading 05](readings/05_layouts_and_containers.md) · [📖 Reading 06](readings/06_dashboard_design_ui_ux.md) · [📓 Notebook 05](notebooks/05_layouts_and_containers.ipynb) · [📓 Notebook 06](notebooks/06_data_science_dashboards.ipynb) · [🖥️ Demo](apps/05_layouts_demo.py) · [🖥️ Demo](apps/06_dashboard_demo.py) |
| 4 | M04 | Data Visualization | Intermediate | [📖 Reading 07](readings/07_data_display_dataframes.md) · [📖 Reading 08](readings/08_visualization_matplotlib_plotly.md) · [📓 Notebook 07](notebooks/07_dataframes_tables_pandas.ipynb) · [📓 Notebook 08](notebooks/08_interactive_visualization.ipynb) · [🖥️ Demo](apps/07_data_display_demo.py) |
| 5 | M05 | Session State & App Memory | Intermediate | [📖 Reading 11](readings/11_session_state_and_execution.md) · [📓 Notebook 11](notebooks/11_session_state_execution_model.ipynb) · [✏️ Exercise 11](exercises/11_state_management_workshop.py) · [🖥️ Demo](apps/11_session_state_demo.py) · [📝 Quiz 07](quizzes/07_session_state.md) |
| 5–6 | M06 | Forms, Inputs & File Handling | Intermediate | [📖 Reading 09](readings/09_file_upload_and_processing.md) · [📖 Reading 10](readings/10_interactive_dashboard.md) · [📓 Notebook 09](notebooks/09_file_upload_and_processing.ipynb) · [📓 Notebook 10](notebooks/10_interactive_dashboard.ipynb) · [✏️ Exercise 09](exercises/09_file_upload_workshop.py) · [✏️ Exercise 10](exercises/10_dashboard_workshop.py) · [🖥️ Demo](apps/09_file_upload_demo.py) · [🖥️ Demo](apps/10_interactive_data_explorer.py) |
| 7 | M07 | Caching, Fragments & Performance | Advanced | [📖 Reading 12](readings/12_caching_and_performance.md) · [📓 Notebook 12](notebooks/12_caching_performance.ipynb) · [✏️ Exercise 12](exercises/12_caching_workshop.py) · [🖥️ Demo](apps/12_caching_performance_demo.py) · [📝 Quiz 08](quizzes/08_caching_performance.md) |
| 8 | M08 | Multipage Apps & Navigation | Advanced | [📖 Reading 13](readings/13_application_architecture.md) · [📓 Notebook 13](notebooks/13_application_architecture.ipynb) · [✏️ Exercise 13](exercises/13_architecture_workshop.py) · [🖥️ Demo](apps/13_modular_app/app.py) · [📝 Quiz 09](quizzes/09_architecture_multipage.md) |
| 8–9 | [M09](notebooks/) | Architecture & Design Patterns | Advanced |
| 10 | M10 | Databases & Persistent Storage | Advanced | [📖 Reading 14](readings/14_databases_and_persistence.md) · [📓 Notebook 14](notebooks/14_databases_persistence.ipynb) · [✏️ Exercise 14](exercises/14_database_workshop.py) · [🖥️ Demo](apps/14_database_dashboard.py) · [📝 Quiz 10](quizzes/10_databases_persistence.md) |
| 11 | M11 | APIs, Connectors & External Data | Advanced |
| 12 | M12 | ML Model Deployment | ML | [📖 Reading 15](readings/15_machine_learning_streamlit.md) · [📓 Notebook 15](notebooks/15_ml_streamlit.ipynb) · [✏️ Exercise 15](exercises/15_ml_workshop.py) · [🖥️ Classification](apps/15_classification_app.py) · [🖥️ Regression](apps/15_regression_app.py) · [📝 Quiz 11](quizzes/11_machine_learning.md) · [🚀 Project P06](projects/P06_ml_model_playground.md) |
| 13 | M13 | NLP, AI & LLM Applications | AI/LLM | [📖 Reading 17](readings/17_nlp_ai_applications.md) · [📓 Notebook 17](notebooks/17_nlp_applications.ipynb) · [✏️ Exercise 17](exercises/17_nlp_workshop.py) · [🖥️ Sentiment App](apps/17_sentiment_app.py) · [📝 Quiz 13](quizzes/13_nlp_ai.md) · [🚀 Project P07](projects/P07_rag_document_chat.md) |
| 14 | M14 | Testing, Security & CI/CD | Advanced | [📖 Reading 18](readings/18_llm_rag_applications.md) · [📓 Notebook 18](notebooks/18_llm_applications.ipynb) · [✏️ Exercise 18](exercises/18_llm_workshop.py) · [🖥️ LLM Chat](apps/18_llm_chat.py) · [🖥️ RAG Q&A](apps/18_rag_app.py) · [📝 Quiz 14](quizzes/14_llm_rag.md) · [🚀 Project P07](projects/P07_rag_document_chat.md) |
| 15 | M15 | Streamlit Community Cloud & Deployment | Deployment | [📖 Deployment Guide](readings/deployment_guide.md) · [📓 Deployment Tutorial](notebooks/deployment_tutorial.ipynb) · [✏️ Deployment Exercises](exercises/deployment_exercises.py) · [🖥️ Deployable App](apps/deployable_app/) · [📝 Quiz 15](quizzes/15_deployment.md) · [📋 Checklist](docs/deployment_checklist.md) |
| 16 | [M16](notebooks/) | Production, Maintenance & Monitoring | Production |

> **Note:** Content for notebooks, exercises, quizzes, and projects is being built out progressively. See [docs/course_blueprint.md](docs/course_blueprint.md) for the full planned structure.

### 🚀 Project Ladder

| # | Project | Level | Key Skills |
|---|---|---|---|
| P01 | [CSV Data Viewer](projects/P01_csv_data_viewer.md) | Beginner | File upload, DataFrame display, statistics |
| P02 | [Data Explorer](projects/P02_data_explorer.md) | Intermediate | Filters, KPIs, charts, session state |
| P03 | [Calculator & Stats](projects/P03_calculator_statistics.md) | Beginner | Widgets, conditional logic, basic stats |
| P04 | [Data Cleaning](projects/P04_data_cleaning_dashboard.md) | Intermediate | Data transformation, before/after, export |
| P05 | [EDA Dashboard](projects/P05_eda_dashboard.md) | Intermediate | Multi-tab exploration, distributions, correlations |
| P06 | [ML Playground](projects/P06_ml_model_playground.md) | Advanced | Model training, evaluation, prediction |
| P09 | [Visualization](projects/P09_visualization_dashboard.md) | Intermediate | Plotly, Matplotlib, chart selection |
| P10 | [Student Analytics](projects/P10_student_performance.md) | Intermediate | Domain-specific analytics, complex filtering |
| P11 | [ML Prediction](projects/P11_ml_prediction_app.md) | Advanced | Model deployment, preprocessing, batch prediction |
| P12 | [Model Evaluation](projects/P12_model_evaluation_dashboard.md) | Advanced | Model comparison, ROC, confusion matrix |
| P13 | [Batch Prediction](projects/P13_batch_prediction.md) | Advanced | Batch processing, validation, reporting |
| P14 | [Database Dashboard](projects/P14_database_dashboard.md) | Advanced | SQLite, CRUD, multipage, caching |
| P15 | [NLP Application](projects/P15_nlp_application.md) | AI/LLM | Text analysis, sentiment, classification |
| P16 | [LLM Chat](projects/P16_llm_chat.md) | AI/LLM | Chat UI, provider abstraction, secrets |
| P17 | [Document Q&A](projects/P17_document_qa.md) | AI/LLM | RAG, retrieval, chunking, LLM integration |
| P18 | [Production Dashboard](projects/P18_production_dashboard.md) | Expert | Testing, security, deployment, monitoring |
| P19 | [AI-Powered App](projects/P19_ai_powered_app.md) | Expert | ML + LLM integration, full-stack AI |
| P20 | [Complete Deployed App](projects/P20_complete_deployed_app.md) | Expert | All course skills combined |
| P08 | [**Capstone Project**](projects/P08_capstone_project.md) | Expert | Full development lifecycle |

---

## 🧪 Testing

This course uses Streamlit's native `st.testing.AppTest` framework:

```bash
# Run all tests
pytest tests/ -v

# Run a specific test
pytest tests/test_hello.py -v

# Run notebook validation
nbmake notebooks/*.ipynb --timeout=300
```

---

## 🚢 Deployment

### Streamlit Community Cloud (Recommended for Students)

1. Push your app to a GitHub repository
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Sign in with GitHub → "New app" → select repo, branch, and main file
4. Add secrets via **Advanced settings**
5. Click **Deploy!**

**Deployment checklist:**
- [ ] `requirements.txt` at repo root
- [ ] Entry point file (e.g., `app.py`) runs without errors
- [ ] No hardcoded secrets in source — use `.streamlit/secrets.toml`
- [ ] App handles errors gracefully
- [ ] Tested locally before pushing

### Alternatives

| Platform | Best For | Free Tier |
|---|---|---|
| [Streamlit Community Cloud](https://streamlit.io/cloud) | Quick sharing, course projects | ✅ Yes |
| [HuggingFace Spaces](https://huggingface.co/spaces) | ML demos, Gradio/Streamlit | ✅ Yes |
| [Render](https://render.com) | Production-grade hosting | ✅ Yes (limited) |
| Docker + VPS | Full control, production | — |

> See `docs/deployment_checklist.md` for the full deployment guide.

---

## 🤝 Contributing

This course welcomes contributions from instructors, TAs, and students.

### How to Contribute

1. **Fork** the repository
2. **Create** a feature branch: `git checkout -b feature/your-improvement`
3. **Commit** with a clear message: `git commit -m "Add: exercise for Module 05"`
4. **Push** and open a **Pull Request**

### Contribution Guidelines

- **Exercises:** Follow the naming convention `exercise_NN_topic.py`
- **Notebooks:** Follow the naming convention `NN_topic_name.ipynb`
- **Readings:** Follow the naming convention `rNN_topic.md`
- **Tests:** Add tests for any new Streamlit app in `tests/`
- **Secrets:** Never commit API keys, passwords, or tokens
- **Linting:** Run `ruff check .` before committing

### Reporting Issues

Found a bug or broken exercise? [Open an issue](../../issues) with:
- Module number and file affected
- Expected vs. actual behavior
- Python and Streamlit versions (`pip show streamlit`)

---

## 📋 Course Assessment

| Component | Weight | Count | Assessment Type |
|---|---|---|---|
| Weekly Quizzes | 10% | 16 | MCQ, short answer, code questions |
| Lab Assessments | 10% | 3 | In-class supervised practicals |
| Mid-Course Assessment | 10% | 1 | 2-hour exam (conceptual + coding) |
| Practical Exam | 10% | 1 | 3-hour timed coding exam |
| Assignments | 20% | 4 | Take-home project submissions (A01–A04) |
| Final Practical Assessment | 15% | 1 | 4-hour comprehensive practical |
| Capstone Project | 15% | 1 | 3-week project + presentation |
| Participation | 5% | — | Attendance, discussion, peer review |
| Pre/Post Assessment | 5% | 2 | Placement + growth measurement |
| **Total** | **100%** | | |

### Bloom's Taxonomy Distribution

| Level | Label | Percentage |
|-------|-------|------------|
| L1 | Remember | 10% |
| L2 | Understand | 15% |
| L3 | Apply | 35% |
| L4 | Analyze | 20% |
| L5 | Evaluate | 15% |
| L6 | Create | 5% |

See [docs/learning_outcomes.md](docs/learning_outcomes.md) for full CLO-to-assessment mapping.
See [docs/course_blueprint.md](docs/course_blueprint.md) §8 for full rubrics.

---

## 📄 License

This project is licensed under the MIT License — see [LICENSE](LICENSE) for details.

**Copyright (c) 2026 Dr. Muhammad Nadeem Majeed**

---

## 🙏 Acknowledgements

- [Streamlit](https://streamlit.io) — the framework that makes this course possible
- The Streamlit community for excellent documentation and examples
- Students and instructors who contribute improvements

---

## 📬 Contact

For course-related questions, open a [GitHub Discussion](../../discussions) or contact the course instructor.

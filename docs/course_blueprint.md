# Streamlit for Data Science — Learn, Build, Deploy
## Course Blueprint

> **Version:** 1.0 · **Date:** September 2, 2026 · **Streamlit target:** ≥ 1.60  
> **Status:** Internal planning document — not student-facing.

---

## Table of Contents

1. [Course Philosophy](#1-course-philosophy)
2. [Target Audience](#2-target-audience)
3. [Prerequisites](#3-prerequisites)
4. [Learning Progression](#4-learning-progression)
5. [Proposed Modules](#5-proposed-modules)
6. [Proposed Notebooks](#6-proposed-notebooks)
7. [Project Progression](#7-project-progression)
8. [Assessment Strategy](#8-assessment-strategy)
9. [Repository Architecture](#9-repository-architecture)
10. [Dependency Strategy](#10-dependency-strategy)
11. [Deployment Strategy](#11-deployment-strategy)
12. [Security Strategy](#12-security-strategy)
13. [QA Strategy](#13-qa-strategy)
14. [Cross-Linking & Navigation Strategy](#14-cross-linking--navigation-strategy)
15. [Topics Requiring Documentation Verification](#15-topics-requiring-documentation-verification)
16. [Appendices](#appendices)

---

## 1. Course Philosophy

### 1.1 Core Belief

Data science education must bridge the gap between *analysis* and *communication*. A model that nobody can interact with is a model that nobody uses. Streamlit removes the engineering barrier so data scientists can ship interactive applications with pure Python — no front-end framework required.

### 1.2 Pedagogical Framework

Every topic follows a **10-stage learning cycle**:

```
Concept → Intuition → Visual Explanation → Example → Code → Run
→ Experiment → Exercise → Assessment → Real-world Application
```

| Stage | What Happens | Where It Lives |
|---|---|---|
| **Concept** | Define the idea in one sentence | Reading / notebook intro |
| **Intuition** | Analogy or everyday metaphor | Reading with diagrams |
| **Visual Explanation** | Architecture diagram, flowchart, or annotated screenshot | `docs/figures/` |
| **Example** | Minimal working demo | Notebook code cell |
| **Code** | Student builds it step-by-step | Notebook walkthrough |
| **Run** | Execute and observe output | `streamlit run` or notebook cell |
| **Experiment** | Vary parameters, break things on purpose | Guided "try this" prompts |
| **Exercise** | Structured practice problem | `exercises/` directory |
| **Assessment** | Quiz or self-check | `quizzes/` or inline |
| **Real-world Application** | Industry scenario or mini-project | `projects/` or `assignments/` |

### 1.3 Design Principles

- **Progressive complexity:** Each module builds on the last; no topic is introduced without its dependency.
- **Reproducibility first:** Every notebook, exercise, and project runs from a clean `pip install -r requirements.txt`.
- **Authentic data:** Use real-world datasets (UCI, Kaggle, government portals) rather than synthetic toy data.
- **Production mindset from Day 1:** Even beginner exercises discuss folder structure, secrets, and version control.
- **Hands-on ratio:** ≥ 70% of class time is writing code; ≤ 30% is lecture/reading.
- **Bilingual support:** All materials are in English; inline Arabic/Urdu glossary terms are provided for key Streamlit concepts where helpful for the intended student population.

---

## 2. Target Audience

### 2.1 Primary

| Attribute | Detail |
|---|---|
| **Degree programs** | BS Data Science, BS Artificial Intelligence, BS Computer Science |
| **Year** | Junior / Senior (3rd–4th year) or final-semester elective |
| **Python proficiency** | Comfortable with functions, classes, file I/O, exceptions |
| **Data libraries** | Working knowledge of NumPy, Pandas, Matplotlib/Plotly |
| **ML familiarity** | Has completed at least one ML course (scikit-learn basics) |
| **Jupyter experience** | Has written and run Jupyter notebooks for assignments |

### 2.2 Secondary Audiences

- Graduate students seeking rapid prototyping skills for research dashboards.
- Industry professionals transitioning from Jupyter-only workflows to shareable apps.
- Hackathon teams needing a fast UI layer for ML/AI demos.

### 2.3 Estimated Class Size

- Designed for sections of **20–40 students** with a single instructor and one teaching assistant.
- All exercises and projects are graded automatically (where possible) to scale.

---

## 3. Prerequisites

### 3.1 Hard Prerequisites (Must Have)

| Topic | Minimum Level | Assessment Gate |
|---|---|---|
| Python 3.10+ | Functions, classes, list comprehensions, file I/O, virtual environments | Placement quiz or instructor sign-off |
| NumPy | Array creation, slicing, broadcasting, basic linear algebra | Pre-course lab |
| Pandas | DataFrame CRUD, groupby, merge, apply, read_csv/read_excel | Pre-course lab |
| Matplotlib / Plotly | Basic plots: line, bar, scatter, histogram | Pre-course lab |
| Machine Learning (intro) | Train/test split, fit/predict, basic classification metrics | Pre-course lab |
| Git fundamentals | clone, add, commit, push, pull, branch, merge | Pre-course lab |

### 3.2 Soft Prerequisites (Recommended)

| Topic | Why Helpful |
|---|---|
| SQL basics | Used in Module 10 (Databases) |
| REST API concepts | Used in Module 11 (APIs & Integrations) |
| Docker basics | Used in Module 14 (Advanced Deployment) |
| Cloud platforms (AWS/GCP) | Used in Module 14 (Production Deployment) |

### 3.3 Pre-Course Preparation Checklist

Students must complete before Module 1:

1. Install Python 3.10+ via Miniconda or pyenv.
2. Create a GitHub account and configure SSH keys.
3. Clone this repository and run `pip install -r requirements.txt`.
4. Verify Streamlit runs: `streamlit run apps/hello.py`.
5. Complete the **Pre-Course Assessment** (`assessments/pre_course_assessment.py`).

---

## 4. Learning Progression

The course spans **16 weeks** (one semester) with a 2–2–1 weekly rhythm:

| Day | Focus | Hours |
|---|---|---|
| Day 1 (Tue) | Concept lecture + guided notebook walkthrough | 1.5 h |
| Day 2 (Thu) | Hands-on coding lab + exercise work session | 1.5 h |
| Day 3 (Sat) | Optional office hours / project lab | 1.0 h |

### 4.1 Progression Map

```
BEGINNER (Weeks 1–3)
  Module 01  ▸ Streamlit Fundamentals
  Module 02  ▸ Widgets & User Input
  Module 03  ▸ Layouts, Containers & Pages
  ────────────────────────────────────
INTERMEDIATE (Weeks 4–6)
  Module 04  ▸ Data Visualization with Streamlit
  Module 05  ▸ Session State & App Memory
  Module 06  ▸ Forms, Inputs & File Handling
  ────────────────────────────────────
ADVANCED (Weeks 7–9)
  Module 07  ▸ Caching, Fragments & Performance
  Module 08  ▸ Multipage Apps & Navigation
  Module 09  ▸ Architecture & Design Patterns
  ────────────────────────────────────
DATA LAYER (Weeks 10–11)
  Module 10  ▸ Databases & Persistent Storage
  Module 11  ▸ APIs, Connectors & External Data
  ────────────────────────────────────
MACHINE LEARNING (Weeks 12–13)
  Module 12  ▸ ML Model Deployment with Streamlit
  Module 13  ▸ NLP, AI & LLM Applications
  ────────────────────────────────────
DEPLOYMENT & PRODUCTION (Weeks 14–16)
  Module 14  ▸ Testing, Security & CI/CD
  Module 15  ▸ Streamlit Community Cloud & Deployment
  Module 16  ▸ Production, Maintenance & Monitoring
  ────────────────────────────────────
CAPSTONE (Weeks 14–16, parallel)
  Project    ▸ Capstone Project Development & Presentation
```

### 4.2 Bloom's Taxonomy Mapping

| Level | Where Addressed |
|---|---|
| Remember | Modules 1–3 (vocabulary, API names) |
| Understand | Modules 4–6 (explain when to use each widget/caching strategy) |
| Apply | Modules 7–9 (build multipage apps, apply design patterns) |
| Analyze | Modules 10–13 (choose database, compare ML model serving approaches) |
| Evaluate | Modules 14–16 (review security posture, compare deployment options) |
| Create | Capstone project (design, build, deploy, present a complete application) |

---

## 5. Proposed Modules

### Module 01 — Streamlit Fundamentals (Week 1)

**Objective:** Students can create, run, and customize a basic Streamlit app.

| Topic | Detail |
|---|---|
| What is Streamlit? | Overview, philosophy, use cases vs. Dash/Flask/Gradio |
| Installation & setup | `pip install streamlit`, virtual environments, `.streamlit/` config |
| Hello World | `st.title`, `st.write`, `st.markdown`, `st.latex` |
| Running apps | `streamlit run`, port configuration, auto-reload |
| Markdown in Streamlit | Headings, bold, italic, links, code blocks, LaTeX, `st.code` |
| `.streamlit/config.toml` | Theme, server, browser, developer settings |
| Streamlit project structure | Best practices for organizing files |
| First exercise | Build a personal profile page |

**Key APIs:** `st.title`, `st.header`, `st.subheader`, `st.write`, `st.markdown`, `st.code`, `st.latex`, `st.divider`, `st.image`  
**Verification note:** Check latest `config.toml` options against docs; the allowed hosts, CORS, and XSRF settings changed in 1.60.

---

### Module 02 — Widgets & User Input (Week 1–2)

**Objective:** Students can build interactive apps using Streamlit's widget library.

| Topic | Detail |
|---|---|
| Widget fundamentals | Return values, keys, callbacks, disabled state |
| Text input | `st.text_input`, `st.text_area`, `st.number_input` |
| Selection | `st.selectbox`, `st.multiselect`, `st.radio`, `st.checkbox`, `st.toggle` |
| Sliders & dates | `st.slider`, `st.select_slider`, `st.date_input`, `st.time_input`, `st.datetime_input` |
| Color & file | `st.color_picker`, `st.file_uploader` |
| Buttons & downloads | `st.button`, `st.form_submit_button`, `st.download_button` |
| New in 1.62 | `st.text_input` client-side validation, `validate` parameter, email/URL/phone/search types |
| `wrap` parameter | Horizontal scrolling for columns, buttons, checkboxes, multiselect |
| **New in 1.61** | `st.metric` icon parameter, `st.time_input` revamp |

**Key APIs:** All widget functions, `disabled` parameter (server-side enforced since 1.60), `placeholder`, `help`  
**Verification note:** The `validate` and `type` parameters on `st.text_input` are new in 1.62.0 — verify defaults and behavior. The `disabled` parameter is now enforced server-side (1.60). The `wrap` parameter on `st.columns` and widgets is new in 1.62.0.

---

### Module 03 — Layouts, Containers & Pages (Week 2–3)

**Objective:** Students can structure app layouts with columns, tabs, sidebars, and containers.

| Topic | Detail |
|---|---|
| Sidebar | `st.sidebar`, sidebar widgets, sidebar vs. main area |
| Columns | `st.columns` with gap presets and new pixel-gap integer support (1.60) |
| Containers | `st.container`, `st.expander`, `st.popover`, `st.dialog` (via `@st.dialog`) |
| Tabs | `st.tabs` with new `height` parameter (1.60) |
| Horizontal layouts | `wrap=False` for scrollable rows (1.62) |
| Status & progress | `st.status`, `st.progress`, `st.spinner`, `st.toast`, `st.balloons`, `st.snow` |
| Theming | `config.toml` themes, dark mode, custom fonts, font-weight increments of 50 (1.62) |
| First multi-file app | Page directory structure introduction |

**Verification note:** `st.tabs` height parameter and `st.columns` pixel gap are new in 1.60. `wrap=False` for columns, buttons, checkboxes, toggles, and multiselect is new in 1.62. Verify `@st.dialog` decorator availability and behavior.

---

### Module 04 — Data Visualization with Streamlit (Week 4)

**Objective:** Students can create and customize charts using Streamlit's native and third-party integrations.

| Topic | Detail |
|---|---|
| Native charts | `st.line_chart`, `st.bar_chart`, `st.area_chart`, `st.scatter_chart`, `st.map` |
| Matplotlib integration | `st.pyplot` (note: must pass explicit figure since 1.62; `savefig` kwargs deprecated) |
| Plotly integration | `st.plotly_chart` with `use_container_width` |
| Altair / Vega-Lite | `st.altair_chart`, `st.vega_lite_chart` (JSON reconstruction fix in 1.62) |
| Chart theming | New categorical, sequential, diverging color config per theme mode (1.62) |
| PyDeck | `st.pydeck_chart` for geospatial |
| Graphviz | `st.graphviz_chart` (sanitized link attributes in 1.60) |
| Seaborn / other | Passing non-native charts via `st.pyplot` or `st.image` |
| Chart configuration | `config`, download buttons, toolbar customization |
| Choosing the right chart | Decision matrix: when to use which chart type |

**Verification note:** `st.pyplot` now requires an explicit figure (breaking change 1.62). The `format="svg"` parameter for `st.pyplot` is now supported (1.62). Vega-Lite action buttons are now in the native toolbar (1.60). Verify the chart categorical/sequential/diverging color config syntax.

---

### Module 05 — Session State & App Memory (Week 5)

**Objective:** Students can manage persistent state across reruns using session state and callbacks.

| Topic | Detail |
|---|---|
| Streamlit's execution model | Top-to-bottom rerun on every interaction |
| `st.session_state` | Dict-like API, per-session isolation |
| Initializing state | `.setdefault()`, conditional init patterns |
| Callbacks | `on_click`, `on_change` for widgets, callback chains |
| State patterns | Counter, multi-page form, undo/redo, user preferences |
| Common pitfalls | State loss, unintended rerun loops, stale values |
| `st.fragment` (partial rerun) | New in 1.33+, background auto-rerun with `run_every` |

**Verification note:** `@st.fragment(run_every=...)` had duplicate-rerun bugs fixed in 1.60 and 1.62. Verify fragment compatibility with `AppTest` (known issue #9242). Fragment nesting bugs fixed in 1.61.

---

### Module 06 — Forms, Inputs & File Handling (Week 5–6)

**Objective:** Students can build form-based input flows and handle file uploads/downloads.

| Topic | Detail |
|---|---|
| `st.form` | Form containers, `st.form_submit_button` |
| Form validation | Client-side validation with `validate` (1.62), custom validation patterns |
| File uploaders | `st.file_uploader`, accepted types, size limits |
| CSV/Excel processing | Reading uploaded files into Pandas |
| Image/audio/video | `st.image`, `st.audio`, `st.video` |
| Download buttons | `st.download_button` (now infers `file_name` from file objects, 1.61) |
| Temporary files | Working with `tempfile`, session-scoped storage |
| File organization | Naming conventions, upload directory structure |

**Verification note:** `st.download_button` auto-infers `file_name` and `mime` from file objects (1.61). Passing local file paths as strings to `st.html`/`st.iframe` is deprecated; use `pathlib.Path` (1.60).

---

### Module 07 — Caching, Fragments & Performance (Week 7)

**Objective:** Students can optimize app performance using caching, fragments, and lazy loading.

| Topic | Detail |
|---|---|
| Why caching matters | Streamlit's rerun model and performance implications |
| `st.cache_data` | Hash-based caching, TTL, `max_entries`, computed hash behavior |
| `st.cache_resource` | Singleton pattern for DB connections, ML models, API clients |
| Background refresh | New `refresh_mode="background"` (1.61) — serve stale while refreshing |
| Cache invalidation | When caches break, manual `.clear()`, `hash_funcs` |
| `st.fragment` | Partial rerun scope, `run_every` periodic rerun, fragment nesting |
| Lazy loading | `st.dataframe` lazy parameter for large datasets (1.61), Polars LazyFrame |
| Performance profiling | `st.help`, line profiling, identifying bottlenecks |
| Cache hash seed | `runner.cacheHashSeed` config for cache key customization (1.62 fix) |

**Verification note:** `refresh_mode="background"` is new in 1.61 — verify exact behavior and edge cases. The `runner.cacheHashSeed` bug fix is in 1.62. Polars LazyFrame support in lazy loading is new in 1.61.

---

### Module 08 — Multipage Apps & Navigation (Week 8)

**Objective:** Students can build and navigate multipage Streamlit applications.

| Topic | Detail |
|---|---|
| Page directory convention | `pages/` folder, numbering, emoji prefixes |
| `st.navigation` | Modern API for programmatic page control |
| `st.Page` | Now a proper class (not alias) since 1.61 |
| `st.Page` class | `isinstance(page, st.Page)` works correctly (1.61) |
| Sidebar navigation | Dynamic page selection, conditional pages |
| URL query params | `st.query_params` for deep linking, URL state |
| Page config | `st.set_page_config` (must be first Streamlit call) |
| Reusable pages | Passing pages between functions, composing navigation |
| Multipage testing | `AppTest` multipage path handling (fixed in 1.61) |

**Verification note:** `st.Page` is now a proper class (1.61), not an alias. `isinstance` checks work. `StreamlitPage` is a backward-compatible alias. Verify `st.navigation` API and any changes since its introduction.

---

### Module 09 — Architecture & Design Patterns (Week 8–9)

**Objective:** Students can design well-structured Streamlit applications using proven patterns.

| Topic | Detail |
|---|---|
| Project structure | `src/`, `pages/`, `utils/`, `components/`, `assets/`, `tests/` |
| Separation of concerns | UI vs. logic vs. data layer |
| Component pattern | Reusable components via `st.fragment` or separate modules |
| Configuration management | `config.toml`, environment variables, `st.secrets` |
| State management patterns | Global vs. session vs. page-level state |
| Error handling | `try/except`, `st.error`, `st.warning`, graceful degradation |
| Logging | Python `logging` module in Streamlit context |
| Code organization | When to extract into separate `.py` files |
| Design review checklist | Architecture decision record template |

---

### Module 10 — Databases & Persistent Storage (Week 10)

**Objective:** Students can connect Streamlit apps to SQL and NoSQL databases.

| Topic | Detail |
|---|---|
| `st.connection` | Unified connection API, built-in types |
| SQL connections | `st.connections.SQLConnection`, SQLAlchemy integration |
| `st.connection("sql")` | Configuration via `secrets.toml`, query execution |
| SQLite | Local database for development and prototyping |
| PostgreSQL | Production database, connection pooling |
| Data reader/writer | `conn.read_sql()`, `conn.query()` |
| Secrets management | `.streamlit/secrets.toml`, env vars, production secrets |
| ORM basics | SQLAlchemy models for Streamlit apps |
| NoSQL introduction | MongoDB, Firestore basics (overview only) |

**Verification note:** Verify `st.connections.SQLConnection` API and retry configuration. The `tenacity` dependency for retries was removed in 1.62. Verify current retry/fallback behavior.

---

### Module 11 — APIs, Connectors & External Data (Week 11)

**Objective:** Students can integrate external APIs and data sources into Streamlit apps.

| Topic | Detail |
|---|---|
| HTTP in Python | `requests`, `httpx`, async patterns |
| REST API consumption | GET/POST, authentication, rate limiting |
| API keys in Streamlit | `st.secrets`, environment variables, never in source |
| JSON processing | Parsing, nested data, error handling |
| External data connectors | `st.connection` for HTTP, custom connectors |
| Data pipelines | Fetch → parse → cache → display pattern |
| Streamlit components | `streamlit.components.v1` for HTML/JS embedding |
| Building custom components | `st.components.v1.declare_component` |

---

### Module 12 — ML Model Deployment with Streamlit (Week 12)

**Objective:** Students can build interactive ML dashboards with model inference in Streamlit.

| Topic | Detail |
|---|---|
| Model serialization | `joblib`, `pickle`, ONNX, `pickle` security concerns |
| Loading models | `@st.cache_resource` for model loading |
| Interactive prediction | Widget-driven input → model inference → output display |
| Feature engineering | Input preprocessing in the app |
| Model comparison | Side-by-side dashboard for multiple models |
| Confidence & explanations | SHAP, LIME, feature importance in the app |
| Batch prediction | File upload → bulk inference → download results |
| Model versioning | Organizing multiple model versions |
| sklearn integration | Complete classification/regression dashboard |
| Real-time vs. batch | When to use each approach |

---

### Module 13 — NLP, AI & LLM Applications (Week 13)

**Objective:** Students can build NLP and AI/LLM-powered Streamlit applications.

| Topic | Detail |
|---|---|
| NLP basics in Streamlit | Text classification, sentiment analysis dashboard |
| Text preprocessing | Tokenization, vectorization, display in Streamlit |
| Chat interfaces | `st.chat_message`, `st.chat_input` — native chat UI |
| LLM integration basics | OpenAI API, Anthropic, open-source via Ollama |
| Conversation management | Session-state-based chat history |
| Streaming responses | Token-by-token display |
| RAG (Retrieval-Augmented Generation) | Document upload → chunking → embedding → retrieval → generation |
| Vector stores | ChromaDB, FAISS, Pinecone basics |
| LangChain + Streamlit | Chain orchestration, tool use |
| Prompt engineering UIs | Building prompt template interfaces |
| Guardrails | Output filtering, token limits, cost control |

---

### Module 14 — Testing, Security & CI/CD (Week 14)

**Objective:** Students can test, secure, and set up CI/CD for Streamlit apps.

| Topic | Detail |
|---|---|
| `st.testing.AppTest` | Streamlit's native testing framework |
| Unit tests with pytest | Structuring test files, fixtures, mocking |
| AppTest API | `AppTest.from_file()`, simulate widget input, assert output |
| AppTest limitations | Known issues with `st.fragment` compatibility (#9242) |
| Security fundamentals | OWASP Top 10 overview for web apps |
| Secrets management | `.streamlit/secrets.toml`, production secrets vaults |
| Input validation | `validate` parameter (1.62), custom sanitization |
| Server security | `server.allowedHosts` (1.61), `server.enableCORS`, `server.enableXsrfProtection` |
| Widget state security | `server.maxWidgetStateSize` (1.60), disabled enforcement (1.60) |
| URL safety | Sanitized dangerous URLs in `st.link_button`, `st.image`, Graphviz (1.60) |
| Data export control | `client.disableDataExport` config (1.60) |
| Authentication | `streamlit-authenticator`, role-based access patterns |
| CI/CD with GitHub Actions | Automated testing, linting, deployment pipelines |
| Linting | Ruff, MyPy, pre-commit hooks |

**Verification note:** Security hardening in 1.60 is extensive — verify all new config options: `server.allowedHosts`, `server.maxWidgetStateSize`, `client.disableDataExport`. The host message origin spoofing protection (CWE-346) and query string caps (CWE-770) are critical security features to teach accurately.

---

### Module 15 — Streamlit Community Cloud & Deployment (Week 15)

**Objective:** Students can deploy and share Streamlit apps on Streamlit Community Cloud.

| Topic | Detail |
|---|---|
| Community Cloud overview | Free hosting, GitHub integration, auto-deploy on push |
| Prerequisites | GitHub repo, `requirements.txt`, entry point |
| Deployment workflow | Connect repo → select branch/file → deploy |
| Secrets in Cloud | Adding secrets via the Cloud dashboard |
| App sleep/wake | 7-day inactivity sleep, keep-awake strategies |
| Custom domains | (Overview) |
| Alternatives | HuggingFace Spaces, Render, Railway, Docker on VPS |
| Deployment checklist | File organization, dependency pinning, secrets, entry point |
| Multi-app repos | Deploying multiple apps from one repository |
| Troubleshooting | Common deployment errors and fixes |

---

### Module 16 — Production, Maintenance & Monitoring (Week 16)

**Objective:** Students can maintain, monitor, and iterate on production Streamlit applications.

| Topic | Detail |
|---|---|
| Monitoring basics | Logging, error tracking, usage analytics |
| Performance monitoring | Cache hit rates, load times, memory usage |
| Version updates | Keeping Streamlit current, migration guides, breaking changes |
| User feedback | In-app feedback mechanisms |
| Documentation | README, inline docs, user guides |
| Maintenance tasks | Dependency updates, security patches, data refresh |
| Scaling considerations | When Streamlit is (and isn't) the right tool |
| Streamlit in production | Limitations, alternatives for high-traffic apps |
| MLOps integration | MLflow, DVC, model registry integration |
| Course review & wrap-up | Comprehensive review, Q&A, next steps |

---

## 6. Proposed Notebooks

### 6.1 Notebook Inventory

| # | Title | Module | Est. Time | Level | Location |
|---|---|---|---|---|---|
| N01 | Your First Streamlit App: From Print to Interactive | M01 | 1.5 h | Beginner | `notebooks/01_first_streamlit_app.ipynb` |
| N02 | The Widget Zoo: Mastering Streamlit's Input Arsenal | M02 | 2.0 h | Beginner | `notebooks/02_widgets_and_input.ipynb` |
| N03 | Layout Mastery: Columns, Tabs, Sidebars & Containers | M03 | 1.5 h | Beginner | `notebooks/03_layouts_and_containers.ipynb` |
| N04 | Data Visualization in Streamlit: Charts That Tell Stories | M04 | 2.0 h | Intermediate | `notebooks/04_data_visualization.ipynb` |
| N05 | Session State Deep Dive: Giving Your App a Memory | M05 | 2.0 h | Intermediate | `notebooks/05_session_state.ipynb` |
| N06 | Forms, Files & Data Pipelines | M06 | 1.5 h | Intermediate | `notebooks/06_forms_file_handling.ipynb` |
| N07 | Performance Engineering: Caching, Fragments & Lazy Loading | M07 | 2.0 h | Advanced | `notebooks/07_caching_and_performance.ipynb` |
| N08 | Building Multipage Applications with Navigation | M08 | 1.5 h | Advanced | `notebooks/08_multipage_apps.ipynb` |
| N09 | Architecting Streamlit Apps: Patterns & Best Practices | M09 | 2.0 h | Advanced | `notebooks/09_architecture_patterns.ipynb` |
| N10 | Database Connectivity: SQLite, PostgreSQL & SQLAlchemy | M10 | 2.0 h | Advanced | `notebooks/10_databases.ipynb` |
| N11 | API Integration & External Data Sources | M11 | 1.5 h | Advanced | `notebooks/11_api_integration.ipynb` |
| N12 | Machine Learning Dashboards: From Model to Interactive App | M12 | 2.5 h | ML | `notebooks/12_ml_dashboard.ipynb` |
| N13 | Building AI-Powered Apps: LLMs, Chat & RAG | M13 | 2.5 h | AI/LLM | `notebooks/13_ai_llm_apps.ipynb` |
| N14 | Testing & Securing Your Streamlit Applications | M14 | 2.0 h | Advanced | `notebooks/14_testing_security.ipynb` |
| N15 | Deploy to the World: Streamlit Community Cloud | M15 | 1.5 h | Deployment | `notebooks/15_deployment_guide.ipynb` |
| N16 | Production Readiness: Monitoring, Maintenance & Beyond | M16 | 1.5 h | Production | `notebooks/16_production_readiness.ipynb` |

**Total estimated contact hours:** ~28.5 h (notebooks only, excluding exercises/projects)

### 6.2 Notebook Design Standards

Each notebook follows this structure:

```
# Notebook Title
## Learning Objectives (bullet list, 3–5 objectives)
## Prerequisites (links to prior notebooks)
## 📚 Concept (1–2 paragraphs)
## 🧠 Intuition (analogy or metaphor)
## 🖼 Visual Explanation (diagram or annotated screenshot — links to docs/figures/)
## 💡 Example (minimal working example with explanation)
## 🔨 Build It (step-by-step code walkthrough with student prompts)
## 🧪 Experiment (2–3 "try this" challenges)
## 📝 Key Takeaways (summary)
## 🔗 Further Reading (links to docs, blog posts)
## ⏭ What's Next (bridge to next notebook)
```

### 6.3 Notebook Format

- **File format:** Jupyter Notebook (`.ipynb`) — students are already familiar.
- **Run capability:** Each notebook can be opened directly in JupyterLab and the Streamlit apps within it can be launched from code cells using `subprocess` or a custom helper.
- **Companion app:** Each notebook has a corresponding runnable Streamlit app in `apps/` that demonstrates the same concepts as a standalone application.
- **Cross-links:** Notebooks contain explicit links to related exercises, readings, and project milestones.

---

## 7. Project Progression

### 7.1 Project Ladder

Projects increase in scope and complexity across the semester. Each builds on skills from the previous.

| # | Title | Weeks | Level | Key Skills | Deliverable |
|---|---|---|---|---|---|
| P01 | Personal Dashboard | 2–3 | Beginner | `st.write`, widgets, layout, theming | Single-page personal profile app |
| P02 | Data Explorer | 4–5 | Intermediate | File upload, Pandas, charts, session state | Interactive CSV/Excel data browser |
| P03 | Form-Based Survey Tool | 5–6 | Intermediate | Forms, validation, file handling, download | Survey app with results export |
| P04 | Real-Time Dashboard | 7–8 | Advanced | Caching, fragments, `run_every`, multipage | Live-updating metrics dashboard |
| P05 | CRUD Database App | 10–11 | Advanced | SQL, forms, authentication, session state | Contact manager or inventory system |
| P06 | ML Model Playground | 12–13 | ML | Model loading, inference, SHAP, comparison | Interactive ML model explorer |
| P07 | RAG Document Chat | 13 | AI/LLM | Chat UI, embeddings, vector store, LLM API | Document Q&A application |
| P08 | Capstone Project | 14–16 | Production | All skills + testing + CI/CD + deployment | Full-stack data app, deployed to Cloud |

### 7.2 Project Descriptions

#### P01 — Personal Dashboard (Beginner)
Build a single-page Streamlit app that displays your profile, skills, projects, and a hobby section. Use `st.columns`, `st.image`, widgets for interactivity (e.g., theme switcher), and `st.metric` for stats.

**Skills practiced:** `st.title`, `st.markdown`, `st.image`, `st.columns`, `st.metric`, `st.sidebar`, theming  
**Grading:** Functionality (40%), UI/UX (30%), Code quality (20%), README (10%)

#### P02 — Data Explorer (Intermediate)
Upload a CSV or Excel file and explore it interactively: filter by columns, sort, show summary statistics, generate charts, and download filtered results.

**Skills practiced:** `st.file_uploader`, Pandas integration, `st.dataframe`, `st.data_editor`, session state, chart selection, `st.download_button`  
**Grading:** Core functionality (35%), Data handling (25%), Visualizations (25%), UX polish (15%)

#### P03 — Form-Based Survey Tool (Intermediate)
Build a multi-step survey application that collects user input via forms, validates entries, stores results locally, and allows export to CSV.

**Skills practiced:** `st.form`, validation, file I/O, `st.progress`, multi-step navigation via session state  
**Grading:** Form design (30%), Validation logic (25%), Data persistence (25%), UX flow (20%)

#### P04 — Real-Time Dashboard (Advanced)
Create a multipage dashboard that shows live-updating metrics, uses caching for expensive computations, and fragments for partial reruns. Use real or simulated data streams.

**Skills practiced:** `st.cache_data`, `refresh_mode="background"`, `@st.fragment(run_every=...)`, multipage navigation, `st.metric` with deltas  
**Grading:** Architecture (30%), Performance (25%), Real-time behavior (25%), Presentation (20%)

#### P05 — CRUD Database App (Advanced)
Build a Create/Read/Update/Delete application backed by SQLite (or PostgreSQL). Include authentication, form-based input, table view, search, and filtering.

**Skills practiced:** `st.connection("sql")`, SQLAlchemy, `st.secrets`, forms, session state for auth, multipage  
**Grading:** Database design (25%), CRUD completeness (25%), Security (20%), UI/UX (20%), Documentation (10%)

#### P06 — ML Model Playground (ML)
Build an app that loads a pre-trained model, accepts user input (text, image, or tabular data), shows predictions with confidence scores, and provides model explanations (SHAP/LIME).

**Skills practiced:** `@st.cache_resource`, model serialization, feature engineering, visualization of model behavior, `st.columns` for side-by-side comparison  
**Grading:** ML pipeline (30%), Interactivity (25%), Explanations (25%), Deployment readiness (20%)

#### P07 — RAG Document Chat (AI/LLM)
Build a document Q&A chatbot that accepts PDF/Text uploads, chunks and embeds them, and answers questions using an LLM with retrieval augmentation.

**Skills practiced:** `st.chat_message`, `st.chat_input`, file upload, LangChain or equivalent, vector store, session-based conversation history  
**Grading:** RAG pipeline (30%), Chat UX (25%), Document handling (25%), Guardrails & error handling (20%)

#### P08 — Capstone Project (Production)
Students propose, design, build, test, and deploy a complete Streamlit application addressing a real-world problem. Must include:

- Problem statement and design document
- Working application with ≥ 3 pages
- Database or API integration
- ML or AI component
- Test suite using `AppTest`
- CI/CD pipeline (GitHub Actions)
- Deployed to Streamlit Community Cloud
- README with setup instructions
- 10-minute presentation + 5-minute Q&A

**Grading:** See [§8.4 Capstone Rubric](#84-capstone-project-rubric)

---

## 8. Assessment Strategy

### 8.1 Grade Distribution

| Component | Weight | Frequency | Format |
|---|---|---|---|
| Weekly Quizzes | 10% | 12 quizzes | Multiple choice + short answer |
| Exercises | 20% | 16 exercises (one per module) | Code submission + screenshot |
| Labs (in-class) | 10% | Attendance + participation | Checked by TA |
| Assignments | 15% | 4 graded assignments | Code + written report |
| Midterm Assessment | 10% | Week 8 | Practical + theory |
| Projects (P01–P07) | 15% | Progressive | Code + demo |
| Capstone Project (P08) | 15% | Week 14–16 | Full app + presentation |
| Pre-Course Assessment | 5% | Week 0 | Placement quiz |

### 8.2 Assessment Taxonomy

| Assessment Type | Bloom's Level | What It Measures |
|---|---|---|
| Quizzes | Remember, Understand | Concept recall, API familiarity |
| Exercises | Apply | Correct use of widgets, APIs, patterns |
| Assignments | Apply, Analyze | Multi-step problem solving, design decisions |
| Labs | Apply | Real-time problem solving with TA guidance |
| Midterm | Analyze, Evaluate | Code review, debugging, architecture decisions |
| Projects | Apply, Analyze, Create | End-to-end application building |
| Capstone | All levels | Complete software development lifecycle |

### 8.3 Quiz Design

**12 quizzes** (one per week, Modules 1–12; Modules 13–16 are covered by capstone)

Each quiz:
- **5 multiple-choice questions** (concept recall)
- **2 short-answer questions** (explain when/why)
- **1 code completion question** (fill in the correct Streamlit API)
- **Time limit:** 15 minutes
- **Format:** Online via LMS (Canvas, Google Forms, or Gradescope)

**Sample Quiz Questions:**

> Q1 (MC): Which Streamlit decorator caches a function result and returns copies on each call?  
> (a) `@st.cache_resource` (b) `@st.cache_data` ✓ (c) `@st.memo` (d) `@st.cache`

> Q2 (Code): Complete this code to display a select box in the sidebar:  
> `___ = st.___.selectbox("Choose", ["A", "B", "C"])`

> Q3 (Short answer): When would you use `@st.cache_resource` instead of `@st.cache_data`?

### 8.4 Capstone Project Rubric

| Criterion | Excellent (A) | Good (B) | Satisfactory (C) | Insufficient (D/F) | Weight |
|---|---|---|---|---|---|
| **Problem & Design** | Clear problem, thorough design doc, justified tech choices | Good problem statement, adequate design | Vague problem, minimal design | No design document | 10% |
| **Functionality** | All features work, handles edge cases, graceful errors | Core features work, minor bugs | Some features broken | App does not run | 25% |
| **Architecture** | Clean separation, reusable components, proper state management | Mostly clean, some mixing | Tangled code, hard to modify | Monolithic, no structure | 15% |
| **Data & ML/AI** | Robust data pipeline, meaningful ML/AI integration | Functional pipeline, basic ML | Minimal data handling | No data integration | 15% |
| **Testing & Security** | Full `AppTest` suite, secrets managed, input validated | Basic tests, secrets in place | Partial tests, some security gaps | No tests, secrets in source | 15% |
| **Deployment** | Deployed to Cloud, CI/CD pipeline, README complete | Deployed, basic README | Partially deployed | Not deployed | 10% |
| **Presentation** | Clear, confident, well-organized, handles Q&A | Good delivery, minor issues | Adequate but disorganized | Unprepared | 10% |

### 8.5 Academic Integrity

- All code must be original or properly attributed (with comments).
- Use of AI assistants (GitHub Copilot, ChatGPT) is **permitted for learning** but must be documented in a `AI_USAGE.md` file in the project repo.
- Plagiarism of design documents, reports, or READMEs is treated per university policy.
- Each exercise and project has a unique dataset or parameter set to reduce copying.

---

## 9. Repository Architecture

### 9.1 Directory Structure

```
Streamlit-for-Data-Science/
│
├── README.md                          # Top-level overview and course syllabus
├── LICENSE                            # MIT License
├── .gitignore                         # Comprehensive Python/Streamlit ignores
├── requirements.txt                   # Core dependencies (pinned)
├── requirements-dev.txt               # Dev/test dependencies
├── setup.sh                           # Streamlit Community Cloud entry point
├── pyproject.toml                     # Project metadata, tool config
│
├── docs/                              # 📚 Documentation & Reference
│   ├── course_blueprint.md            # ← This file (internal planning)
│   ├── syllabus.md                    # Student-facing course syllabus
│   ├── schedule.md                    # Week-by-week schedule
│   ├── prerequisites_guide.md         # Setup instructions for students
│   ├── streamlit_cheatsheet.md        # Quick-reference API cheat sheet
│   ├── deployment_checklist.md        # Step-by-step deployment guide
│   ├── troubleshooting.md             # Common errors and fixes
│   ├── contributing.md                # How to contribute (if open-source)
│   └── figures/                       # Diagrams, screenshots, flowcharts
│       ├── architecture_patterns.png
│       ├── session_state_flow.png
│       ├── caching_diagram.png
│       ├── rag_pipeline.png
│       ├── deployment_workflow.png
│       └── course_progression.png
│
├── readings/                          # 📖 Conceptual readings (Markdown)
│   ├── r01_what_is_streamlit.md
│   ├── r02_streamlit_vs_dash_vs_flask.md
│   ├── r03_widget_internals.md
│   ├── r04_execution_model.md
│   ├── r05_caching_internals.md
│   ├── r06_session_state_internals.md
│   ├── r07_architecture_patterns.md
│   ├── r08_database_design_basics.md
│   ├── r09_api_design_patterns.md
│   ├── r10_ml_serving_patterns.md
│   ├── r11_rag_concepts.md
│   ├── r12_security_best_practices.md
│   ├── r13_testing_strategies.md
│   ├── r14_deployment_options.md
│   └── r15_production_checklist.md
│
├── notebooks/                         # 📓 Jupyter Notebooks (primary learning)
│   ├── 01_first_streamlit_app.ipynb
│   ├── 02_widgets_and_input.ipynb
│   ├── 03_layouts_and_containers.ipynb
│   ├── 04_data_visualization.ipynb
│   ├── 05_session_state.ipynb
│   ├── 06_forms_file_handling.ipynb
│   ├── 07_caching_and_performance.ipynb
│   ├── 08_multipage_apps.ipynb
│   ├── 09_architecture_patterns.ipynb
│   ├── 10_databases.ipynb
│   ├── 11_api_integration.ipynb
│   ├── 12_ml_dashboard.ipynb
│   ├── 13_ai_llm_apps.ipynb
│   ├── 14_testing_security.ipynb
│   ├── 15_deployment_guide.ipynb
│   └── 16_production_readiness.ipynb
│
├── exercises/                         # ✏️ Module exercises (student submissions)
│   ├── exercise_01_hello_streamlit.py
│   ├── exercise_02_widget_master.py
│   ├── exercise_03_layout_designer.py
│   ├── exercise_04_chart_gallery.py
│   ├── exercise_05_state_counter.py
│   ├── exercise_06_form_builder.py
│   ├── exercise_07_cache_challenge.py
│   ├── exercise_08_multipage_nav.py
│   ├── exercise_09_architecture_review.py
│   ├── exercise_10_database_crud.py
│   ├── exercise_11_api_fetcher.py
│   ├── exercise_12_ml_predictor.py
│   ├── exercise_13_chatbot_builder.py
│   ├── exercise_14_test_suite.py
│   ├── exercise_15_deploy_pipeline.py
│   └── exercise_16_monitoring.py
│
├── quizzes/                           # 📝 Quiz files
│   ├── quiz_01_fundamentals.md
│   ├── quiz_02_widgets.md
│   ├── quiz_03_layouts.md
│   ├── quiz_04_visualization.md
│   ├── quiz_05_session_state.md
│   ├── quiz_06_forms_files.md
│   ├── quiz_07_caching.md
│   ├── quiz_08_multipage.md
│   ├── quiz_09_architecture.md
│   ├── quiz_10_databases.md
│   ├── quiz_11_apis.md
│   └── quiz_12_ml_ai.md
│
├── assignments/                       # 📋 Graded assignments
│   ├── assignment_01_basic_app/       # Submit a Streamlit app (Module 3)
│   │   ├── README.md
│   │   └── solution/
│   ├── assignment_02_data_dashboard/  # Interactive dashboard (Module 6)
│   │   ├── README.md
│   │   └── solution/
│   ├── assignment_03_full_stack_app/  # Database + ML app (Module 11)
│   │   ├── README.md
│   │   └── solution/
│   └── assignment_04_production_app/  # Tested, deployed app (Module 15)
│       ├── README.md
│       └── solution/
│
├── assessments/                       # 🎯 Assessment files
│   ├── pre_course_assessment.py       # Placement quiz (Week 0)
│   ├── midterm_practical.py           # Midterm practical (Week 8)
│   ├── midterm_theory.md              # Midterm theory (Week 8)
│   ├── final_exam_study_guide.md      # Study guide (Week 15)
│   └── rubrics/                       # Grading rubrics
│       ├── exercise_rubric.md
│       ├── assignment_rubric.md
│       ├── project_rubric.md
│       └── capstone_rubric.md
│
├── projects/                          # 🚀 Student-facing project templates
│   ├── p01_personal_dashboard/
│   │   ├── README.md
│   │   ├── template/
│   │   └── starter/
│   ├── p02_data_explorer/
│   │   ├── README.md
│   │   ├── template/
│   │   └── starter/
│   ├── p03_survey_tool/
│   │   ├── README.md
│   │   ├── template/
│   │   └── starter/
│   ├── p04_realtime_dashboard/
│   │   ├── README.md
│   │   ├── template/
│   │   └── starter/
│   ├── p05_crud_app/
│   │   ├── README.md
│   │   ├── template/
│   │   └── starter/
│   ├── p06_ml_playground/
│   │   ├── README.md
│   │   ├── template/
│   │   └── starter/
│   ├── p07_rag_chat/
│   │   ├── README.md
│   │   ├── template/
│   │   └── starter/
│   └── p08_capstone/
│       ├── README.md
│       ├── proposal_template.md
│       ├── design_template.md
│       ├── CI_template.yml
│       └── rubric.md
│
├── apps/                              # 🖥️ Runnable Streamlit apps
│   ├── hello.py                       # Module 01 companion
│   ├── widgets_demo.py                # Module 02 companion
│   ├── layouts_demo.py                # Module 03 companion
│   ├── charts_demo.py                 # Module 04 companion
│   ├── state_demo.py                  # Module 05 companion
│   ├── forms_demo.py                  # Module 06 companion
│   ├── caching_demo.py                # Module 07 companion
│   ├── multipage_demo/                # Module 08 companion (multipage)
│   │   ├── app.py
│   │   ├── pages/
│   │   │   ├── 1_home.py
│   │   │   ├── 2_data.py
│   │   │   └── 3_about.py
│   ├── architecture_demo/             # Module 09 companion
│   │   ├── app.py
│   │   ├── utils/
│   │   └── components/
│   ├── db_demo.py                     # Module 10 companion
│   ├── api_demo.py                    # Module 11 companion
│   ├── ml_demo.py                     # Module 12 companion
│   ├── ai_chat_demo.py                # Module 13 companion
│   ├── test_demo.py                   # Module 14 companion
│   └── deployed_app/                  # Module 15–16 companion (deployed)
│       ├── app.py
│       └── requirements.txt
│
├── data/                              # 📊 Shared datasets
│   ├── sample.csv
│   ├── sample.xlsx
│   ├── students.db                    # SQLite for Module 10
│   ├── sample_model.joblib            # Pre-trained model for Module 12
│   └── sample_documents/             # PDF/TXT for Module 13 RAG
│       ├── document1.pdf
│       └── document2.txt
│
├── tests/                             # 🧪 Course test examples & solutions
│   ├── test_hello.py
│   ├── test_widgets.py
│   ├── test_caching.py
│   └── test_ml_demo.py
│
├── instructor/                        # 👩‍🏫 Instructor-only materials
│   ├── answer_keys/                   # Exercise & quiz solutions
│   │   ├── exercise_solutions/
│   │   └── quiz_solutions/
│   ├── grading_guide.md
│   ├── office_hours_faq.md
│   ├── lecture_slides/                # Slide decks (if used)
│   │   ├── week01_slides.pdf
│   │   └── ...
│   └── workshop_materials/
│       ├── setup_workshop.md
│       └── deployment_workshop.md
│
└── .streamlit/                        # ⚙️ Streamlit configuration
    └── config.toml                    # Theme and server settings
```

### 9.2 File Naming Conventions

| File Type | Convention | Example |
|---|---|---|
| Notebooks | `NN_topic_name.ipynb` | `01_first_streamlit_app.ipynb` |
| Exercises | `exercise_NN_topic.py` | `exercise_01_hello_streamlit.py` |
| Quizzes | `quiz_NN_topic.md` | `quiz_01_fundamentals.md` |
| Readings | `rNN_topic.md` | `r01_what_is_streamlit.md` |
| Apps | `topic_demo.py` or `topic_demo/` | `widgets_demo.py`, `multipage_demo/` |
| Projects | `pNN_project_name/` | `p01_personal_dashboard/` |
| Figures | `topic_diagram.png` | `caching_diagram.png` |

### 9.3 Cross-Linking Strategy

Every content file contains explicit cross-references using relative Markdown links:

```markdown
## Related Materials
- 📓 Notebook: [Session State Deep Dive](../notebooks/05_session_state.ipynb)
- ✏️ Exercise: [State Counter Challenge](../exercises/exercise_05_state_counter.py)
- 📖 Reading: [Session State Internals](../readings/r06_session_state_internals.md)
- 🚀 Project: [Real-Time Dashboard](../projects/p04_realtime_dashboard/)
- 🖥️ Demo App: [Stream it live](../apps/state_demo.py)
- 📝 Quiz: [Test your knowledge](../quizzes/quiz_05_session_state.md)
```

The **top-level README.md** serves as the navigation hub with a visual course map linking to all modules, notebooks, projects, and resources.

---

## 10. Dependency Strategy

### 10.1 Core Dependencies (Always Required)

| Package | Version Constraint | Purpose |
|---|---|---|
| `streamlit` | `>=1.60.0,<2.0.0` | Core framework |
| `numpy` | `>=1.24.0` | Numerical computing |
| `pandas` | `>=2.0.0` | Data manipulation |
| `matplotlib` | `>=3.7.0` | Static plotting |
| `plotly` | `>=5.15.0` | Interactive plotting |
| `scikit-learn` | `>=1.3.0` | Machine learning (ML modules) |

### 10.2 Optional Dependencies (Module-Specific)

| Package | Version Constraint | Required By | Notes |
|---|---|---|---|
| `altair` | `>=5.0.0` | Module 04 | Declarative visualization |
| `seaborn` | `>=0.12.0` | Module 04 | Statistical visualization |
| `sqlalchemy` | `>=2.0.0` | Module 10 | Database ORM |
| `pymysql` | `>=1.1.0` | Module 10 | MySQL connector |
| `psycopg2-binary` | `>=2.9.0` | Module 10 | PostgreSQL connector |
| `requests` | `>=2.31.0` | Module 11 | HTTP client |
| `httpx` | `>=0.24.0` | Module 11 | Async HTTP client |
| `shap` | `>=0.43.0` | Module 12 | Model explanations |
| `openai` | `>=1.0.0` | Module 13 | OpenAI API |
| `langchain` | `>=0.1.0` | Module 13 | LLM orchestration |
| `chromadb` | `>=0.4.0` | Module 13 | Vector store for RAG |
| `langchain-community` | `>=0.0.0` | Module 13 | LangChain community integrations |
| `tiktoken` | `>=0.5.0` | Module 13 | Token counting |

### 10.3 Dev/Test Dependencies

| Package | Version Constraint | Purpose |
|---|---|---|
| `pytest` | `>=7.0.0` | Test runner |
| `ruff` | `>=0.1.0` | Linter & formatter |
| `mypy` | `>=1.5.0` | Type checking |
| `pre-commit` | `>=3.0.0` | Git hooks |
| `pip-audit` | `>=2.6.0` | Security scanning |

### 10.4 Dependency Files

| File | Purpose | Audience |
|---|---|---|
| `requirements.txt` | Core + all optional deps (pinned) | Students, deployment |
| `requirements-core.txt` | Core only | Minimal install |
| `requirements-dev.txt` | Dev/test tools | Developers, TAs |
| `pyproject.toml` | Project metadata, tool configs | Developers |

### 10.5 Version Pinning Strategy

- **Notebooks & exercises:** Pin to `>=X.Y` (compatible ranges) so students can use newer patch releases.
- **Projects & apps deployed to Cloud:** Pin exact versions for reproducibility.
- **CI/CD:** Use lockfile generation (`pip-compile` or `uv lock`) for deterministic builds.

---

## 11. Deployment Strategy

### 11.1 Deployment Progression

| Stage | Tool | When | Purpose |
|---|---|---|---|
| **Local development** | `streamlit run` | Every session | Rapid iteration |
| **Local sharing** | ngrok / localtunnel | Week 4+ | Demo to peers/instructor |
| **GitHub Pages** (README) | GitHub | Week 1+ | Course materials hosting |
| **Streamlit Community Cloud** | Cloud dashboard | Week 15 | Free production deployment |
| **Docker** | Dockerfile | Week 14 | Containerized deployment |
| **Cloud platform** (optional) | HuggingFace Spaces, Render | Week 15+ | Alternative hosting |

### 11.2 Streamlit Community Cloud Deployment Guide

**Prerequisites:**
1. GitHub account with repository pushed.
2. `requirements.txt` at repo root.
3. Entry point file (e.g., `app.py`) at repo root or well-known path.

**Steps:**
1. Go to [share.streamlit.io](https://share.streamlit.io).
2. Sign in with GitHub.
3. Click "New app" → select repository, branch, and main file.
4. Click "Deploy!".
5. Add secrets via the dashboard (Advanced settings).

**Configuration:**
```toml
# .streamlit/secrets.toml (DO NOT commit real secrets)
[database]
host = "localhost"
port = 5432
name = "myapp"

[api]
key = "your-api-key-here"
```

**Sleep policy:** Apps without traffic for 7 consecutive days go to sleep. First visit after sleep triggers a wake-up (30–60s cold start).

**Student deployment checklist:**
- [ ] `requirements.txt` lists all dependencies with pinned versions
- [ ] Entry point file runs without errors
- [ ] No hardcoded secrets in source code
- [ ] `.streamlit/secrets.toml` is in `.gitignore`
- [ ] README explains what the app does
- [ ] App handles errors gracefully (no crashes on bad input)
- [ ] Tested locally before pushing

### 11.3 Docker Deployment

```dockerfile
# Dockerfile
FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8501
HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health
ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

### 11.4 CI/CD Pipeline (GitHub Actions)

```yaml
# .github/workflows/ci.yml
name: CI
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.11"
      - run: pip install -r requirements.txt -r requirements-dev.txt
      - run: ruff check .
      - run: mypy .
      - run: pytest tests/ -v

  deploy:
    needs: test
    if: github.ref == 'refs/heads/main'
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Deploy to Streamlit Cloud
        run: echo "Streamlit Cloud auto-deploys on push to main"
```

---

## 12. Security Strategy

### 12.1 Security Principles

1. **Never commit secrets** — `.streamlit/secrets.toml` is always in `.gitignore`.
2. **Validate all inputs** — Use `st.text_input` `validate` parameter (1.62) and server-side checks.
3. **Least privilege** — Database users have minimal required permissions.
4. **Defense in depth** — Multiple layers of protection (client validation + server checks).
5. **Security by default** — Start with the most secure configuration and relax only when needed.

### 12.2 Streamlit Security Features to Teach

| Feature | Streamlit Version | What It Does | Teaching Module |
|---|---|---|---|
| `server.allowedHosts` | 1.60+ | Restricts WebSocket origins | M14, M15 |
| `server.maxWidgetStateSize` | 1.60+ | Limits widget state payload (default 25 MB) | M14 |
| `client.disableDataExport` | 1.60+ | Disables CSV export/clipboard for dataframes | M14 |
| Host message origin validation | 1.60+ | Prevents spoofing (CWE-346) | M14 |
| Query string caps | 1.60+ | Limits to 512 KiB / 1,000 fields (CWE-770) | M14 |
| URL sanitization | 1.60+ | Sanitizes `st.link_button`, `st.image`, Graphviz links | M14 |
| `disabled` server-side enforcement | 1.60+ | Disabled widgets reject browser values | M02, M14 |
| `validate` parameter (text_input) | 1.62+ | Client-side validation (email, URL, phone, search) | M02, M06 |
| HTML/PyDeck tooltip escaping | 1.60+ | Prevents XSS in tooltip interpolations | M14 |
| WebSocket security hardening | 1.60+ | Rejects malformed messages, hides tracebacks | M16 |

### 12.3 Security Topics by Module

| Module | Security Topic |
|---|---|
| M01 | `.gitignore` for secrets, never hardcode API keys |
| M02 | Input validation, `disabled` widget enforcement |
| M06 | File upload security (type restrictions, size limits) |
| M10 | SQL injection prevention (parameterized queries), secrets in `secrets.toml` |
| M11 | API key management, HTTPS, rate limiting |
| M13 | LLM prompt injection awareness, output sanitization, token limits |
| M14 | Full security module: OWASP Top 10, `AppTest`, CI/CD, auth patterns |
| M15 | Community Cloud secrets, CORS/XSRF config, `allowedHosts` |

### 12.4 Secrets Management Best Practices

```toml
# .streamlit/secrets.toml — template (no real values)
[database]
host = "PLACEHOLDER"
port = 5432
name = "PLACEHOLDER"
user = "PLACEHOLDER"
password = "PLACEHOLDER"

[openai]
api_key = "sk-PLACEHOLDER"

[auth]
username = "PLACEHOLDER"
password_hash = "PLACEHOLDER"
```

- Never log secrets or print them in app output.
- Use `st.secrets["section"]["key"]` in app code.
- For Community Cloud, add secrets via the web dashboard.
- Rotate secrets regularly; document the rotation process.

---

## 13. QA Strategy

### 13.1 Quality Assurance Layers

| Layer | Tool/Method | Scope | Frequency |
|---|---|---|---|
| **Linting** | Ruff | All Python files | Every commit (pre-commit hook) |
| **Type checking** | MyPy | All Python files | Every commit (CI) |
| **Testing** | pytest + `AppTest` | All apps and exercises | Every push (CI) |
| **Notebook validation** | `nbval` or `nbmake` | All notebooks | Weekly or before release |
| **Security scanning** | `pip-audit`, `bandit` | Dependencies + code | Weekly |
| **Documentation review** | Manual review + Vale | All Markdown files | Before release |
| **Accessibility** | Manual screen reader test | Deployed apps | Per project |
| **Cross-browser** | Manual test (Chrome, Firefox, Safari) | Deployed apps | Per project |

### 13.2 Testing Strategy

**Unit Tests (`tests/`):**
```python
# tests/test_hello.py
from streamlit.testing.v1 import AppTest

def test_hello_app():
    at = AppTest.from_file("apps/hello.py")
    at.run()
    assert not at.exception
    assert at.title[0].value == "Hello, Streamlit!"
```

**Exercise Validation:**
Each exercise includes a self-check function:
```python
# exercises/exercise_01_hello_streamlit.py
def self_check():
    """Run this to verify your exercise submission."""
    from streamlit.testing.v1 import AppTest
    at = AppTest.from_file("exercise_01_hello_streamlit.py")
    at.run()
    assert not at.exception, "App threw an exception"
    # ... specific checks
    print("✅ All checks passed!")
```

**Notebook Validation:**
```bash
# Run all notebooks through nbmake
nbmake notebooks/*.ipynb --timeout=300
```

### 13.3 Content Quality Standards

| Criterion | Standard |
|---|---|
| **Accuracy** | All API references verified against Streamlit docs (see §15) |
| **Reproducibility** | Every code cell runs without modification on fresh install |
| **Freshness** | Reviewed against Streamlit release notes quarterly |
| **Accessibility** | Images have alt text; color is not the sole indicator |
| **Conciseness** | Readings ≤ 2000 words; no filler paragraphs |
| **Cross-references** | Every content file links to ≥ 2 related materials |

### 13.4 Continuous Improvement

- **Student feedback:** End-of-module anonymous surveys (3 questions: helpful? confusing? suggestions?)
- **Issue tracking:** GitHub Issues for bug reports and content corrections
- **Version log:** Track content updates in `CHANGELOG.md`
- **Instructor review:** Bi-weekly check-in to assess pacing and difficulty

---

## 14. Cross-Linking & Navigation Strategy

### 14.1 Navigation Hierarchy

```
README.md (Course Home)
  ├── docs/syllabus.md (Student Syllabus)
  ├── docs/schedule.md (Week-by-Week)
  ├── Module → Reading + Notebook + Exercise + Quiz
  │     └── Project (where applicable)
  └── Cross-links between all materials
```

### 14.2 Link Types

| Link Type | Format | Example |
|---|---|---|
| **Module → Reading** | `📖 [Reading Title](../readings/rNN_topic.md)` | In notebook or exercise header |
| **Module → Notebook** | `📓 [Notebook Title](../notebooks/NN_topic.ipynb)` | In schedule, syllabus |
| **Module → Exercise** | `✏️ [Exercise](../exercises/exercise_NN_topic.py)` | In notebook footer |
| **Module → Quiz** | `📝 [Quiz](../quizzes/quiz_NN_topic.md)` | In schedule |
| **Module → App** | `🖥️ [Demo App](../apps/topic_demo.py)` | In notebook |
| **Module → Project** | `🚀 [Project](../projects/pNN_name/)` | In notebook, schedule |
| **Reading → Notebook** | `📓 [See it in code](../notebooks/NN_topic.ipynb)` | In reading body |
| **Exercise → Solution** | `✅ [Solution](../instructor/answer_keys/exercise_solutions/NN.py)` | Instructor materials only |

### 14.3 README Navigation Hub

The top-level `README.md` serves as the entry point with:

1. **Course banner and badges** (Streamlit version, Python version, license)
2. **One-sentence description**
3. **Visual course map** (mermaid diagram or ASCII art showing progression)
4. **Quick start** (install + run)
5. **Module table** (16 rows, each linking to notebook + reading + exercise)
6. **Project ladder** (8 projects with level indicators)
7. **Assessment overview** (grade breakdown)
8. **Resources** (Streamlit docs, community, cheat sheets)

---

## 15. Topics Requiring Documentation Verification

The following topics reference Streamlit features that have recently changed or are new. **Before content creation, each must be verified against the current official documentation.**

| Topic | Why Verification Needed | Current Status (Sept 2026) |
|---|---|---|
| `st.text_input` `validate` and `type` parameters | New in 1.62 (Aug 2026) | Confirm parameter names, allowed types, defaults |
| `wrap` parameter on `st.columns`, `st.button`, `st.checkbox`, `st.toggle`, `st.multiselect` | New in 1.62 | Confirm API signature and behavior |
| `refresh_mode="background"` for `st.cache_data` / `st.cache_resource` | New in 1.61 (Aug 2026) | Confirm exact behavior, edge cases, interactions |
| `st.dataframe` `lazy` parameter and Polars LazyFrame support | New in 1.61 | Confirm API, limitations, performance characteristics |
| `st.metric` `icon` parameter | New in 1.61 | Confirm parameter name and accepted values |
| `st.time_input` revamp (segments, format, seconds) | New in 1.61 | Confirm new API, `format` parameter options |
| `st.Page` as a proper class | Changed in 1.61 | Confirm `isinstance` behavior, `StreamlitPage` alias |
| `server.allowedHosts` config | New in 1.61 | Confirm config syntax and behavior |
| `st.pyplot` requires explicit figure | Breaking change in 1.62 | Confirm migration path and error messages |
| `st.pyplot` SVG support (`format="svg"`) | New in 1.62 | Confirm parameter and behavior |
| `st.tabs` `height` parameter | New in 1.60 | Confirm API |
| `st.columns` pixel gap (integer) | New in 1.60 | Confirm accepted values |
| `server.maxWidgetStateSize` config | New in 1.60 | Confirm default, units, range |
| `client.disableDataExport` config | New in 1.60 | Confirm scope and behavior |
| `st.download_button` auto-infer `file_name` | New in 1.61 | Confirm behavior with various file types |
| `st.html` / `st.iframe` pathlib.Path deprecation | New in 1.60 | Confirm migration path |
| `st.cache` removal | Breaking in 1.62 | Confirm error message, migration guide |
| `runner.cacheHashSeed` config | Bug fix in 1.62 | Confirm current behavior and docs |
| `@st.fragment` `run_every` behavior | Multiple fixes in 1.60–1.62 | Confirm current behavior, AppTest compatibility |
| `st.navigation` API | Verify current API | Confirm parameters and usage patterns |
| AppTest multipage path handling | Fixed in 1.61 | Confirm test patterns for multipage apps |
| Chart categorical/sequential/diverging color config | New in 1.62 | Confirm config.toml syntax |
| Font-weight increments of 50 | New in 1.62 | Confirm config syntax |
| `use_column_width` removal from `st.image` | Breaking in 1.61 | Confirm replacement (`width` parameter) |

**Verification process:**
1. Before writing content for any module, check the official Streamlit docs page for each API used.
2. Cross-reference with release notes for versions 1.60, 1.61, and 1.62.
3. Test each code snippet locally with the target Streamlit version.
4. Mark verified items in the content with a comment: `<!-- Verified against docs.streamlit.io on YYYY-MM-DD -->`

---

## Appendices

### Appendix A: Course Syllabus Outline (for `docs/syllabus.md`)

| Week | Topic | Module | Notebook | Exercise | Project Milestone |
|---|---|---|---|---|---|
| 0 | Setup & Pre-Course Assessment | — | — | — | — |
| 1 | Fundamentals + Widgets | M01, M02 | N01, N02 | E01, E02 | P01 started |
| 2 | Layouts + Visualization | M03, M04 | N03, N04 | E03, E04 | P01 due, P02 started |
| 3 | Visualization (cont.) + Session State | M04, M05 | N04, N05 | E05 | P02 due, P03 started |
| 4 | Session State (cont.) + Forms | M05, M06 | N05, N06 | E06 | P03 due |
| 5 | Caching + Performance | M07 | N07 | E07 | P04 started |
| 6 | Multipage Apps | M08 | N08 | E08 | P04 due |
| 7 | Architecture + Databases | M09, M10 | N09, N10 | E09, E10 | P05 started |
| 8 | Midterm + APIs | M11 | N11 | E11 | P05 due, Assignment 03 due |
| 9 | ML Dashboards | M12 | N12 | E12 | P06 started |
| 10 | ML (cont.) + NLP/AI | M12, M13 | N12, N13 | — | P06 due, P07 started |
| 11 | AI/LLM Apps + RAG | M13 | N13 | — | P07 due |
| 12 | Testing & Security | M14 | N14 | E14 | Capstone proposal due |
| 13 | Deployment | M15 | N15 | E15 | Capstone development |
| 14 | Production & Monitoring | M16 | N16 | E16 | Capstone dev + Assignment 04 due |
| 15 | Capstone Presentations | — | — | — | Capstone presentation |
| 16 | Course Review & Wrap-up | — | — | — | Final materials due |

### Appendix B: Reading Descriptions

| # | Title | Module | Description | Est. Length |
|---|---|---|---|---|
| R01 | What is Streamlit? | M01 | Origin story, philosophy, comparison with alternatives | 1,500 words |
| R02 | Streamlit vs Dash vs Flask vs Gradio | M01 | Feature comparison, use-case analysis, decision framework | 2,000 words |
| R03 | Widget Internals | M02 | How widgets communicate between frontend and backend | 1,500 words |
| R04 | The Streamlit Execution Model | M05 | Top-to-bottom reruns, why state is needed, lifecycle | 2,000 words |
| R05 | Caching Internals | M07 | Hash-based caching, `st.cache_data` vs `st.cache_resource`, TTL | 1,800 words |
| R06 | Session State Internals | M05 | Per-session isolation, dict-like behavior, lifecycle | 1,500 words |
| R07 | Architecture Patterns for Streamlit | M09 | MVC-like patterns, component architecture, state management | 2,000 words |
| R08 | Database Design Basics | M10 | Normalization, schema design, ORM vs raw SQL | 1,800 words |
| R09 | API Design Patterns | M11 | REST conventions, pagination, error handling, authentication | 1,800 words |
| R10 | ML Serving Patterns | M12 | Batch vs real-time, model serialization, feature stores | 2,000 words |
| R11 | RAG Concepts | M13 | Retrieval-augmented generation, embeddings, vector stores, chunking | 2,000 words |
| R12 | Security Best Practices | M14 | OWASP Top 10 for Streamlit, secrets, input validation | 2,000 words |
| R13 | Testing Strategies | M14 | Unit vs integration vs e2e, AppTest patterns, CI integration | 1,500 words |
| R14 | Deployment Options | M15 | Community Cloud, Docker, HuggingFace Spaces, cloud platforms | 1,500 words |
| R15 | Production Checklist | M16 | Monitoring, logging, scaling, maintenance, SLOs | 1,500 words |

### Appendix C: Streamlit API Quick Reference by Module

| Module | Primary APIs | Secondary APIs |
|---|---|---|
| M01 | `st.title`, `st.header`, `st.write`, `st.markdown`, `st.code` | `st.image`, `st.latex`, `st.divider` |
| M02 | `st.text_input`, `st.number_input`, `st.slider`, `st.selectbox`, `st.button` | `st.checkbox`, `st.toggle`, `st.radio`, `st.color_picker` |
| M03 | `st.sidebar`, `st.columns`, `st.tabs`, `st.container`, `st.expander` | `st.popover`, `st.status`, `st.progress`, `st.spinner` |
| M04 | `st.line_chart`, `st.bar_chart`, `st.plotly_chart`, `st.pyplot` | `st.altair_chart`, `st.pydeck_chart`, `st.graphviz_chart` |
| M05 | `st.session_state`, `st.fragment` | Callbacks (`on_click`, `on_change`), `st.rerun` |
| M06 | `st.form`, `st.form_submit_button`, `st.file_uploader`, `st.download_button` | `st.text_area`, `st.date_input`, `st.time_input` |
| M07 | `@st.cache_data`, `@st.cache_resource`, `@st.fragment` | `st.cache_data.clear`, `run_every`, `refresh_mode` |
| M08 | `st.navigation`, `st.Page`, `st.query_params` | `st.set_page_config`, page directory convention |
| M10 | `st.connection`, `st.connections.SQLConnection` | SQLAlchemy, `conn.read_sql`, `conn.query` |
| M11 | `requests`, `httpx`, `st.components.v1` | Custom components, JSON processing |
| M12 | `@st.cache_resource` (model), `st.dataframe`, `st.plotly_chart` | SHAP, LIME, `st.columns` for comparison |
| M13 | `st.chat_message`, `st.chat_input` | `st.session_state` for chat history, streaming |
| M14 | `st.testing.AppTest`, `st.secrets` | Auth patterns, `server.*` config |
| M15 | Community Cloud dashboard, `requirements.txt` | `setup.sh`, Docker, secrets in Cloud |
| M16 | Logging, monitoring, `config.toml` | MLOps integration, versioning |

### Appendix D: Course Learning Outcomes (CLOs)

Upon successful completion of this course, students will be able to:

| CLO | Description | Bloom's Level | Assessed By |
|---|---|---|---|
| **CLO1** | Explain Streamlit's architecture, execution model, and widget lifecycle | Understand | Quizzes, Midterm |
| **CLO2** | Build interactive data applications using Streamlit widgets, layouts, and state management | Apply | Exercises, Projects |
| **CLO3** | Implement effective data visualization strategies using Streamlit's native and third-party chart integrations | Apply | Exercises, P02 |
| **CLO4** | Design and implement caching, performance optimization, and efficient data flow in Streamlit apps | Analyze | Assignments, P04 |
| **CLO5** | Connect Streamlit applications to databases and external APIs for persistent data and real-time information | Apply | Exercises, P05 |
| **CLO6** | Deploy machine learning models as interactive Streamlit applications with model explanation and comparison capabilities | Apply, Analyze | P06 |
| **CLO7** | Build AI-powered applications including chat interfaces and RAG systems using LLMs and Streamlit | Apply, Create | P07 |
| **CLO8** | Apply testing, security best practices, and CI/CD pipelines to Streamlit applications | Evaluate | M14, P08 |
| **CLO9** | Deploy, monitor, and maintain Streamlit applications in production environments | Evaluate | P08, M15–M16 |
| **CLO10** | Design and execute a complete software development lifecycle for a data application, from requirements to deployment | Create | Capstone (P08) |

### Appendix E: Risk Register

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| Streamlit API breaking changes during semester | Medium | High | Pin version in `requirements.txt`; maintain `CHANGELOG` |
| Community Cloud downtime during project deadline | Medium | Medium | Allow Docker/local deployment as alternative |
| Students lack prerequisite Python/data skills | Medium | High | Pre-course assessment; supplementary materials in `readings/` |
| LLM API costs for Module 13 exercises | High | Medium | Use free tiers (Ollama local, HuggingFace inference API) |
| Notebook environments differ from student setups | Low | Medium | Docker-based dev environment option; clear setup guide |
| Rapid Streamlit feature churn (1.60 → 1.62 in 3 months) | High | Medium | Quarterly content review; version-pinned code examples |

---

## Revision History

| Version | Date | Author | Changes |
|---|---|---|---|
| 1.0 | 2026-09-02 | Dr. Muhammad Nadeem Majeed | Initial blueprint |

---

> **Next Steps:** This blueprint is the foundation for content creation. The following files should be created next:
> 1. `docs/syllabus.md` — Student-facing syllabus derived from this blueprint
> 2. `docs/schedule.md` — Week-by-week detailed schedule
> 3. `README.md` (update) — Add navigation hub, course map, and quick start
> 4. `requirements.txt` — Core dependency list
> 5. `notebooks/01_first_streamlit_app.ipynb` — First notebook
> 6. `apps/hello.py` — First companion app
> 7. `exercises/exercise_01_hello_streamlit.py` — First exercise

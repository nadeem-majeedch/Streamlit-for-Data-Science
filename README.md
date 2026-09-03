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
├── readings/                📖 Conceptual readings
│   ├── 01_streamlit_introduction.md   # What is Streamlit, comparisons
│   ├── 02_first_streamlit_app.md      # Installation, first app, execution model
│   ├── 03_streamlit_widgets_and_input.md  # All widget types, forms, validation
│   ├── 04_widget_keys_and_behavior.md # Keys, identity, session_state, callbacks
│   ├── 05_layouts_and_containers.md  # Sidebar, columns, tabs, expanders, containers
│   └── 06_dashboard_design_ui_ux.md  # Status, metrics, accessibility, DS dashboard design
├── notebooks/               📓 Jupyter notebooks (primary learning)
│   ├── 01_Streamlit_Introduction.ipynb # Concepts, comparisons, intuition
│   ├── 02_First_Streamlit_App.ipynb    # Installation, text elements, rerun model
│   ├── 03_streamlit_widgets.ipynb      # Every widget type, keys, forms
│   ├── 04_interactive_ds_controls.ipynb # Dataset filters, ML params, validation
│   ├── 05_layouts_and_containers.ipynb  # Sidebar, columns, tabs, containers, popover, dialog
│   └── 06_data_science_dashboards.ipynb # KPIs, status feedback, accessibility, dashboard design
├── exercises/               ✏️ Module exercises (one per module)
├── quizzes/                 📝 Weekly quizzes
├── assignments/             📋 Graded assignments (4 per semester)
├── assessments/             🎯 Pre-course, midterm, final exam materials
├── projects/                🚀 Project templates (P01–P08 Capstone)
├── instructor/              👩‍🏫 Answer keys, grading guides, slides
├── apps/                    🖥️ Runnable Streamlit demo apps
│   ├── hello.py                        # Environment verification
│   ├── 01_introduction_demo.py         # Text elements, rerun model, data display
│   ├── 02_first_app_demo.py            # Complete first app with session state
│   ├── 03_widgets_demo.py              # Widgets showcase, session_state demo
│   ├── 04_forms_demo.py                # Forms, validation patterns
│   ├── 05_layouts_demo.py              # Layout elements showcase
│   └── 06_dashboard_demo.py            # Complete Sales Analytics Dashboard
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
- 📓 Notebook: [Session State Deep Dive](../notebooks/05_session_state.ipynb)
- ✏️ Exercise: [State Counter Challenge](../exercises/exercise_05_state_counter.py)
- 📖 Reading: [Session State Internals](../readings/r06_session_state_internals.md)
- 🚀 Project: [Real-Time Dashboard](../projects/p04_realtime_dashboard/)
- 🖥️ Demo App: [Run it](../apps/state_demo.py)
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
| 4 | [M04](notebooks/) | Data Visualization | Intermediate |
| 5 | [M05](notebooks/) | Session State & App Memory | Intermediate |
| 5–6 | [M06](notebooks/) | Forms, Inputs & File Handling | Intermediate |
| 7 | [M07](notebooks/) | Caching, Fragments & Performance | Advanced |
| 8 | [M08](notebooks/) | Multipage Apps & Navigation | Advanced |
| 8–9 | [M09](notebooks/) | Architecture & Design Patterns | Advanced |
| 10 | [M10](notebooks/) | Databases & Persistent Storage | Advanced |
| 11 | [M11](notebooks/) | APIs, Connectors & External Data | Advanced |
| 12 | [M12](notebooks/) | ML Model Deployment | ML |
| 13 | [M13](notebooks/) | NLP, AI & LLM Applications | AI/LLM |
| 14 | [M14](notebooks/) | Testing, Security & CI/CD | Advanced |
| 15 | [M15](notebooks/) | Streamlit Community Cloud & Deployment | Deployment |
| 16 | [M16](notebooks/) | Production, Maintenance & Monitoring | Production |

> **Note:** Content for notebooks, exercises, quizzes, and projects is being built out progressively. See [docs/course_blueprint.md](docs/course_blueprint.md) for the full planned structure.

### 🚀 Project Ladder

| # | Project | Level | Key Skills |
|---|---|---|---|
| P01 | Personal Dashboard | Beginner | `st.write`, widgets, layout, theming |
| P02 | Data Explorer | Intermediate | File upload, Pandas, charts, session state |
| P03 | Form-Based Survey Tool | Intermediate | Forms, validation, file handling |
| P04 | Real-Time Dashboard | Advanced | Caching, fragments, `run_every` |
| P05 | CRUD Database App | Advanced | SQL, forms, authentication |
| P06 | ML Model Playground | ML | Model loading, inference, SHAP |
| P07 | RAG Document Chat | AI/LLM | Chat UI, embeddings, vector store |
| P08 | **Capstone Project** | Production | All skills + CI/CD + deployment |

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

| Component | Weight | Count |
|---|---|---|
| Weekly Quizzes | 10% | 12 |
| Exercises | 20% | 16 |
| Labs (in-class) | 10% | Weekly |
| Assignments | 15% | 4 |
| Midterm | 10% | 1 |
| Projects (P01–P07) | 15% | 7 |
| Capstone (P08) | 15% | 1 |

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

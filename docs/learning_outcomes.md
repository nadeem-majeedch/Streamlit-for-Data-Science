# Learning Outcomes

> **Streamlit for Data Science — Learn, Build, Deploy**  
> Course Learning Outcomes (CLOs) with full assessment and resource mapping.

---

## Course Learning Outcomes

Upon successful completion of this course, students will be able to:

| # | CLO | Bloom's Level | Primary Modules |
|---|---|---|---|
| [CLO1](#clo1--explain-streamlit-core-concepts) | Explain Streamlit's execution model, architecture, and widget lifecycle | Understand | M01, M02, M05 |
| [CLO2](#clo2--build-interactive-applications) | Build interactive data applications using Streamlit widgets, layouts, and state management | Apply | M01–M03, M05 |
| [CLO3](#clo3--implement-data-visualization) | Implement data visualization strategies using Streamlit's native and third-party chart integrations | Apply | M04 |
| [CLO4](#clo4--manage-application-state) | Design and manage application state across reruns using session state, callbacks, and fragments | Apply, Analyze | M05, M07 |
| [CLO5](#clo5--optimize-performance) | Optimize Streamlit application performance through caching, fragments, and lazy loading | Analyze | M07, M08 |
| [CLO6](#clo6--design-well-architected-applications) | Design well-structured Streamlit applications using proven architecture patterns | Apply, Analyze | M08, M09 |
| [CLO7](#clo7--connect-to-data-sources) | Connect Streamlit apps to databases and external APIs for persistent data and real-time information | Apply | M10, M11 |
| [CLO8](#clo8--deploy-ml-models) | Deploy machine learning models as interactive Streamlit applications with explanations | Apply, Analyze | M12 |
| [CLO9](#clo9--build-ai-powered-applications) | Build AI-powered applications including chat interfaces and RAG systems | Apply, Create | M13 |
| [CLO10](#clo10--test-and-secure-applications) | Apply testing, security best practices, and CI/CD to Streamlit applications | Evaluate | M14 |
| [CLO11](#clo11--deploy-to-production) | Deploy, monitor, and maintain Streamlit applications in production environments | Evaluate | M15, M16 |
| [CLO12](#clo12--execute-full-development-lifecycle) | Execute a complete software development lifecycle for a data application, from requirements to deployment | Create | M14–M16, P08 |

---

## CLO Detail & Traceability

### CLO1 — Explain Streamlit Core Concepts

> **"Students can explain Streamlit's execution model, architecture, and widget lifecycle."**

**Bloom's Level:** Understand

| Resource Type | Resource | Description |
|---|---|---|
| **Reading** | [R01 — What is Streamlit?](../readings/r01_what_is_streamlit.md) | Origin, philosophy, comparison with alternatives |
| **Reading** | [R02 — Streamlit vs Alternatives](../readings/r02_streamlit_vs_dash_vs_flask.md) | Feature comparison, use-case analysis |
| **Reading** | [R04 — The Execution Model](../readings/r04_execution_model.md) | Top-to-bottom reruns, lifecycle |
| **Reading** | [R06 — Session State Internals](../readings/r06_session_state_internals.md) | Per-session isolation, dict-like behavior |
| **Notebook** | [N01 — Your First Streamlit App](../notebooks/01_first_streamlit_app.ipynb) | Hands-on introduction |
| **Notebook** | [N02 — The Widget Zoo](../notebooks/02_widgets_and_input.ipynb) | Widget fundamentals |
| **Notebook** | [N05 — Session State Deep Dive](../notebooks/05_session_state.ipynb) | Execution model in practice |
| **Exercise** | [E01 — Hello Streamlit](../exercises/exercise_01_hello_streamlit.py) | Build a basic app |
| **Quiz** | [Q01 — Fundamentals](../quizzes/quiz_01_fundamentals.md) | Concept recall (MC + short answer) |
| **Quiz** | [Q02 — Widgets](../quizzes/quiz_02_widgets.md) | Widget API knowledge |
| **Assessment** | [Midterm Theory](../assessments/midterm_theory.md) | Architecture and lifecycle questions |
| **Assessment** | [Pre-Course Assessment](../assessments/pre_course_assessment.py) | Baseline placement |

---

### CLO2 — Build Interactive Applications

> **"Students can build interactive data applications using Streamlit widgets, layouts, and state management."**

**Bloom's Level:** Apply

| Resource Type | Resource | Description |
|---|---|---|
| **Notebook** | [N01 — Your First Streamlit App](../notebooks/01_first_streamlit_app.ipynb) | Basic app creation |
| **Notebook** | [N02 — The Widget Zoo](../notebooks/02_widgets_and_input.ipynb) | Full widget library |
| **Notebook** | [N03 — Layout Mastery](../notebooks/03_layouts_and_containers.ipynb) | Complex layouts |
| **Notebook** | [N05 — Session State Deep Dive](../notebooks/05_session_state.ipynb) | Stateful apps |
| **Exercise** | [E01 — Hello Streamlit](../exercises/exercise_01_hello_streamlit.py) | Basic app |
| **Exercise** | [E02 — Widget Master](../exercises/exercise_02_widget_master.py) | Widget implementation |
| **Exercise** | [E03 — Layout Designer](../exercises/exercise_03_layout_designer.py) | Layout challenge |
| **Exercise** | [E05 — State Counter](../exercises/exercise_05_state_counter.py) | State management |
| **Quiz** | [Q03 — Layouts](../quizzes/quiz_03_layouts.md) | Layout API knowledge |
| **Assignment** | [Assignment 01 — Basic App](../assignments/assignment_01_basic_app/) | Graded app submission |
| **Project** | [P01 — Personal Dashboard](../projects/p01_personal_dashboard/) | Complete single-page app |
| **App Demo** | [hello.py](../apps/hello.py), [widgets_demo.py](../apps/widgets_demo.py), [layouts_demo.py](../apps/layouts_demo.py) | Reference implementations |

---

### CLO3 — Implement Data Visualization

> **"Students can implement data visualization strategies using Streamlit's native and third-party chart integrations."**

**Bloom's Level:** Apply

| Resource Type | Resource | Description |
|---|---|---|
| **Notebook** | [N04 — Data Visualization](../notebooks/04_data_visualization.ipynb) | All chart types and integrations |
| **Exercise** | [E04 — Chart Gallery](../exercises/exercise_04_chart_gallery.py) | Multi-chart implementation |
| **Quiz** | [Q04 — Visualization](../quizzes/quiz_04_visualization.md) | Chart selection and API |
| **Assignment** | [Assignment 02 — Data Dashboard](../assignments/assignment_02_data_dashboard/) | Interactive dashboard |
| **Project** | [P02 — Data Explorer](../projects/p02_data_explorer/) | Chart-driven data exploration |
| **App Demo** | [charts_demo.py](../apps/charts_demo.py) | All chart types demonstrated |

---

### CLO4 — Manage Application State

> **"Students can design and manage application state across reruns using session state, callbacks, and fragments."**

**Bloom's Level:** Apply, Analyze

| Resource Type | Resource | Description |
|---|---|---|
| **Reading** | [R04 — The Execution Model](../readings/r04_execution_model.md) | Why state is needed |
| **Reading** | [R06 — Session State Internals](../readings/r06_session_state_internals.md) | How state works |
| **Notebook** | [N05 — Session State Deep Dive](../notebooks/05_session_state.ipynb) | State patterns |
| **Notebook** | [N07 — Performance Engineering](../notebooks/07_caching_and_performance.ipynb) | Fragment-based partial reruns |
| **Exercise** | [E05 — State Counter](../exercises/exercise_05_state_counter.py) | State implementation |
| **Exercise** | [E07 — Cache Challenge](../exercises/exercise_07_cache_challenge.py) | Fragment patterns |
| **Quiz** | [Q05 — Session State](../quizzes/quiz_05_session_state.md) | State concepts |
| **Quiz** | [Q07 — Caching](../quizzes/quiz_07_caching.md) | Fragment and cache state |
| **Project** | [P04 — Real-Time Dashboard](../projects/p04_realtime_dashboard/) | Advanced state management |
| **App Demo** | [state_demo.py](../apps/state_demo.py), [caching_demo.py](../apps/caching_demo.py) | State demos |

---

### CLO5 — Optimize Performance

> **"Students can optimize Streamlit application performance through caching, fragments, and lazy loading."**

**Bloom's Level:** Analyze

| Resource Type | Resource | Description |
|---|---|---|
| **Reading** | [R05 — Caching Internals](../readings/r05_caching_internals.md) | Hash-based caching, TTL |
| **Notebook** | [N07 — Performance Engineering](../notebooks/07_caching_and_performance.ipynb) | Caching and fragments |
| **Notebook** | [N08 — Building Multipage Applications](../notebooks/08_multipage_apps.ipynb) | Navigation performance |
| **Exercise** | [E07 — Cache Challenge](../exercises/exercise_07_cache_challenge.py) | Caching implementation |
| **Quiz** | [Q07 — Caching](../quizzes/quiz_07_caching.md) | Cache strategy selection |
| **Assignment** | [Assignment 02 — Data Dashboard](../assignments/assignment_02_data_dashboard/) | Performance-optimized dashboard |
| **Project** | [P04 — Real-Time Dashboard](../projects/p04_realtime_dashboard/) | Caching + fragments |
| **App Demo** | [caching_demo.py](../apps/caching_demo.py) | Caching patterns |

---

### CLO6 — Design Well-Architected Applications

> **"Students can design well-structured Streamlit applications using proven architecture patterns."**

**Bloom's Level:** Apply, Analyze

| Resource Type | Resource | Description |
|---|---|---|
| **Reading** | [R07 — Architecture Patterns](../readings/r07_architecture_patterns.md) | MVC-like patterns, components |
| **Notebook** | [N09 — Architecting Streamlit Apps](../notebooks/09_architecture_patterns.ipynb) | Design patterns |
| **Notebook** | [N08 — Building Multipage Applications](../notebooks/08_multipage_apps.ipynb) | Multi-page structure |
| **Exercise** | [E08 — Multipage Navigator](../exercises/exercise_08_multipage_nav.py) | Navigation design |
| **Exercise** | [E09 — Architecture Review](../exercises/exercise_09_architecture_review.py) | Architecture analysis |
| **Quiz** | [Q08 — Multipage](../quizzes/quiz_08_multipage.md) | Navigation patterns |
| **Quiz** | [Q09 — Architecture](../quizzes/quiz_09_architecture.md) | Architecture concepts |
| **Assignment** | [Assignment 03 — Full Stack App](../assignments/assignment_03_full_stack_app/) | Full architecture exercise |
| **Project** | [P04 — Real-Time Dashboard](../projects/p04_realtime_dashboard/) | Architecture in practice |
| **App Demo** | [architecture_demo/](../apps/architecture_demo/), [multipage_demo/](../apps/multipage_demo/) | Pattern demos |

---

### CLO7 — Connect to Data Sources

> **"Students can connect Streamlit apps to databases and external APIs for persistent data and real-time information."**

**Bloom's Level:** Apply

| Resource Type | Resource | Description |
|---|---|---|
| **Reading** | [R08 — Database Design Basics](../readings/r08_database_design_basics.md) | Schema design, ORM vs raw SQL |
| **Reading** | [R09 — API Design Patterns](../readings/r09_api_design_patterns.md) | REST conventions, error handling |
| **Notebook** | [N10 — Database Connectivity](../notebooks/10_databases.ipynb) | SQL connections |
| **Notebook** | [N11 — API Integration](../notebooks/11_api_integration.ipynb) | REST APIs |
| **Exercise** | [E10 — Database CRUD](../exercises/exercise_10_database_crud.py) | CRUD operations |
| **Exercise** | [E11 — API Fetcher](../exercises/exercise_11_api_fetcher.py) | API consumption |
| **Quiz** | [Q10 — Databases](../quizzes/quiz_10_databases.md) | Database concepts |
| **Quiz** | [Q11 — APIs](../quizzes/quiz_11_apis.md) | API patterns |
| **Project** | [P05 — CRUD Database App](../projects/p05_crud_app/) | Full database application |
| **App Demo** | [db_demo.py](../apps/db_demo.py), [api_demo.py](../apps/api_demo.py) | Data integration demos |

---

### CLO8 — Deploy ML Models

> **"Students can deploy machine learning models as interactive Streamlit applications with explanations."**

**Bloom's Level:** Apply, Analyze

| Resource Type | Resource | Description |
|---|---|---|
| **Reading** | [R10 — ML Serving Patterns](../readings/r10_ml_serving_patterns.md) | Batch vs real-time, serialization |
| **Notebook** | [N12 — ML Dashboards](../notebooks/12_ml_dashboard.ipynb) | End-to-end ML deployment |
| **Exercise** | [E12 — ML Predictor](../exercises/exercise_12_ml_predictor.py) | Model deployment |
| **Quiz** | [Q12 — ML & AI](../quizzes/quiz_12_ml_ai.md) | ML concepts |
| **Assignment** | [Assignment 03 — Full Stack App](../assignments/assignment_03_full_stack_app/) | ML integration |
| **Project** | [P06 — ML Model Playground](../projects/p06_ml_playground/) | Interactive ML explorer |
| **App Demo** | [ml_demo.py](../apps/ml_demo.py) | ML deployment demo |

---

### CLO9 — Build AI-Powered Applications

> **"Students can build AI-powered applications including chat interfaces and RAG systems."**

**Bloom's Level:** Apply, Create

| Resource Type | Resource | Description |
|---|---|---|
| **Reading** | [R11 — RAG Concepts](../readings/r11_rag_concepts.md) | Embeddings, vector stores, chunking |
| **Notebook** | [N13 — Building AI-Powered Apps](../notebooks/13_ai_llm_apps.ipynb) | LLM + RAG integration |
| **Exercise** | [E13 — Chatbot Builder](../exercises/exercise_13_chatbot_builder.py) | Chat interface implementation |
| **Project** | [P07 — RAG Document Chat](../projects/p07_rag_chat/) | Document Q&A application |
| **App Demo** | [ai_chat_demo.py](../apps/ai_chat_demo.py) | Chat + RAG demo |

---

### CLO10 — Test and Secure Applications

> **"Students can apply testing, security best practices, and CI/CD to Streamlit applications."**

**Bloom's Level:** Evaluate

| Resource Type | Resource | Description |
|---|---|---|
| **Reading** | [R12 — Security Best Practices](../readings/r12_security_best_practices.md) | OWASP Top 10 for Streamlit |
| **Reading** | [R13 — Testing Strategies](../readings/r13_testing_strategies.md) | Unit vs integration vs e2e |
| **Notebook** | [N14 — Testing & Securing Apps](../notebooks/14_testing_security.ipynb) | AppTest + security |
| **Exercise** | [E14 — Test Suite](../exercises/exercise_14_test_suite.py) | Test implementation |
| **Assessment** | [Midterm Practical](../assessments/midterm_practical.py) | Testing and debugging |
| **Project** | [P08 — Capstone Project](../projects/p08_capstone/) | Full test suite required |
| **App Demo** | [test_demo.py](../apps/test_demo.py) | Testing patterns |

---

### CLO11 — Deploy to Production

> **"Students can deploy, monitor, and maintain Streamlit applications in production environments."**

**Bloom's Level:** Evaluate

| Resource Type | Resource | Description |
|---|---|---|
| **Reading** | [R14 — Deployment Options](../readings/r14_deployment_options.md) | Cloud, Docker, alternatives |
| **Reading** | [R15 — Production Checklist](../readings/r15_production_checklist.md) | Monitoring, logging, scaling |
| **Notebook** | [N15 — Deploy to the World](../notebooks/15_deployment_guide.ipynb) | Community Cloud deployment |
| **Notebook** | [N16 — Production Readiness](../notebooks/16_production_readiness.ipynb) | Monitoring and maintenance |
| **Exercise** | [E15 — Deploy Pipeline](../exercises/exercise_15_deploy_pipeline.py) | Deployment setup |
| **Exercise** | [E16 — Monitoring Setup](../exercises/exercise_16_monitoring.py) | Monitoring implementation |
| **Assignment** | [Assignment 04 — Production App](../assignments/assignment_04_production_app/) | Deployed application |
| **Project** | [P08 — Capstone Project](../projects/p08_capstone/) | Full deployment |
| **App Demo** | [deployed_app/](../apps/deployed_app/) | Deployment reference |

---

### CLO12 — Execute Full Development Lifecycle

> **"Students can execute a complete software development lifecycle for a data application, from requirements to deployment."**

**Bloom's Level:** Create (highest)

| Resource Type | Resource | Description |
|---|---|---|
| **All readings** | [R01–R15](roadmap.md#quick-links) | Full conceptual foundation |
| **All notebooks** | [N01–N16](roadmap.md#module--resource-matrix) | Complete skill progression |
| **All exercises** | [E01–E16](roadmap.md#module--resource-matrix) | Applied practice |
| **All quizzes** | [Q01–Q12](roadmap.md#module--resource-matrix) | Knowledge validation |
| **Assignments** | [A01–A04](roadmap.md#assessment-milestones) | Graded milestones |
| **Capstone Project** | [P08 — Capstone](../projects/p08_capstone/) | End-to-end lifecycle |
| **Assessment** | [Capstone Rubric](../assessments/rubrics/capstone_rubric.md) | Final evaluation |

The capstone integrates all prior CLOs:
- CLO1–C2: App fundamentals and interactivity
- CLO3: Visualization strategy
- CLO4–C5: State management and performance
- CLO6: Architecture decisions
- CLO7: Data source integration
- CLO8–C9: ML/AI components
- CLO10: Testing and security
- CLO11: Deployment and monitoring

---

## Assessment ↔ CLO Mapping

| Assessment | CLOs Assessed | Bloom's Level | Weight |
|---|---|---|---|
| [Pre-Course Assessment](../assessments/pre_course_assessment.py) | CLO1 | Remember, Understand | 5% |
| Weekly Quizzes (Q01–Q12) | CLO1–CLO8 | Remember, Understand | 10% |
| Exercises (E01–E16) | CLO1–CLO11 | Apply | 20% |
| Labs (in-class) | CLO2–CLO6 | Apply | 10% |
| [Assignment 01](../assignments/assignment_01_basic_app/) | CLO2, CLO6 | Apply | 15% (total) |
| [Assignment 02](../assignments/assignment_02_data_dashboard/) | CLO3, CLO4, CLO5 | Apply, Analyze | — |
| [Assignment 03](../assignments/assignment_03_full_stack_app/) | CLO6, CLO7, CLO8 | Apply, Analyze | — |
| [Assignment 04](../assignments/assignment_04_production_app/) | CLO10, CLO11 | Evaluate | — |
| [Midterm](../assessments/midterm_practical.py) | CLO1–CLO6 | Analyze, Evaluate | 10% |
| Projects (P01–P07) | CLO2–CLO9 | Apply, Analyze, Create | 15% |
| [Capstone (P08)](../projects/p08_capstone/) | CLO1–CLO12 | All levels | 15% |

---

## Bloom's Taxonomy Reference

| Level | Description | Course Context |
|---|---|---|
| **Remember** | Recall facts and basic concepts | API names, widget functions, terminology |
| **Understand** | Explain ideas or concepts | Explain execution model, describe when to use caching |
| **Apply** | Use information in new situations | Build apps, implement widgets, connect to APIs |
| **Analyze** | Draw connections among ideas | Compare caching strategies, choose architecture patterns |
| **Evaluate** | Justify a stand or decision | Review security posture, assess deployment options |
| **Create** | Produce new or original work | Design and build complete applications, capstone project |

---

## Content Quality Standards

Every learning outcome must be traceable through the full chain:

```
Topic → Reading → Notebook → Exercise → Quiz → Assessment → Project
  │         │          │          │         │          │           │
  │         │          │          │         │          │           └─ Real-world application
  │         │          │          │         │          └─ Formal evaluation
  │         │          │          │         └─ Knowledge check
  │         │          │          └─ Applied practice
  │         │          └─ Guided exploration
  │         └─ Conceptual foundation
  └─ Module topic definition
```

This document serves as the **accountability layer**: if any link in this chain is missing for a CLO, it must be flagged and filled before the course is delivered.

# P18 — Production-Style Data Science Dashboard

> **🚀 Project · Expert · M14–M16**
> *Build a production-quality dashboard with testing, security, monitoring, and deployment.*
> Difficulty: ★★★★★ · Duration: 3 weeks · Weight: Part of 15% project grade

---

## Problem Statement

A fintech startup needs a production-ready analytics dashboard for their operations team. The dashboard must be tested, secure, deployable, and maintainable — not just a prototype, but something that could actually run in production.

---

## Learning Objectives

1. Design a production-quality application architecture (CLO6)
2. Implement comprehensive testing (CLO10)
3. Apply security best practices (CLO10)
4. Deploy and monitor a production application (CLO11)
5. Execute a complete development lifecycle (CLO12)

---

## Prerequisites

- Completed all modules (M01–M16)
- All assignments submitted
- Understanding of testing, security, deployment

---

## Functional Requirements

| # | Requirement | Marks |
|---|-------------|-------|
| F1 | Modular architecture: separate data, UI, logic, config | 8 |
| F2 | Database integration (SQLite) with CRUD operations | 8 |
| F3 | Multipage navigation with `st.navigation()` | 6 |
| F4 | Interactive filters with session state | 6 |
| F5 | KPI metrics and 4+ chart types | 8 |
| F6 | Caching with proper invalidation | 6 |
| F7 | Input validation and error handling | 6 |
| F8 | Unit tests (≥3) passing with pytest | 8 |
| F9 | AppTest (≥2) for Streamlit testing | 6 |
| F10 | Security: no hardcoded secrets, parameterized SQL, .gitignore | 6 |
| F11 | Deployed on Community Cloud, accessible via URL | 8 |
| F12 | README with architecture diagram, setup, screenshots | 6 |

**Total: 82 marks**

---

## Non-Functional Requirements

| Category | Requirement |
|----------|-------------|
| Performance | App loads in <15 seconds, interactions <3 seconds |
| Security | No hardcoded secrets, input validation, safe SQL |
| Testing | All tests pass, ≥80% coverage of data functions |
| Deployment | Live on Community Cloud, no errors |
| Documentation | Complete README, code comments, docstrings |
| Maintainability | Clear naming, separation of concerns, no magic numbers |

---

## Architecture

```
production_dashboard/
├── app.py                    # Entry point
├── config.py                 # Configuration
├── data_access.py            # Database operations
├── data_processing.py        # Data transformation
├── components.py             # Reusable UI components
├── pages/
│   ├── __init__.py
│   ├── home.py
│   ├── explore.py
│   ├── manage.py
│   └── reports.py
├── tests/
│   ├── __init__.py
│   ├── test_data_access.py
│   ├── test_processing.py
│   └── test_app.py
├── requirements.txt
├── .gitignore
├── README.md
└── screenshots/
```

---

## Milestones

| Week | Milestone | Deliverable |
|------|-----------|-------------|
| 1 | Architecture + core data layer | File structure, database, data functions |
| 2 | UI + features + testing | All pages, tests passing, security |
| 3 | Deployment + documentation | Deployed app, README, screenshots |

---

## Evaluation Criteria

| Criteria | Marks |
|----------|-------|
| Architecture and code quality | 20 |
| Functionality | 20 |
| Testing | 14 |
| Security | 12 |
| Deployment | 8 |
| Documentation | 8 |
| **Total** | **82** |

---

## Extensions

- Add logging with Python `logging` module
- Add rate limiting on inputs
- Add performance monitoring (cache hit rates)
- Add CI/CD with GitHub Actions

---

## Related Materials

- 📖 Reading: [Architecture](../readings/13_application_architecture.md)
- 📖 Reading: [Security](../readings/security_and_secrets.md)
- 📖 Reading: [Deployment](../readings/deployment_guide.md)
- 📋 Checklist: [Deployment Checklist](../docs/deployment_checklist.md)
- ✏️ Exercise: [16 — Production](../exercises/16_production_ready.py)

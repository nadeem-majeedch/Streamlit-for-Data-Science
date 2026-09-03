# Capstone Submission Checklist

> **✅ Student Checklist — Complete Before Submitting**
> *Use this checklist to ensure nothing is missed before final submission.*

---

## How to Use This Checklist

1. Print or open this file alongside your project
2. Check off each item as you complete it
3. **All items must be checked** before submission
4. Items marked with ⚠️ will cause mark deductions if incomplete
5. Items marked with 🚨 will cause automatic failure if missing

---

## Phase 1: Problem & Data (Week 13)

- [ ] ⚠️ Problem statement written (2–3 paragraphs)
- [ ] ⚠️ Target users identified
- [ ] ⚠️ Value proposition explained
- [ ] ⚠️ Dataset obtained and in `data/` directory
- [ ] ⚠️ Data source documented (origin, license)
- [ ] ⚠️ Data dictionary created (column descriptions)
- [ ] Data is appropriate size (≥100 rows for ML)
- [ ] No PII in dataset without consent

---

## Phase 2: Architecture & Design (Week 13)

- [ ] ⚠️ Project structure created (see `final_capstone.md` Section 5)
- [ ] ⚠️ `config.py` with constants
- [ ] ⚠️ `data_loader.py` with loading functions
- [ ] ⚠️ `data_processing.py` with transformation functions
- [ ] ⚠️ `components.py` with reusable UI components
- [ ] ⚠️ `pages/` directory with page modules
- [ ] UI wireframe/sketch created
- [ ] Architecture diagram drawn (even text-based)

---

## Phase 3: Core Development (Week 14)

- [ ] ⚠️ Data loading works (`data_loader.py`)
- [ ] ⚠️ Sidebar filters implemented and working
- [ ] ⚠️ KPI metrics displayed (4+ metrics)
- [ ] ⚠️ At least 4 chart types implemented
- [ ] ⚠️ Charts update when filters change
- [ ] ⚠️ Data table displays with formatting
- [ ] All visualizations have titles and labels
- [ ] `st.set_page_config()` is first Streamlit call

---

## Phase 4: ML/AI Component (Week 14–15)

- [ ] ⚠️ ML/AI component implemented
- [ ] ⚠️ Model trained or loaded correctly
- [ ] ⚠️ Model saved with `joblib` (if trained)
- [ ] ⚠️ Model loaded with `@st.cache_resource`
- [ ] ⚠️ Preprocessing consistent (transform, not fit_transform)
- [ ] ⚠️ Prediction interface with input widgets
- [ ] ⚠️ Prediction result displayed with confidence
- [ ] ⚠️ Input validation on prediction inputs
- [ ] ⚠️ Batch prediction works (if applicable)
- [ ] Model info panel displayed
- [ ] Feature importance shown (if applicable)

---

## Phase 5: State & Performance (Week 15)

- [ ] ⚠️ All stateful values in `st.session_state`
- [ ] ⚠️ No state bugs (variables resetting on rerun)
- [ ] ⚠️ `@st.cache_data` on expensive computations
- [ ] ⚠️ `@st.cache_resource` on model/DB connections
- [ ] ⚠️ Cache invalidation after writes (if applicable)
- [ ] App loads within 15 seconds
- [ ] Interactions respond within 3 seconds
- [ ] No unnecessary rerun computations

---

## Phase 6: Testing (Week 15)

- [ ] ⚠️ Unit tests in `tests/test_data.py` (≥3 tests)
- [ ] ⚠️ Unit tests in `tests/test_model.py` (if applicable)
- [ ] ⚠️ AppTest in `tests/test_app.py` (≥2 tests)
- [ ] ⚠️ All tests pass: `pytest tests/ -v`
- [ ] Tests cover edge cases (empty data, invalid input)
- [ ] No test warnings

---

## Phase 7: Security (Week 15)

- [ ] 🚨 **NO hardcoded secrets** in any source file
- [ ] ⚠️ `.gitignore` includes `.streamlit/secrets.toml`
- [ ] ⚠️ `.gitignore` includes `__pycache__/`
- [ ] ⚠️ `.gitignore` includes `models/*.joblib`
- [ ] ⚠️ `.gitignore` includes `data/*.csv` (if large)
- [ ] ⚠️ All user inputs validated
- [ ] ⚠️ No `exec()` or `eval()` calls
- [ ] No f-string SQL queries (parameterized only)
- [ ] File upload validation (type, size)

---

## Phase 8: Deployment (Week 15)

- [ ] 🚨 **App deployed on Community Cloud**
- [ ] 🚨 **Deployment URL accessible**
- [ ] ⚠️ `requirements.txt` at repository root
- [ ] ⚠️ `requirements.txt` includes all imports
- [ ] ⚠️ `requirements.txt` has no development-only packages
- [ ] ⚠️ Entry point file correct in Community Cloud settings
- [ ] ⚠️ All features work in deployed version
- [ ] ⚠️ No hardcoded file paths in code
- [ ] App handles cold start gracefully
- [ ] Secrets configured in Community Cloud settings (if needed)

---

## Phase 9: Documentation (Week 16)

- [ ] ⚠️ `README.md` includes: title and description
- [ ] ⚠️ `README.md` includes: features list
- [ ] ⚠️ `README.md` includes: setup instructions
- [ ] ⚠️ `README.md` includes: deployment URL
- [ ] ⚠️ `README.md` includes: data sources
- [ ] ⚠️ `README.md` includes: limitations
- [ ] ⚠️ `README.md` includes: screenshots (4+)
- [ ] ⚠️ Screenshots in `screenshots/` directory
- [ ] ⚠️ Code has docstrings on functions
- [ ] ⚠️ Code has comments on complex logic
- [ ] Code has type hints (recommended)
- [ ] AI assistance declared in README (if used)

---

## Phase 10: Final Checks (Week 16, before submit)

- [ ] ⚠️ App runs from fresh clone: `git clone ... && pip install -r requirements.txt && streamlit run app.py`
- [ ] ⚠️ All tests pass from fresh clone
- [ ] ⚠️ No `__pycache__/` in repository
- [ ] ⚠️ No `.venv/` in repository
- [ ] ⚠️ No large data files in repository (>10MB)
- [ ] ⚠️ No secrets in git history
- [ ] ⚠️ Git history is clean (meaningful commits)
- [ ] ⚠️ Deployment URL is correct in README
- [ ] ⚠️ All files in submission are intentional
- [ ] Presentation ready (slides, demo)

---

## Phase 11: Submission

### Repository
- [ ] 🚨 Repository is pushed to GitHub
- [ ] 🚨 Repository is accessible (public or shared)
- [ ] All files committed and pushed

### Links to Submit
1. [ ] 🚨 **GitHub Repository URL:** _______________
2. [ ] 🚨 **Community Cloud Deployment URL:** _______________
3. [ ] **Presentation slides URL** (if applicable): _______________

### Presentation
- [ ] ⚠️ 10-minute presentation prepared
- [ ] ⚠️ Live demo tested and ready
- [ ] ⚠️ Prepared to answer technical questions
- [ ] ⚠️ Architecture explanation ready
- [ ] ⚠️ Challenges and solutions prepared

---

## Quick Verification Commands

```bash
# Run all tests
pytest tests/ -v

# Check for secrets in code
grep -rn "sk-\|api_key\|password\|secret" --include="*.py" .

# Check for hardcoded paths
grep -rn "/Users/\|/home/\|C:\\" --include="*.py" .

# Verify requirements.txt
pip install -r requirements.txt

# Run the app locally
streamlit run app.py

# Check git status
git status
git log --oneline -10
```

---

## Emergency: Last-Minute Fixes

If you're running out of time, prioritize in this order:

| Priority | Item | Impact |
|----------|------|--------|
| 1 | 🚨 Deployment works | 15 marks |
| 2 | 🚨 No hardcoded secrets | 10 marks |
| 3 | 🚨 App runs without crashes | 30 marks |
| 4 | ⚠️ Tests pass | 15 marks |
| 5 | ⚠️ README complete | 15 marks |
| 6 | ⚠️ Screenshots taken | 4 marks |
| 7 | Nice-to-have polish | Up to 15 marks |

---

## Related Materials

- 📋 Capstone Spec: [final_capstone.md](final_capstone.md)
- 📋 Grading Rubric: [capstone_rubric.md](capstone_rubric.md)
- 🎤 Presentation Guide: [capstone_presentation.md](capstone_presentation.md)
- 📋 Deployment Checklist: [../docs/deployment_checklist.md](../docs/deployment_checklist.md)

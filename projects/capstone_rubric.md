# Capstone Grading Rubric

> **👩‍🏫 Instructor Reference — Detailed Grading Rubric**
> *Point-by-point breakdown for consistent, fair assessment.*
> ⚠️ **Do not distribute to students**

---

## Rubric Overview

| Section | Marks | Weight | Bloom's |
|---------|-------|--------|---------|
| 1. Problem & Data | 20 | 10% | Understand, Apply |
| 2. Architecture & Design | 25 | 12.5% | Analyze |
| 3. Application Functionality | 30 | 15% | Apply |
| 4. Visualization | 20 | 10% | Apply |
| 5. ML/AI Component | 25 | 12.5% | Apply, Analyze |
| 6. State & Performance | 15 | 7.5% | Analyze |
| 7. Testing | 15 | 7.5% | Evaluate |
| 8. Security | 10 | 5% | Evaluate |
| 9. Deployment | 15 | 7.5% | Evaluate |
| 10. Documentation | 15 | 7.5% | Create |
| 11. Presentation | 30 | 15% | Evaluate, Create |
| 12. Innovation & Polish | 15 | 7.5% | Create |
| **Total** | **235** | | (capped at 200 + 15 bonus) |

---

## Section 1: Problem & Data (20 marks)

### 1.1 Problem Definition (8 marks)

| Marks | Criteria |
|-------|----------|
| 8 | Problem is real, well-defined, and clearly articulated. Target users identified. Value proposition compelling. |
| 6 | Problem is real but definition is vague. Users or value unclear. |
| 4 | Problem is contrived or too simple. Limited justification. |
| 2 | Problem statement missing or unclear. |
| 0 | No problem definition provided. |

### 1.2 Dataset Quality (8 marks)

| Marks | Criteria |
|-------|----------|
| 8 | Dataset is appropriate, well-documented, has sufficient volume and variety. Data dictionary complete. |
| 6 | Dataset is appropriate but documentation incomplete. |
| 4 | Dataset exists but is too small or inappropriate for the problem. |
| 2 | Dataset minimal or poorly documented. |
| 0 | No dataset provided. |

### 1.3 Data Processing (4 marks)

| Marks | Criteria |
|-------|----------|
| 4 | Processing functions are clean, documented, handle edge cases. Reusable. |
| 3 | Processing works but has some issues (no error handling, not reusable). |
| 2 | Basic processing, inline code. |
| 1 | Minimal processing. |
| 0 | No processing evident. |

---

## Section 2: Architecture & Design (25 marks)

### 2.1 File Structure (8 marks)

| Marks | Criteria |
|-------|----------|
| 8 | Clean modular structure: separate data, UI, logic, config. All files serve a clear purpose. |
| 6 | Mostly modular with minor mixing of concerns. |
| 4 | Some separation but significant mixing (e.g., DB queries in UI). |
| 2 | Mostly one file with minor extraction. |
| 0 | All code in a single file. |

### 2.2 Code Quality (10 marks)

| Marks | Criteria |
|-------|----------|
| 10 | PEP 8 compliant, docstrings on all functions, type hints, no magic numbers, consistent naming. |
| 8 | Mostly clean, some docstrings, minor style issues. |
| 6 | Readable but inconsistent style, few docstrings. |
| 4 | Functional but hard to read, no documentation. |
| 2 | Poor code quality, difficult to understand. |
| 0 | Code is non-functional or unreadable. |

### 2.3 Design Decisions (7 marks)

| Marks | Criteria |
|-------|----------|
| 7 | Architecture choices are justified and appropriate. Trade-offs understood. |
| 5 | Choices are reasonable but not clearly justified. |
| 3 | Some design issues but functional. |
| 1 | Poor design choices that impact functionality. |
| 0 | No coherent design. |

---

## Section 3: Application Functionality (30 marks)

### 3.1 Data Loading & Display (8 marks)

| Marks | Criteria |
|-------|----------|
| 8 | Data loads from appropriate source, displays correctly, handles errors. File upload works. |
| 6 | Data loads and displays, minor issues with error handling. |
| 4 | Data loads but display has issues. |
| 2 | Data loading partially works. |
| 0 | Data does not load. |

### 3.2 Interactive Controls (10 marks)

| Marks | Criteria |
|-------|----------|
| 10 | Sidebar filters comprehensive, update all views, clear labels, sensible defaults. |
| 8 | Filters work, update most views, minor UX issues. |
| 6 | Basic filtering works but doesn't update all views. |
| 4 | Filters exist but don't work correctly. |
| 2 | Minimal filtering. |
| 0 | No interactive controls. |

### 3.3 KPIs & Metrics (6 marks)

| Marks | Criteria |
|-------|----------|
| 6 | 4+ relevant KPIs, properly formatted, update with filters. |
| 4 | 2-3 KPIs, mostly formatted. |
| 2 | 1 KPI or poorly formatted. |
| 0 | No KPIs. |

### 3.4 Error Handling (6 marks)

| Marks | Criteria |
|-------|----------|
| 6 | Graceful failure for all edge cases: empty data, invalid input, missing files, API errors. |
| 4 | Handles common errors, misses edge cases. |
| 2 | Basic error handling, some crashes possible. |
| 0 | App crashes on invalid input. |

---

## Section 4: Visualization (20 marks)

### 4.1 Chart Variety (8 marks)

| Marks | Criteria |
|-------|----------|
| 8 | 4+ different chart types, each appropriate for the data. |
| 6 | 3 chart types, mostly appropriate. |
| 4 | 2 chart types. |
| 2 | 1 chart type. |
| 0 | No charts. |

### 4.2 Chart Quality (7 marks)

| Marks | Criteria |
|-------|----------|
| 7 | Clear titles, labels, legends. Colors appropriate. Interactive (Plotly). |
| 5 | Most charts clear, some missing labels. |
| 3 | Charts render but lack labels or are hard to read. |
| 1 | Charts exist but are unclear. |
| 0 | No meaningful visualizations. |

### 4.3 Chart Interactivity (5 marks)

| Marks | Criteria |
|-------|----------|
| 5 | Charts update dynamically with all filter changes. Responsive. |
| 3 | Some charts update, others static. |
| 1 | Charts don't respond to filters. |
| 0 | No interactivity. |

---

## Section 5: ML/AI Component (25 marks)

### 5.1 Model Implementation (10 marks)

| Marks | Criteria |
|-------|----------|
| 10 | Model trained/loaded correctly, saved with joblib, loaded with caching. Preprocessing consistent. |
| 8 | Model works, minor issues with caching or preprocessing. |
| 6 | Model works but not properly cached or saved. |
| 4 | Model partially works. |
| 2 | Model exists but doesn't work correctly. |
| 0 | No ML/AI component. |

### 5.2 Prediction Interface (8 marks)

| Marks | Criteria |
|-------|----------|
| 8 | Input UI with validation, prediction with confidence, edge cases handled. |
| 6 | Input UI works, prediction displayed, some validation. |
| 4 | Basic prediction interface. |
| 2 | Prediction works but no UI polish. |
| 0 | No prediction interface. |

### 5.3 Model Explanation (7 marks)

| Marks | Criteria |
|-------|----------|
| 7 | Feature importance, probability distribution, model info panel. |
| 5 | Some explanation (e.g., feature importance only). |
| 3 | Model info displayed but no explanation. |
| 1 | Minimal model information. |
| 0 | No model explanation. |

---

## Section 6: State & Performance (15 marks)

### 6.1 Session State (8 marks)

| Marks | Criteria |
|-------|----------|
| 8 | All stateful values in session_state. No state bugs. Initialization correct. |
| 6 | Most state handled correctly, minor issues. |
| 4 | Some session state usage, some state bugs. |
| 2 | Minimal state management. |
| 0 | No session state or persistent bugs. |

### 6.2 Caching & Performance (7 marks)

| Marks | Criteria |
|-------|----------|
| 7 | Appropriate caching on all expensive operations. App loads <15s, interactions <3s. |
| 5 | Caching present, performance acceptable. |
| 3 | Some caching, performance has issues. |
| 1 | No caching, slow performance. |
| 0 | App is unusably slow. |

---

## Section 7: Testing (15 marks)

### 7.1 Unit Tests (5 marks)

| Marks | Criteria |
|-------|----------|
| 5 | 3+ unit tests for data/logic functions. Tests are meaningful (not trivial). |
| 3 | 1-2 unit tests. |
| 1 | Tests exist but are trivial. |
| 0 | No unit tests. |

### 7.2 AppTest (5 marks)

| Marks | Criteria |
|-------|----------|
| 5 | 2+ `st.testing.AppTest` tests covering load, interaction, prediction. |
| 3 | 1 AppTest test. |
| 1 | AppTest exists but minimal. |
| 0 | No AppTest. |

### 7.3 Test Results (5 marks)

| Marks | Criteria |
|-------|----------|
| 5 | All tests pass cleanly. No warnings. |
| 3 | Tests pass with warnings. |
| 1 | Some tests fail. |
| 0 | Tests not runnable or most fail. |

---

## Section 8: Security (10 marks)

### 8.1 Secrets Management (5 marks)

| Marks | Criteria |
|-------|----------|
| 5 | No hardcoded secrets. `.gitignore` includes secrets. Secrets accessed via `st.secrets`. |
| 3 | Minor issue (e.g., .gitignore incomplete). |
| 1 | Secret found in source code but not critical. |
| 0 | API keys or passwords in source code. |

### 8.2 Input Validation (5 marks)

| Marks | Criteria |
|-------|----------|
| 5 | All user inputs validated. No injection risks. File uploads validated. |
| 3 | Most inputs validated. |
| 1 | Some validation present. |
| 0 | No input validation. |

---

## Section 9: Deployment (15 marks)

### 9.1 Deployment Success (8 marks)

| Marks | Criteria |
|-------|----------|
| 8 | Deployed on Community Cloud. URL accessible. All features work. |
| 6 | Deployed, most features work. |
| 4 | Deployed but significant issues. |
| 2 | Deployment attempted but fails. |
| 0 | Not deployed. |

### 9.2 Deployment Quality (7 marks)

| Marks | Criteria |
|-------|----------|
| 7 | `requirements.txt` correct. App loads <15s. No hardcoded paths. Clean deployment. |
| 5 | Requirements correct, minor deployment issues. |
| 3 | Requirements present but deployment has problems. |
| 1 | Minimal deployment preparation. |
| 0 | No deployment preparation. |

---

## Section 10: Documentation (15 marks)

### 10.1 README Quality (8 marks)

| Marks | Criteria |
|-------|----------|
| 8 | Complete: title, description, features, setup, deployment link, data sources, limitations, screenshots. |
| 6 | Mostly complete, missing 1-2 sections. |
| 4 | Basic README with some information. |
| 2 | Minimal README. |
| 0 | No README. |

### 10.2 Screenshots (4 marks)

| Marks | Criteria |
|-------|----------|
| 4 | 4+ clear screenshots showing different views/features. |
| 3 | 2-3 screenshots. |
| 1 | 1 screenshot. |
| 0 | No screenshots. |

### 10.3 Code Documentation (3 marks)

| Marks | Criteria |
|-------|----------|
| 3 | Docstrings on all functions. Comments on complex logic. Type hints. |
| 2 | Some docstrings present. |
| 1 | Minimal documentation. |
| 0 | No code documentation. |

---

## Section 11: Presentation (30 marks)

### 11.1 Live Demonstration (15 marks)

| Marks | Criteria |
|-------|----------|
| 15 | Smooth demo of all major features. Handles demo gracefully (no crashes). Engaging. |
| 12 | Demo covers most features, minor hiccup. |
| 9 | Demo covers basic features. |
| 5 | Demo incomplete or has major issues. |
| 0 | No demo or demo fails. |

### 11.2 Technical Explanation (10 marks)

| Marks | Criteria |
|-------|----------|
| 10 | Clear explanation of architecture, design decisions, and trade-offs. Demonstrates understanding. |
| 8 | Good explanation, some gaps. |
| 6 | Basic explanation. |
| 3 | Minimal technical depth. |
| 0 | Cannot explain own code. |

### 11.3 Q&A Response (5 marks)

| Marks | Criteria |
|-------|----------|
| 5 | Answers all questions accurately and thoughtfully. |
| 3 | Answers most questions. |
| 1 | Struggles with questions. |
| 0 | Cannot answer questions. |

---

## Section 12: Innovation & Polish (15 marks)

### 12.1 Creative Features (5 marks)

| Marks | Criteria |
|-------|----------|
| 5 | At least 2 features not taught in class. Demonstrates initiative. |
| 3 | 1 feature not taught in class. |
| 1 | Minimal innovation. |
| 0 | Only course-taught features. |

### 12.2 UX Design (5 marks)

| Marks | Criteria |
|-------|----------|
| 5 | Professional appearance. Intuitive navigation. Consistent styling. Clear labels. |
| 3 | Good appearance, minor UX issues. |
| 1 | Basic appearance. |
| 0 | Poor or no attention to UX. |

### 12.3 Responsiveness & Accessibility (5 marks)

| Marks | Criteria |
|-------|----------|
| 5 | Works on different screen sizes. Good contrast. Meaningful labels. |
| 3 | Mostly responsive. |
| 1 | Desktop-only, no accessibility consideration. |
| 0 | No attention to responsiveness. |

---

## Grade Calculation

| Component | Raw Marks | Weight | Weighted |
|-----------|-----------|--------|----------|
| Section 1: Problem & Data | /20 | 10% | |
| Section 2: Architecture | /25 | 12.5% | |
| Section 3: Functionality | /30 | 15% | |
| Section 4: Visualization | /20 | 10% | |
| Section 5: ML/AI | /25 | 12.5% | |
| Section 6: State & Performance | /15 | 7.5% | |
| Section 7: Testing | /15 | 7.5% | |
| Section 8: Security | /10 | 5% | |
| Section 9: Deployment | /15 | 7.5% | |
| Section 10: Documentation | /15 | 7.5% | |
| Section 11: Presentation | /30 | 15% | |
| Section 12: Innovation | /15 | 7.5% | |
| **Subtotal** | **/235** | | |
| **Bonus** | /15 | | |
| **Final** | | | **capped at 200 + 15** |

---

## CLO Alignment

| CLO | Sections |
|-----|----------|
| CLO1 | 11.2, 11.3 |
| CLO2 | 3.1, 3.2, 3.3 |
| CLO3 | 4.1, 4.2, 4.3 |
| CLO4 | 6.1 |
| CLO5 | 6.2 |
| CLO6 | 2.1, 2.3 |
| CLO7 | 1.2, 3.1 |
| CLO8 | 5.1, 5.2, 5.3 |
| CLO9 | 5.1 (if AI/LLM chosen) |
| CLO10 | 7.1, 7.2, 7.3, 8.1, 8.2 |
| CLO11 | 9.1, 9.2 |
| CLO12 | 1.1, 2.3, 10.1 |

---

## Common Grading Issues

### When to Deduct vs. Not
- **Deduct for missing features** — If requirement not met
- **Don't deduct for style** — Unless it impedes readability
- **Deduct for crashes** — App must not crash on valid input
- **Don't deduct for domain choice** — Any domain is fine
- **Deduct for no deployment** — This is a core requirement
- **Deduct for no tests** — Testing is required, not optional

### Edge Cases
- **Pair projects:** Both students must contribute. Grade individually based on contribution evidence.
- **AI assistance:** Allowed but must be declared. Grade on understanding, not just output.
- **Extensions:** Bonus marks capped at 15 to prevent grade inflation.

---

## Related Materials

- 📋 Capstone Spec: [final_capstone.md](final_capstone.md)
- ✅ Submission Checklist: [capstone_submission_checklist.md](capstone_submission_checklist.md)
- 🎤 Presentation Guide: [capstone_presentation.md](capstone_presentation.md)

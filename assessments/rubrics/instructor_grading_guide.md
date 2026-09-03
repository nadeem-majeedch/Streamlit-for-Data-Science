# Instructor Grading Guide

> **👩‍🏫 Instructor Reference — Assessment Grading Guide**
> *Rubrics, common issues, and grading notes for all course assessments.*
> ⚠️ **Do not distribute to students**

---

## Assessment Overview

| Assessment | Week | Weight | Duration | Type | Bloom's |
|------------|------|--------|----------|------|---------|
| Pre-course assessment | 0 | 0% (placement) | 30 min | Individual | L1–L3 |
| Lab 1 | 3 | 3.3% | 50 min | Individual, supervised | L1–L3 |
| Lab 2 | 8 | 3.3% | 50 min | Individual, supervised | L2–L4 |
| Mid-Course Assessment | 9 | 10% | 2 hours | Individual, closed-book | L1–L5 |
| Lab 3 | 13 | 3.3% | 50 min | Individual, supervised | L3–L5 |
| Practical Exam | 12 | 10% | 3 hours | Individual, timed | L2–L5 |
| Final Practical | 15 | 15% | 4 hours | Individual, deployed | L2–L6 |
| Capstone Project | 16 | 15% | 3 weeks | Individual/Pair | L1–L6 |
| Post-course assessment | 16 | 0% (reflection) | 30 min | Individual | L2–L5 |

---

## Grade Distribution Summary

| Component | Weight | Count |
|-----------|--------|-------|
| Weekly Quizzes | 10% | 16 |
| Exercises | 20% | 20 |
| Lab Assessments | 10% | 3 |
| Assignments | 15% | 4 |
| Mid-Course Assessment | 10% | 1 |
| Practical Exam | 10% | 1 |
| Final Practical | 15% | 1 |
| Capstone Project | 15% | 1 |
| **Total** | **105%** | (5% buffer for participation) |

---

## Mid-Course Assessment Grading Notes

### Part A: Conceptual (20 marks)

**Common issues:**
- Students confuse reruns with event-driven models
- Many forget that session_state is per-session
- Cache_data vs cache_resource confusion is common

**Grading approach:**
- Award partial credit for partial understanding
- Accept equivalent explanations (not just textbook definitions)
- Check for technical vocabulary usage

### Part B: Coding (40 marks)

**Task B1 (Widget & Layout):**
- Check for `st.set_page_config()` as first call (deduct 2 if missing)
- Verify all sidebar widgets work
- Metrics must update with filters
- Download button must work

**Task B2 (Session State):**
- Check for proper initialization pattern
- Verify step navigation works
- Form data persists between steps
- Submit resets form correctly

**Task B3 (Visualization):**
- Charts must update with filter changes
- Tab structure must be correct
- At least one Plotly chart required

### Part C: Debugging (20 marks)

**Q C1 (State Bug):**
Expected answer: Local variable resets on rerun. Fix: use session_state.
Deduct 2 if student identifies the problem but gives wrong fix.

**Q C2 (Cache Bug):**
Expected answer: Cache not invalidated after write. Fix: call `.clear()`.
Deduct 2 if student adds unnecessary complexity.

**Q C3 (Layout Bug):**
Expected answer: Wrong call order + incorrect columns usage.
Deduct 1 per issue found.

**Q C4 (Form Bug):**
Expected answer: Form widgets don't trigger reruns. Form submit must be checked.
Deduct 2 if student doesn't understand form behavior.

### Part D: Design (20 marks)

**D1 (Architecture):**
- File structure must show separation of concerns
- Function signatures must be correct
- Caching strategy must be justified
- Error handling must be realistic

**D2 (Performance):**
- Must identify all 4 issues
- Caching solutions must use correct decorators
- Additional optimization must be relevant

---

## Practical Exam Grading Notes

### Common Issues

1. **Model training on every rerun** — Deduct 5 marks from Task 3
2. **fit_transform at inference** — Deduct 3 marks from Task 3
3. **No error handling** — Deduct 2 marks from each task
4. **All code in one file** — Deduct 5 marks from Task 6
5. **Missing requirements.txt** — Deduct 3 marks from Task 6

### Time Management Advice for Students
- Spend 30 min on Tasks 1-2 (data + viz)
- Spend 60 min on Task 3 (ML — most marks)
- Spend 30 min on Tasks 4-5 (batch + state)
- Spend 30 min on Tasks 6-7 (architecture + docs)
- Keep 30 min buffer for testing and fixing

### Submission Checklist
- [ ] `app.py` runs without errors
- [ ] `requirements.txt` present
- [ ] Model files saved in `models/`
- [ ] README with screenshot
- [ ] No hardcoded secrets

---

## Final Practical Grading Notes

### Key Differentiators (A vs B)

| Criteria | A Grade | B Grade |
|----------|---------|---------|
| Architecture | Clean modular structure, config | Some separation, some mixing |
| ML | Proper caching, preprocessing | Basic ML, minor issues |
| Testing | Tests pass, good coverage | Some tests, basic coverage |
| Deployment | Deployed, no errors | Deployed, minor issues |
| Documentation | Complete, screenshots, architecture | Basic README |

### Common Issues

1. **Spending too long on ML, not enough on deployment** — Advise time-boxing
2. **No tests** — 15 marks lost immediately
3. **Not deploying** — 20 marks lost immediately
4. **Charts don't update with filters** — Check this during live demo
5. **Missing requirements.txt** — Deployment fails

---

## Capstone Project Grading Notes

### Presentation Assessment

**Live Demo (25 marks):**
- Must demonstrate ALL major features
- Must explain architecture clearly
- Must answer technical questions
- Deduct 5 for not showing deployment

**Reflection (15 marks):**
- Must be honest about challenges
- Must show technical understanding
- Must propose realistic improvements

### Project Quality Indicators

**A-level projects:**
- Clean, modular architecture
- Proper caching and state management
- All tests passing
- Deployed and working
- Creative feature beyond requirements
- Professional documentation

**C-level projects:**
- Single-file app
- Basic functionality only
- No tests or broken tests
- Deployment issues
- Minimal documentation

---

## Academic Integrity Incidents

### Red Flags
1. Code is significantly more advanced than student's demonstrated skill
2. Inconsistent coding style between different sections
3. Student cannot explain their own code during presentation
4. Two submissions have identical structure with minor changes
5. Code contains patterns not taught in the course

### Response Protocol
1. Schedule a 10-minute code review interview
2. Ask student to explain specific code sections
3. If explanation is inadequate, flag for further review
4. Document all incidents for course records

---

## CLO Assessment Matrix

| CLO | Pre | Labs | Mid | Practical | Final | Capstone |
|-----|-----|------|-----|-----------|-------|----------|
| CLO1 | ✓ | | ✓ | | | ✓ |
| CLO2 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| CLO3 | | ✓ | ✓ | ✓ | ✓ | ✓ |
| CLO4 | | ✓ | ✓ | ✓ | ✓ | ✓ |
| CLO5 | | | ✓ | ✓ | ✓ | ✓ |
| CLO6 | | | ✓ | | ✓ | ✓ |
| CLO7 | | ✓ | | | ✓ | ✓ |
| CLO8 | | ✓ | | ✓ | ✓ | ✓ |
| CLO9 | | | | | | ✓ |
| CLO10 | | | | | ✓ | ✓ |
| CLO11 | | | | | ✓ | ✓ |
| CLO12 | | | | | ✓ | ✓ |

---

## Related Materials

- 📋 Learning Outcomes: [../../docs/learning_outcomes.md](../../docs/learning_outcomes.md)
- 📋 Curriculum: [../../docs/curriculum.md](../../docs/curriculum.md)
- 📋 Course Blueprint: [../../docs/course_blueprint.md](../../docs/course_blueprint.md)

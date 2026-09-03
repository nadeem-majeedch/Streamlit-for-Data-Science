# ✅ Release Checklist

> **Streamlit for Data Science — Learn, Build, Deploy**
> *Pre-release verification checklist.*

---

## Pre-Release Checks

### Content
- [ ] All 16 modules have readings, notebooks, exercises, quizzes
- [ ] All 12 CLOs mapped through TAUGHT→PRACTICED→ASSESSED→APPLIED
- [ ] Progressive difficulty verified (★☆☆☆☆ → ★★★★★)
- [ ] No deprecated Streamlit APIs used
- [ ] All code examples are current (Streamlit 1.62+)

### Code Quality
- [ ] All 54 Python files pass syntax check
- [ ] All 19 notebooks are valid JSON
- [ ] All imports reference installed packages
- [ ] No hardcoded secrets in any file
- [ ] `.gitignore` covers `__pycache__`, `.env`, `secrets.toml`

### Documentation
- [ ] README.md is complete with navigation
- [ ] 9 directory README.md indexes exist
- [ ] All 1,371 local links resolve correctly
- [ ] All 19 notebook internal links resolve
- [ ] No orphaned resources

### Deployment
- [ ] `requirements.txt` at root level
- [ ] `apps/deployable_app/` ready for Community Cloud
- [ ] `.streamlit/config.toml` ships with repo
- [ ] Deployment guide is comprehensive
- [ ] No hardcoded file paths in any app

### Security
- [ ] No API keys in source code
- [ ] No passwords in source code
- [ ] `st.secrets` used for all sensitive data
- [ ] SQL injection prevention taught and demonstrated
- [ ] Input validation in file upload apps

### Instructor Materials
- [ ] `instructor/README.md` with navigation
- [ ] 16 session plans in `lecture_lab_sequence.md`
- [ ] 4 lab activities with timed tasks
- [ ] Solutions for all 19 exercises
- [ ] Assessment strategy with grade distribution
- [ ] Common mistakes catalog (35+ entries)

---

## Release Steps

1. **Final QA pass** — Run `docs/final_qa_report.md` checks
2. **Clean repository** — Remove any `__pycache__`, `.pyc`, temp files
3. **Commit all changes** — Stage and commit with descriptive message
4. **Tag release** — Create git tag for version
5. **Push to GitHub** — Push main branch
6. **Verify deployment** — Deploy `apps/deployable_app/` to Community Cloud
7. **Test live** — Verify deployed app works
8. **Announce** — Share with students/instructors

---

## Post-Release Monitoring

- [ ] Monitor Community Cloud deployment logs
- [ ] Check for student-reported issues
- [ ] Update Streamlit version when new releases arrive
- [ ] Review and incorporate feedback

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0.0 | 2026-09-03 | Initial release — complete course repository |

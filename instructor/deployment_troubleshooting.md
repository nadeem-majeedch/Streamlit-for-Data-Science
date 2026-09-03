# 🚨 Deployment Troubleshooting (Instructor Guide)

> **Streamlit for Data Science — Learn, Build, Deploy**
> *Instructor-facing guide for helping students debug deployment issues.*

---

## Quick Reference: Top 10 Deployment Failures

| Rank | Error | Cause | Fix |
|------|-------|-------|-----|
| 1 | Missing `requirements.txt` | File not in repo root | Create `requirements.txt` with all dependencies |
| 2 | Import error | Package not in requirements | Add missing package to `requirements.txt` |
| 3 | Hardcoded file paths | `/Users/me/data.csv` | Use relative paths only |
| 4 | Missing secrets | App expects API key | Add to Community Cloud secrets manager |
| 5 | Wrong entry point | `main.py` vs `app.py` | Set correct path in deployment settings |
| 6 | Python version mismatch | Code uses Python 3.11+ features | Pin Python version or simplify syntax |
| 7 | Large model file | `model.joblib` > 100MB | Use Git LFS or retrain with smaller model |
| 8 | Memory limit exceeded | Processing large dataset | Downsample, use caching, optimize |
| 9 | Build timeout | Long installation process | Simplify dependencies, remove unused packages |
| 10 | Port conflict | Hardcoded port | Never hardcode port in Streamlit apps |

---

## Deployment Flow (Student Perspective)

```
LOCAL DEVELOPMENT
    ↓
TEST LOCALLY: streamlit run app.py
    ↓
GIT SETUP: git init && git add . && git commit -m "Initial commit"
    ↓
GITHUB: Create repo, push code
    ↓
COMMUNITY CLOUD: Connect GitHub repo → Select branch → Set entry point
    ↓
DEPLOY: Click "Deploy"
    ↓
BUILD: Community Cloud installs requirements.txt
    ↓
RUN: App starts on community.streamlit.io
    ↓
MONITOR: Check logs for errors
    ↓
UPDATE: Push changes → auto-redeploy
```

---

## Troubleshooting by Error Type

### Build Failures

#### "No module named 'X'"
**Student question:** "My app works locally but fails to build."
**Diagnosis:** Package missing from `requirements.txt`
**Fix:** Add the package. Check `pip freeze > requirements.txt` locally.
**Prevention:** Teach students to maintain `requirements.txt` from Day 1.

#### "Error installing requirements"
**Student question:** "Build fails during dependency installation."
**Diagnosis:** Conflicting versions, platform-specific package, or compilation failure
**Fix:**
1. Check if the package has a pre-built wheel for Linux (Community Cloud runs Linux)
2. Simplify dependencies — remove unused packages
3. Pin versions: `numpy==1.24.0` not just `numpy`
**Prevention:** Test `pip install -r requirements.txt` on a clean Python environment.

#### "Build timed out"
**Student question:** "Build takes too long and fails."
**Diagnosis:** Too many dependencies or large packages (e.g., `tensorflow`)
**Fix:** Remove unnecessary packages. Consider lighter alternatives.
**Prevention:** Keep requirements minimal. Distinguish core vs. optional dependencies.

---

### Runtime Failures

#### "FileNotFoundError: 'data.csv'"
**Student question:** "It finds the file locally but not in the cloud."
**Diagnosis:** Hardcoded absolute path
**Fix:** Use relative paths: `pd.read_csv("data/file.csv")`
**Prevention:** Never use absolute paths in any file operation.

#### "ModuleNotFoundError" at runtime
**Student question:** "It built successfully but crashes on import."
**Diagnosis:** Package in requirements but wrong version or missing sub-dependency
**Fix:** Pin exact versions. Check the package's own requirements.
**Prevention:** Use `requirements.txt` with pinned versions.

#### "ImportError: cannot import name 'X'"
**Student question:** "The import works locally but fails in the cloud."
**Diagnosis:** API changed between versions, or Python version mismatch
**Fix:** Check package version locally (`pip show package_name`), pin that version.
**Prevention:** Test with the same Python version as Community Cloud (3.9–3.11).

#### App starts but shows blank page
**Student question:** "The app loads but nothing shows up."
**Diagnosis:** Error in the script that Streamlit catches silently
**Fix:** Check deployment logs for hidden errors. Add `st.write("Hello")` to verify the script runs.
**Prevention:** Add a "health check" line at the top of every app.

---

### Secrets and Configuration

#### "st.secrets" raises KeyError
**Student question:** "My API key works locally but fails in the cloud."
**Diagnosis:** Secrets not configured in Community Cloud
**Fix:** Go to app settings → Secrets → Add the key-value pairs
**Prevention:** Create a template `.streamlit/secrets_template.toml` (without real values)

#### Secrets format error
**Student question:** "I added secrets but it says format is wrong."
**Diagnosis:** TOML syntax error in secrets
**Fix:** Check for:
- Missing quotes around strings: `api_key = "sk-abc"` not `api_key = sk-abc`
- Missing brackets for nested tables
- Trailing commas
**Prevention:** Provide a secrets template with correct TOML syntax.

---

### Performance Issues

#### App is very slow
**Student question:** "My app takes 30+ seconds to load."
**Diagnosis:** No caching, expensive computation on every rerun
**Fix:** Add `@st.cache_data` for data loading and `@st.cache_resource` for models.
**Prevention:** Teach caching before deployment.

#### App crashes with memory error
**Student question:** "The app crashes when I upload a large file."
**Diagnosis:** Exceeds Community Cloud memory limit (1GB for free tier)
**Fix:** Add file size limits, process data in chunks, optimize memory usage.
**Prevention:** Discuss resource limits before deployment.

#### App goes to sleep
**Student question:** "My app stopped working after a few days."
**Diagnosis:** Community Cloud apps sleep after inactivity (free tier: ~1 week)
**Fix:** This is expected behavior. Users can wake it by visiting the URL.
**Prevention:** Document this limitation in the README.

---

## Instructor Intervention Checklist

When a student comes to you with a deployment issue:

1. **Ask:** "Does it work locally?" (If no, fix local first)
2. **Ask:** "What does the build log say?" (Check Community Cloud logs)
3. **Ask:** "Is `requirements.txt` in the repo root?" (Most common issue)
4. **Ask:** "Are there any hardcoded paths?" (Second most common)
5. **Ask:** "Are secrets configured in Community Cloud?" (If app uses API keys)
6. **Check:** Entry point path in deployment settings
7. **Check:** Python version compatibility
8. **Check:** File sizes (models, data files)
9. **Suggest:** Create a minimal test app to isolate the issue
10. **Escalate:** If Community Cloud itself is down, check status page

---

## Pre-Deployment Checklist (Give to Students)

```
□ requirements.txt exists in repo root
□ All imports are in requirements.txt
□ No hardcoded file paths (use relative paths)
□ No hardcoded secrets (use st.secrets)
□ .gitignore excludes secrets files
□ Entry point file exists (app.py or main.py)
□ App runs locally with: streamlit run app.py
□ No large files > 100MB in repo
□ README.md has setup instructions
```

---

## Common Community Cloud Limitations

| Limit | Free Tier | Pro Tier |
|-------|-----------|----------|
| Memory | 1 GB | 3+ GB |
| CPU | 1 vCPU | 2+ vCPUs |
| Disk | 1 GB | 5+ GB |
| Sleep | After ~1 week inactivity | Never |
| Build timeout | 15 minutes | 30+ minutes |
| File size | ~1 GB repo | ~10 GB repo |
| Custom domains | No | Yes |
| Auth | No | Yes |

---

## Deployment Day Tips

### Before the Lab
- Test Community Cloud status page
- Have a backup plan (local demo) if cloud is down
- Prepare a step-by-step walkthrough on the projector

### During the Lab
- Roam and help students one-on-one
- Note common issues for the review phase
- Have a "golden deployment" ready to show as an example

### If Cloud Is Down
- Let students demo locally instead
- Collect GitHub repo links for later deployment
- Use the downtime for code review or architecture discussion

---

## Related Materials

- [Deployment Guide](../readings/deployment_guide.md) — Student-facing deployment reading
- [Deployment Tutorial](../notebooks/deployment_tutorial.ipynb) — Step-by-step notebook
- [Deployment Checklist](../docs/deployment_checklist.md) — Student checklist
- [Deployment Exercises](../exercises/deployment_exercises.py) — Practice exercises
- [Common Mistakes](common_student_mistakes.md) — Error catalog

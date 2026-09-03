# Deployment Troubleshooting Guide

> **📚 Reference · Module 15 — Deployment**
> *Common deployment issues and their solutions.*

---

## Quick Reference

| Problem | Likely Cause | Quick Fix |
|---------|-------------|-----------|
| Build fails immediately | Missing `requirements.txt` | Create one with all imports |
| `ModuleNotFoundError` | Package not in requirements | Add package name |
| `SyntaxError` | Code error | Fix locally, test, push |
| App shows white page | Runtime error | Check logs |
| Secrets not found | Not configured | Add in Community Cloud settings |
| App is slow | No caching | Add `@st.cache_data` |
| App won't sleep/wake | Too many dependencies | Reduce requirements |
| `FileNotFoundError` | File not committed | `git add` and push |

---

## 1. Build Failures

### Missing requirements.txt

**Symptom:**
```
Could not find requirements.txt
```

**Cause:** Community Cloud expects `requirements.txt` at the repo root or app directory.

**Fix:**
```bash
# Create requirements.txt
echo "streamlit>=1.44.0" > requirements.txt
echo "pandas>=2.0.0" >> requirements.txt
git add requirements.txt
git commit -m "Add requirements.txt"
git push
```

### Module Not Found

**Symptom:**
```
ModuleNotFoundError: No module named 'plotly'
```

**Cause:** The package isn't listed in `requirements.txt`.

**Fix:**
```bash
# Add the missing package
echo "plotly>=5.15.0" >> requirements.txt
git add requirements.txt
git commit -m "Add plotly dependency"
git push
```

### Version Conflicts

**Symptom:**
```
ERROR: pip's dependency resolver does not currently take into account
```

**Cause:** Two packages require incompatible versions of a dependency.

**Fix:**
1. Pin compatible versions:
```txt
# ❌ Conflicting
pandas>=2.0.0
numpy>=2.0.0  # May conflict with older pandas

# ✅ Compatible
pandas>=2.0.0
numpy>=1.24.0,<2.0.0
```

2. Or use `--no-deps` for problematic packages (use carefully)

### Build Timeout

**Symptom:**
```
Build exceeded time limit
```

**Cause:** Too many dependencies or large packages being installed.

**Fix:**
- Reduce the number of packages in `requirements.txt`
- Remove packages not actually used by the app
- Pin versions to avoid resolving conflicts
- Avoid heavy packages like `tensorflow` or `torch` on free tier

---

## 2. Runtime Errors

### App Shows White/Blank Page

**Cause:** An unhandled exception occurs before any content renders.

**Debugging:**
1. Check deployment logs for the actual error
2. Run the app locally with `streamlit run app.py`
3. Check browser console (F12) for JavaScript errors

**Common Causes:**
- `st.set_page_config()` not being the first Streamlit call
- Import errors that only happen at runtime
- Missing files that exist locally but aren't committed

### KeyError (Secrets)

**Symptom:**
```
KeyError: 'openai'
```

**Cause:** Secret not configured in Community Cloud.

**Fix:**
1. Go to app settings → Secrets
2. Add the missing secret in TOML format:
```toml
[openai]
api_key = "sk-your-key"
```
3. Click Save

**Prevention:** Use safe access:
```python
api_key = st.secrets.get("openai", {}).get("api_key", "")
if not api_key:
    st.warning("OpenAI API key not configured.")
    st.stop()
```

### FileNotFoundError

**Symptom:**
```
FileNotFoundError: [Errno 2] No such file or directory: 'data/sales.csv'
```

**Cause:** File exists locally but wasn't committed to git.

**Fix:**
```bash
# Check if file is tracked
git status data/sales.csv

# If untracked, add it
git add data/sales.csv
git commit -m "Add data file"
git push
```

**Prevention:**
- Use `git status` before committing
- Commit all files the app needs
- Use `st.cache_data` to generate sample data instead of files

### Import Errors at Runtime

**Symptom:**
```
ImportError: cannot import name 'something' from 'package'
```

**Cause:** Package version in cloud differs from local.

**Fix:**
```txt
# Pin the version you tested with
package-name==1.2.3
```

---

## 3. Secrets Issues

### Secrets.toml Committed to Git

**Symptom:** Your secrets are visible in the GitHub repository.

**Fix:**
```bash
# Remove from tracking (keeps local file)
git rm --cached .streamlit/secrets.toml

# Add to .gitignore
echo ".streamlit/secrets.toml" >> .gitignore

# Commit
git commit -m "Remove secrets from tracking"
git push
```

**If secrets were exposed:**
1. Rotate ALL exposed credentials immediately
2. Generate new API keys
3. Update Community Cloud secrets with new values
4. Consider the old keys compromised

### TOML Syntax Errors

**Symptom:** Secrets not loading, no error shown.

**Cause:** Invalid TOML syntax in secrets configuration.

**Common mistakes:**
```toml
# ❌ Missing quotes around strings with special chars
[openai]
api_key = sk-your-key-here

# ✅ Correct
[openai]
api_key = "sk-your-key-here"

# ❌ Wrong section nesting
openai.api_key = "sk-..."

# ✅ Correct
[openai]
api_key = "sk-..."
```

---

## 4. Performance Issues

### App Is Very Slow

**Cause:** Expensive computations on every rerun.

**Fix:**
```python
# ❌ Recomputes on every interaction
def get_data():
    return pd.read_csv('huge_file.csv')

# ✅ Cached — computed once per session
@st.cache_data
def get_data():
    return pd.read_csv('huge_file.csv')
```

### App Takes Long to Start (Cold Start)

**Cause:** Too many imports or heavy dependencies.

**Fix:**
```python
# ❌ Imports everything at the top
import tensorflow as tf
import transformers
import torch

# ✅ Import only when needed
def load_model():
    import tensorflow as tf
    return tf.keras.models.load_model('model.h5')
```

### Memory Exceeded

**Symptom:** App crashes with "resource limits" message.

**Fix:**
1. Use `@st.cache_data` to avoid recomputation
2. Load only necessary columns: `pd.read_csv('data.csv', usecols=[...])`
3. Process data in chunks
4. Delete large objects: `del large_dataframe`
5. Use `st.cache_resource` for model loading

---

## 5. Configuration Issues

### Wrong Entry Point

**Symptom:** App deploys but shows wrong content or errors.

**Fix:**
1. Check the "Main file path" in app settings
2. Must be relative to repo root: `app.py` or `apps/my_app/app.py`

### Missing .streamlit/config.toml

**Symptom:** App runs but uses default theme.

**Fix:**
Create `.streamlit/config.toml`:
```toml
[theme]
base = "light"
primaryColor = "#FF4B4B"

[server]
headless = true
```

---

## 6. Git Issues

### Large Files in Repository

**Symptom:** Push fails or is extremely slow.

**Fix:**
```bash
# Check repository size
du -sh .git

# Find large files
git ls-files -z | xargs -0 du -sh | sort -rh | head -10

# Remove large files from tracking
git rm --cached large_file.csv
echo "large_file.csv" >> .gitignore
git commit -m "Remove large file from tracking"
```

### Wrong Branch

**Symptom:** Community Cloud deploys an old version.

**Fix:**
1. Check which branch is selected in app settings
2. Make sure you pushed to that branch
3. Verify with `git branch -a`

### Accidental Secrets in History

**Symptom:** Secrets were committed then removed, but still in git history.

**Fix:**
1. Rotate all exposed credentials IMMEDIATELY
2. Use `git filter-branch` or BFG Repo-Cleaner to remove from history
3. Force push (coordinate with team)
4. Consider the old credentials compromised

---

## 7. Platform-Specific Issues

### Community Cloud Sleep Behavior

**Understanding:** Free tier apps go to sleep after ~10 minutes of inactivity.

**Impact:**
- First visit after sleep takes 30–60 seconds
- Cached data may need to rebuild

**Mitigation:**
```python
# Show a friendly message during cold start
@st.cache_data
def load_data():
    # This runs on first load after sleep
    return expensive_computation()

# The spinner shows while loading
with st.spinner("Loading data..."):
    data = load_data()
```

### Python Version Mismatch

**Symptom:** Syntax works locally but fails in cloud.

**Fix:**
```txt
# Specify Python version in requirements
python>=3.10,<3.12
```

Or check Community Cloud Python version in app settings.

---

## 8. Getting Help

### Where to Find Answers

1. **Deployment logs** — most informative source
2. **Streamlit Community Forum** — [discuss.streamlit.io](https://discuss.streamlit.io)
3. **Stack Overflow** — tag: `streamlit`
4. **GitHub Issues** — [github.com/streamlit/streamlit/issues](https://github.com/streamlit/streamlit/issues)

### What to Include When Asking for Help

- Error message (full traceback)
- Streamlit version (`pip show streamlit`)
- Python version (`python --version`)
- What you expected vs. what happened
- Minimal code that reproduces the issue
- Whether it works locally but fails in cloud

---

## Key Takeaways

1. **Check logs first** — they contain the actual error
2. **Test locally** — most issues are caught before deployment
3. **Keep requirements minimal** — fewer dependencies = fewer problems
4. **Never commit secrets** — use Community Cloud settings
5. **Use git status** — verify what's being committed
6. **Monitor after deploy** — check logs periodically

---

## Related Materials

- 📖 Reading: [Deployment Guide](../readings/deployment_guide.md)
- 📓 Notebook: [Deployment Tutorial](../notebooks/deployment_tutorial.ipynb)
- 📋 Checklist: [Deployment Checklist](../docs/deployment_checklist.md)
- 🖥️ Example: [Deployable App](../apps/deployable_app/)

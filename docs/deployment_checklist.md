# Deployment Checklist

> **📋 Reference · Module 15 — Deployment**
> *Use this checklist before every deployment to Streamlit Community Cloud.*

---

## Pre-Deployment Checklist

### Application Code

- [ ] App runs locally without errors: `streamlit run app.py`
- [ ] All imports are available and in `requirements.txt`
- [ ] `st.set_page_config()` is the **first** Streamlit call
- [ ] No hardcoded file paths (use relative paths)
- [ ] No hardcoded secrets or API keys
- [ ] Error handling for user inputs
- [ ] App handles empty/missing data gracefully
- [ ] No `print()` statements that shouldn't be in production
- [ ] No debug code or TODO comments in production

### Dependencies

- [ ] `requirements.txt` exists at repo root or app directory
- [ ] All imported packages are listed
- [ ] Versions are pinned (recommended: `package>=1.0.0`)
- [ ] No development-only packages (ipython, jupyter, pytest)
- [ ] Package sizes are reasonable for free tier

### Files and Structure

- [ ] Entry point file exists (e.g., `app.py`)
- [ ] All required data files are committed
- [ ] No large files (> 100 MB) in repository
- [ ] No `__pycache__/`, `.venv/`, or build artifacts
- [ ] `.gitignore` is properly configured

### Secrets and Security

- [ ] No `secrets.toml` in git: `git ls-files | grep secret`
- [ ] `.gitignore` includes `.streamlit/secrets.toml`
- [ ] All secrets configured in Community Cloud settings
- [ ] Code uses safe secret access: `st.secrets.get("key", {}).get("subkey", "")`
- [ ] User inputs are validated before processing
- [ ] SQL queries use parameterized statements
- [ ] No dangerous `exec()` or `eval()` calls

### Git Repository

- [ ] All changes are committed
- [ ] No untracked sensitive files
- [ ] Commit message is descriptive
- [ ] Pushed to the correct branch (usually `main`)

---

## Community Cloud Configuration

### App Settings

- [ ] **Repository:** Correct repository selected
- [ ] **Branch:** Correct branch (usually `main`)
- [ ] **Main file path:** Points to your entry point (e.g., `app.py`)
- [ ] **Python version:** Compatible with your code (3.10+ recommended)

### Secrets Configuration

- [ ] All required secrets added in Advanced Settings → Secrets
- [ ] TOML syntax is valid
- [ ] No trailing commas in TOML
- [ ] Secrets tested with `st.secrets.get()` with defaults

### Theme (Optional)

- [ ] Custom theme configured in `.streamlit/config.toml`
- [ ] `headless = true` in server config
- [ ] `enableXsrfProtection = true` for security

---

## Post-Deployment Verification

### Initial Check

- [ ] App loads without errors
- [ ] No white/blank page
- [ ] Theme and styling appear correct
- [ ] All interactive elements work

### Feature Verification

- [ ] All pages/tabs load correctly
- [ ] Widgets respond to interaction
- [ ] Data loads and displays correctly
- [ ] Charts render properly
- [ ] File uploads work (if applicable)
- [ ] Downloads work (if applicable)
- [ ] Forms submit correctly

### Performance

- [ ] App loads in < 30 seconds (cold start)
- [ ] Interactions respond in < 5 seconds
- [ ] No memory warnings in logs
- [ ] Caching is working (check with `@st.cache_data`)

### Security

- [ ] No secrets visible in the app
- [ ] User inputs are sanitized
- [ ] Error messages don't expose sensitive info
- [ ] HTTPS is enabled (default on Community Cloud)

---

## Deployment Troubleshooting

### If Build Fails

1. Check build logs for the specific error
2. Verify `requirements.txt` has all dependencies
3. Check Python version compatibility
4. Ensure no syntax errors: `python -m py_compile app.py`

### If App Crashes at Runtime

1. Check deployment logs (Manage app → Logs)
2. Test the exact same code locally
3. Check for missing files: `git ls-files | grep filename`
4. Verify secrets are configured

### If App Is Slow

1. Add `@st.cache_data` to expensive functions
2. Reduce data loaded into memory
3. Minimize dependencies in `requirements.txt`
4. Use lazy imports for heavy packages

---

## Update Checklist

When updating a deployed app:

- [ ] Test changes locally first
- [ ] Update `requirements.txt` if new packages added
- [ ] Commit with descriptive message
- [ ] Push to the deployment branch
- [ ] Verify auto-redeployment triggered
- [ ] Check logs for errors
- [ ] Test all features in deployed version
- [ ] Rollback if critical issues found

---

## Quick Commands

```bash
# Verify no secrets in git
git ls-files | grep -i secret
git ls-files | grep -i "\.env"

# Check requirements.txt
cat requirements.txt

# Test locally
streamlit run app.py

# Check git status before push
git status

# Push for deployment
git push origin main

# View deployment logs (Community Cloud)
# Go to app → ⋮ → Manage app → Logs
```

---

## Related Materials

- 📖 Reading: [Deployment Guide](../readings/deployment_guide.md)
- 📓 Notebook: [Deployment Tutorial](../notebooks/deployment_tutorial.ipynb)
- 📚 Troubleshooting: [Deployment Issues](../docs/deployment_troubleshooting.md)
- 🖥️ Example: [Deployable App](../apps/deployable_app/)

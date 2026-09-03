# Quiz: Deployment & Community Cloud

> **📝 Quiz · Module 15 — Deployment**
> *Test your understanding of deploying Streamlit applications.*

---

## Part A: Multiple Choice (1 point each)

### Q1. What file is REQUIRED for Community Cloud deployment?

A. `Dockerfile`
B. `app.py` and `requirements.txt`
C. `setup.py`
D. `Makefile`

### Q2. Where should you configure secrets for a Community Cloud deployment?

A. In a `secrets.toml` file committed to the repository
B. In environment variables set on your local machine
C. In the app settings on Community Cloud
D. In the `requirements.txt` file

### Q3. What happens when you push changes to the deployment branch?

A. Nothing — you must manually redeploy
B. Community Cloud automatically rebuilds and redeploys
C. The app goes to sleep immediately
D. You receive an email confirmation

### Q4. Why should `st.set_page_config()` be the first Streamlit call?

A. It's required by Community Cloud
B. Streamlit raises an error if it's not first
C. It sets the page title for the browser
D. Both B and C

### Q5. What is the best way to handle a missing API key in a deployed app?

A. Hardcode a default key in the source code
B. Use `st.secrets.get()` with a fallback and show a warning
C. Skip the feature entirely if the key is missing
D. Print the error to the console

### Q6. How can you prevent secrets from being committed to git?

A. Add `.streamlit/secrets.toml` to `.gitignore`
B. Use `git rm --cached` if already committed
C. Never commit files containing secrets
D. All of the above

### Q7. What is "app sleep" on Community Cloud?

A. The app shuts down permanently after inactivity
B. The app pauses after inactivity and restarts on next visit
C. The app runs in the background at reduced capacity
D. The app stops accepting new users

### Q8. Which of the following is NOT a valid reason for a build failure?

A. Missing `requirements.txt`
B. Syntax error in `app.py`
C. Using `st.cache_data` decorator
D. Missing dependency in `requirements.txt`

### Q9. How do you view deployment logs on Community Cloud?

A. Run `streamlit logs` in terminal
B. Go to app settings → Manage app → Logs
C. Check the GitHub Actions tab
D. Download from the Community Cloud dashboard

### Q10. What should you do if your deployed app shows a white page?

A. Refresh the browser repeatedly
B. Check deployment logs for the error
C. Delete and recreate the app
D. Change the app's URL

### Q11. Which is the correct way to specify a file path in a deployed app?

A. `/Users/me/data/sales.csv`
B. `C:\\Users\\me\\data\\sales.csv`
C. `data/sales.csv` (relative path)
D. `~/data/sales.csv`

### Q12. What is the recommended Python version for Streamlit Community Cloud?

A. Python 3.8
B. Python 3.10+
C. Python 2.7
D. Any version works

---

## Part B: Short Answer (3 points each)

### Q13. Explain the deployment workflow from local development to a live app. List each step.

### Q14. Your app works locally but fails on Community Cloud with `ModuleNotFoundError: No module named 'plotly'`. What went wrong and how do you fix it?

### Q15. Describe two strategies to reduce cold-start time for a deployed Streamlit app.

---

## Part C: Code Completion (5 points each)

### Q16. Write a Python function that safely accesses a secret from Streamlit with a fallback default:

```python
import streamlit as st

def get_api_key() -> str:
    """Safely retrieve the OpenAI API key from secrets."""
    # Your code here
    pass
```

### Q17. Write a deployment-ready `requirements.txt` file for an app that uses Streamlit, Pandas, Plotly, and requests. Pin minimum versions.

---

## Answer Key

### Part A: Multiple Choice

| Q | Answer | Explanation |
|---|--------|-------------|
| 1 | **B** | `app.py` (entry point) and `requirements.txt` (dependencies) are required |
| 2 | **C** | Secrets are configured in Community Cloud app settings, never in code |
| 3 | **B** | Community Cloud auto-redeploys on push to the deployment branch |
| 4 | **D** | Streamlit raises an error if it's not first, and it sets the page config |
| 5 | **B** | Safe access with `.get()` and a user-facing warning is best practice |
| 6 | **D** | All three approaches help prevent secret exposure |
| 7 | **B** | Apps pause after inactivity and restart on next visit (cold start) |
| 8 | **C** | Using `@st.cache_data` is a best practice, not a build failure cause |
| 9 | **B** | Logs are in app settings → Manage app → Logs tab |
| 10 | **B** | Check deployment logs — they contain the actual error message |
| 11 | **C** | Relative paths work in both local and cloud environments |
| 12 | **B** | Python 3.10+ is recommended for modern Streamlit features |

### Part B: Short Answer

**Q13. Deployment Workflow:**
1. Write/test app locally (`streamlit run app.py`)
2. Create `requirements.txt` with dependencies
3. Add `.gitignore` to exclude secrets and cache
4. Test all features work correctly
5. `git add` and `git commit` with descriptive message
6. `git push origin main` to GitHub
7. Go to share.streamlit.io → New app
8. Select repository, branch, and entry point
9. Configure secrets in Advanced Settings if needed
10. Click Deploy and wait for build
11. Verify app loads and works
12. Share the URL

**Q14. Fix:** The `plotly` package is imported in the code but missing from `requirements.txt`. Fix by adding `plotly>=5.15.0` to the file, committing, and pushing. Community Cloud will rebuild with the new dependency.

**Q15. Cold-start strategies:**
1. Use `@st.cache_data` / `@st.cache_resource` to cache expensive computations so they only run once per session
2. Keep `requirements.txt` minimal — fewer packages means faster installation during build
3. Use lazy imports for heavy packages (import inside functions, not at top level)

### Part C: Code Completion

**Q16:**
```python
import streamlit as st

def get_api_key() -> str:
    """Safely retrieve the OpenAI API key from secrets."""
    try:
        api_key = st.secrets["openai"]["api_key"]
        if api_key and api_key != "sk-your-key-here":
            return api_key
    except (KeyError, FileNotFoundError):
        pass
    
    st.warning("⚠️ OpenAI API key not configured. Add it in app settings → Secrets.")
    st.stop()
    return ""  # Never reached due to st.stop()
```

**Q17:**
```txt
streamlit>=1.44.0
pandas>=2.0.0
plotly>=5.15.0
requests>=2.31.0
```

---

## Related Materials

- 📖 Reading: [Deployment Guide](../readings/deployment_guide.md)
- 📓 Notebook: [Deployment Tutorial](../notebooks/deployment_tutorial.ipynb)
- 📚 Troubleshooting: [Deployment Issues](../docs/deployment_troubleshooting.md)
- 📋 Checklist: [Deployment Checklist](../docs/deployment_checklist.md)
- 🖥️ Example: [Deployable App](../apps/deployable_app/)

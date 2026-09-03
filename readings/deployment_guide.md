# Deployment Guide

> **📖 Reading · Deployment Module**  
> *Complete guide to deploying Streamlit applications.*

---

## Learning Objectives

After completing this reading you will be able to:

- Prepare a Streamlit app for deployment
- Organize repository structure correctly
- Configure dependencies and secrets
- Deploy to Streamlit Community Cloud
- Debug deployment issues
- Update and redeploy applications
- Understand resource limitations

---

## 1. Deployment Workflow

```
LOCAL DEVELOPMENT
       │
       ▼
   TEST LOCALLY
       │
       ▼
   COMMIT TO GIT
       │
       ▼
   PUSH TO GITHUB
       │
       ▼
   DEPLOY TO CLOUD
       │
       ▼
   MONITOR & DEBUG
       │
       ▼
   UPDATE & REDEPLOY
```

---

## 2. Repository Organization

### Basic Structure

```
your-repo/
├── .streamlit/
│   └── config.toml      # Streamlit configuration
├── requirements.txt      # Python dependencies
├── .gitignore           # Files to ignore
├── README.md            # Documentation
└── app.py               # Entry point
```

### Multiple Apps Structure

```
your-repo/
├── .streamlit/
│   └── config.toml
├── requirements.txt     # Shared dependencies
├── app1/
│   ├── requirements.txt # App-specific deps (optional)
│   └── main.py          # App 1 entry point
└── app2/
    ├── requirements.txt # App-specific deps (optional)
    └── main.py          # App 2 entry point
```

---

## 3. Essential Files

### requirements.txt

```txt
# requirements.txt
streamlit>=1.44.0
pandas>=2.0.0
numpy>=1.24.0
plotly>=5.15.0
```

### .gitignore

```gitignore
# Python
__pycache__/
*.py[cod]
*.egg-info/
dist/
build/

# Virtual environments
.venv/
venv/
env/

# IDE
.vscode/
.idea/

# Streamlit
.streamlit/secrets.toml

# Uploaded files
uploads/

# OS files
.DS_Store
Thumbs.db
```

### .streamlit/config.toml

```toml
[theme]
base = "light"
primaryColor = "#FF4B4B"

[server]
headless = true
enableCORS = false
enableXsrfProtection = true

[browser]
gatherUsageStats = false
```

---

## 4. Streamlit Community Cloud Deployment

### Step 1: Push to GitHub

```bash
git add .
git commit -m "Prepare for deployment"
git push origin main
```

### Step 2: Connect to Community Cloud

1. Go to [share.streamlit.io](https://share.streamlit.io)
2. Sign in with GitHub
3. Click "New app"

### Step 3: Configure Deployment

- **Repository:** Select your repository
- **Branch:** Usually `main`
- **Main file path:** `app.py` (or your entry point)
- **App URL:** Custom subdomain (optional)

### Step 4: Add Secrets (if needed)

1. Click "Advanced settings"
2. Paste your `.streamlit/secrets.toml` content
3. Click "Save"

### Step 5: Deploy

Click "Deploy!" and wait for build to complete.

---

## 5. Secrets Management

### Local Development

Create `.streamlit/secrets.toml` (NEVER commit):

```toml
[openai]
api_key = "sk-your-key"

[database]
host = "localhost"
password = "secret"
```

### Community Cloud

1. Go to app settings
2. Click "Secrets"
3. Paste TOML content
4. Save

### Access in Code

```python
import streamlit as st

api_key = st.secrets.openai.api_key
db_host = st.secrets.database.host
```

---

## 6. Common Deployment Issues

### Dependency Failures

**Symptom:** Build fails with import errors

**Solution:**
- Check `requirements.txt` includes all imports
- Pin versions if needed
- Check Python version compatibility

### Missing Files

**Symptom:** FileNotFoundError during runtime

**Solution:**
- Ensure all files are committed to git
- Use relative paths from entry point
- Check file paths use forward slashes

### Secrets Not Found

**Symptom:** KeyError or AttributeError

**Solution:**
- Verify secrets are added in Community Cloud settings
- Check TOML syntax is correct
- Use `st.secrets.get()` with defaults

### Memory Limits

**Symptom:** "App has gone over resource limits"

**Solution:**
- Optimize memory usage
- Use caching (`@st.cache_data`)
- Reduce data loaded into memory
- Close unused connections

---

## 7. Resource Limits (Community Cloud)

| Resource | Limit |
|----------|-------|
| Memory | 1 GB (free tier) |
| CPU | 0.078 cores minimum |
| Storage | 50 GB maximum |
| Apps | Limited per account |

### App Sleep

- Apps go to sleep after inactivity
- First visit wakes the app (may take 30-60 seconds)
- Consider this for production apps

---

## 8. Updating Deployed Apps

### Automatic Redeployment

1. Push changes to GitHub
2. Community Cloud auto-deploys

### Manual Redeployment

1. Go to app settings
2. Click "Reboot app"

### Rollback

1. Revert git changes
2. Push to GitHub
3. Auto-deploys previous version

---

## 9. Security Considerations

### Public vs Private

| Aspect | Public Repo | Private Repo |
|--------|-------------|--------------|
| Code visibility | Anyone can see | Only collaborators |
| Deployment | Easier | Requires GitHub OAuth |
| Secrets | Still hidden | Hidden |
| Best for | Open source, learning | Production, sensitive code |

### Deployment Security

- Never commit secrets
- Use environment variables
- Validate all inputs
- Enable CORS/XSRF protection
- Use HTTPS (default on Community Cloud)

---

## 10. Best Practices

### Do's

- ✅ Test locally before deploying
- ✅ Use requirements.txt with pinned versions
- ✅ Add .gitignore for secrets
- ✅ Write clear README
- ✅ Use meaningful commit messages
- ✅ Monitor app logs

### Don'ts

- ❌ Commit secrets to git
- ❌ Use absolute file paths
- ❌ Ignore error messages
- ❌ Skip local testing
- ❌ Use large files in repo

---

## Key Takeaways

1. **Test locally first** — Always verify before deploying
2. **Organize properly** — Clear structure helps deployment
3. **Manage secrets** — Never commit, use Cloud settings
4. **Monitor logs** — Check for errors after deployment
5. **Update regularly** — Push changes for auto-redeploy

---

## Further Reading

- [Community Cloud Documentation](https://docs.streamlit.io/deploy/streamlit-community-cloud)
- [Deployment Tutorials](https://docs.streamlit.io/knowledge-base/deploy)

---

## Related Materials

- 📓 Notebook: [Deployment Tutorial](../notebooks/deployment_tutorial.ipynb)
- 📚 Troubleshooting: [Deployment Issues](../docs/deployment_troubleshooting.md)
- ✏️ Exercises: [Deployment Exercises](../exercises/deployment_exercises.py)
- 📋 Checklist: [Deployment Checklist](../docs/deployment_checklist.md)
- 🖥️ Example: [Deployable App](../apps/deployable_app/)

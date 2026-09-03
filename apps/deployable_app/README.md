# Deployable Data Science Dashboard

A complete, ready-to-deploy Streamlit application for learning deployment workflows.

## What This App Demonstrates

- Clean project structure for deployment
- Session state for filter persistence
- Caching for performance
- Error handling for production
- Sidebar filters with multiple inputs
- KPI metrics display
- Interactive charts (line, bar)
- Data tables with sorting
- CSV download
- No hardcoded secrets

## How to Deploy

### Option 1: Streamlit Community Cloud (Recommended)

1. Push this entire repository to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Click **"New app"**
4. Select your repository, branch `main`, and file path `apps/deployable_app/app.py`
5. Click **Deploy!**

### Option 2: Run Locally

```bash
pip install -r apps/deployable_app/requirements.txt
streamlit run apps/deployable_app/app.py
```

## File Structure

```
apps/deployable_app/
├── app.py              # Main application
├── requirements.txt    # Python dependencies
└── README.md           # This file
```

## Secrets (Not Required)

This demo app uses only generated sample data and requires no API keys or secrets.
For apps that need secrets, see the [deployment guide](../../readings/deployment_guide.md).

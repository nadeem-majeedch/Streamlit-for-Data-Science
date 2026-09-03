"""
Exercise 16 — Production, Maintenance & Monitoring
====================================================
Module 16 · Production

Prepare a Streamlit application for production deployment with
monitoring, error handling, and maintenance best practices.

Run this file:
    streamlit run exercises/16_production_ready.py

Instructions:
    Complete every TODO section. This exercise focuses on production
    concerns: error handling, logging, graceful degradation, and monitoring.

Related Materials:
- Reading: ../readings/deployment_guide.md
- Reading: ../readings/security_and_secrets.md
- Notebook: ../notebooks/deployment_tutorial.ipynb
- Doc: ../docs/deployment_checklist.md
- Doc: ../docs/deployment_troubleshooting.md
"""

import streamlit as st
import logging
import sys
from datetime import datetime

# ---------------------------------------------------------------------------
# Page Config
# ---------------------------------------------------------------------------
st.set_page_config(
    page_title="Exercise 16 — Production Ready",
    page_icon="🏭",
    layout="wide",
)

st.title("🏭 Exercise 16 — Production Ready")
st.markdown(
    "Build apps that handle failures gracefully and provide monitoring."
)

st.divider()

# ============================================================================
# PART 1 — Understanding Production Challenges
# ============================================================================

st.header("Part 1 — Production vs Development")

st.markdown("""
**Q1:** Your app works perfectly on your laptop but crashes on Community Cloud.
Which is the MOST likely cause?

A) The Community Cloud has a different version of Streamlit
B) A file exists locally but was not committed to the git repository
C) The cloud server is too slow
D) Your browser is incompatible

**Q2:** A user reports that your deployed app shows a white page.
What is the FIRST thing you should check?

A) Ask the user to clear their browser cache
B) Check the deployment logs on Community Cloud
C) Restart the app from the Community Cloud dashboard
D) Push a new commit to fix the issue

**Q3:** Which of these is NOT a reason to use @st.cache_data?

A) A database query that takes 10 seconds
B) Generating a random UUID for session tracking
C) Loading a large CSV file
D) Computing a heavy aggregation

<details>
<summary>Answers</summary>

Q1: **B** — Missing files are the #1 cause of "works locally, fails in cloud."
Q2: **B** — Logs contain the actual error message. Always check logs first.
Q3: **B** — A UUID should be unique per session, not cached. Caching it
would return the same UUID to all users.

</details>
""")

st.divider()

# ============================================================================
# PART 2 — Error Handling Patterns
# ============================================================================

st.header("Part 2 — Graceful Error Handling")

# TODO 2a: Complete this function that safely divides two numbers.
#   - If divisor is 0, return None and show st.warning()
#   - If inputs are not numbers, return None and show st.error()
#   - Otherwise return the result

def safe_divide(a, b):
    """Safely divide a by b, handling errors gracefully."""
    # Your code here:
    pass


# TODO 2b: Complete this function that safely loads data.
#   - Try to create a sample DataFrame
#   - On any exception, show st.error() with the message
#   - Always return a DataFrame (empty on failure)

def safe_load_data():
    """Load sample data with error handling."""
    # Your code here:
    pass


# Test your functions
col1, col2 = st.columns(2)

with col1:
    st.subheader("Safe Divide")
    result = safe_divide(10, 2)
    if result is not None:
        st.success(f"10 / 2 = {result}")

    result = safe_divide(10, 0)
    if result is None:
        st.info("Division by zero handled gracefully")

with col2:
    st.subheader("Safe Data Load")
    df = safe_load_data()
    if df is not None and not df.empty:
        st.dataframe(df)
    elif df is not None:
        st.info("Empty DataFrame returned (failure handled)")

st.divider()

# ============================================================================
# PART 3 — Structured Logging
# ============================================================================

st.header("Part 3 — Application Logging")

# TODO 3a: Set up a basic logger
#   - Configure logging with format "%(asctime)s - %(levelname)s - %(message)s"
#   - Set level to INFO

# Your code here:

# TODO 3b: Add logging to this app function:
#   - Log when the app starts
#   - Log when data is loaded
#   - Log when a user performs an action
#   - Log any errors with exc_info=True

def run_monitored_app():
    """Run an app with structured logging."""
    # Your code here:
    pass

st.info(
    "Complete the logging setup above. When run, your app should "
    "produce log output in the terminal."
)

st.divider()

# ============================================================================
# PART 4 — Health Check
# ============================================================================

st.header("Part 4 — Build a Health Check Page")

# TODO 4: Build a "health check" section that displays:
#   1. App version (hardcode "1.0.0")
#   2. Current timestamp
#   3. Python version
#   4. Streamlit version
#   5. Status of a simulated dependency (use st.cache_resource)
#   6. Memory usage estimate (os module)
#
# This simulates a monitoring dashboard for a production app.

# Your code here:

st.divider()

# ============================================================================
# PART 5 — Design Decision
# ============================================================================

st.header("Part 5 — Architecture Decisions")

st.markdown("""
You are deploying a data pipeline app that:
- Processes uploaded CSV files (up to 100 MB)
- Runs a Pandas aggregation (takes 5–15 seconds)
- Displays results in charts
- Allows downloading the processed data

**Design Question:** How should you handle the 5–15 second processing delay?

A) Show nothing until processing completes
B) Use st.spinner() with a descriptive message
C) Use st.progress() with an estimated completion time
D) Use st.toast() to notify when done
E) B or C are both acceptable, depending on predictability of duration

**Follow-up:** At what point would you switch from B to C to D?

<details>
<summary>Answer</summary>

**E** — If the processing time is predictable (within a narrow range),
`st.progress()` gives better UX. If unpredictable, `st.spinner()` is
simpler and appropriate. `st.toast()` is best for background tasks that
don't block the UI. In production, you'd also consider `st.fragment`
with `run_every` for periodic updates.

</details>
""")

st.divider()

# ============================================================================
# PART 6 — Scenario: Debug the Production App
# ============================================================================

st.header("Part 6 — Debug This Production App")

st.markdown("""
A colleague deploys this code and reports:
*"The app works locally but shows a white page on Community Cloud."*

```python
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Sales Report", layout="wide")

@st.cache_data
def load_data():
    return pd.read_csv("data/sales_2024.csv")

df = load_data()
st.title("Sales Report 2024")
st.dataframe(df.head(10))
```

Identify ALL deployment issues:
""")

# TODO 6: List every issue you can find
# Issues:
# 1. _______________________________________________
# 2. _______________________________________________
# 3. _______________________________________________

# Your analysis here:

st.markdown("""
<details>
<summary>Click to reveal issues</summary>

**Issue 1:** `data/sales_2024.csv` may not exist on Community Cloud.
The file needs to be committed to the repository OR the app should
generate sample data.

**Issue 2:** `requirements.txt` must exist with `streamlit` and `pandas`
listed as dependencies.

**Issue 3:** No `.streamlit/config.toml` with `headless = true` for
cloud deployment.

**Fix:**
```python
import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Sales Report", layout="wide")

@st.cache_data
def load_data():
    # Generate sample data if no file exists
    np.random.seed(42)
    return pd.DataFrame({
        "date": pd.date_range("2024-01-01", periods=100),
        "sales": np.random.uniform(100, 1000, 100).round(2),
        "region": np.random.choice(["North", "South", "East", "West"], 100),
    })

df = load_data()
st.title("Sales Report 2024")
st.dataframe(df.head(10))
```

</details>
""")

st.divider()
st.caption("Exercise 16 complete. You are now ready for the Capstone Project (P08).")

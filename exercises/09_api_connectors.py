"""
Exercise 09 — API Connectors & External Data
==============================================
Module 09 · Advanced

Build Streamlit apps that consume REST APIs, handle JSON,
and display external data interactively.

Run this file:
    streamlit run exercises/09_api_connectors.py

Instructions:
    Complete every TODO. This exercise uses ONLY free public APIs.
    No API keys required.

Related Materials:
- Reading: ../readings/13_application_architecture.md
- Notebook: ../notebooks/13_application_architecture.ipynb
- Demo App: ../apps/13_modular_app/
"""

import streamlit as st
import json

# ---------------------------------------------------------------------------
# Page Config
# ---------------------------------------------------------------------------
st.set_page_config(
    page_title="Exercise 09 — API Connectors",
    page_icon="🔌",
    layout="wide",
)

st.title("🔌 Exercise 09 — API Connectors & External Data")
st.markdown(
    "Build apps that fetch, process, and display data from REST APIs."
)

st.divider()

# ============================================================================
# PART 1 — Understanding APIs
# ============================================================================

st.header("Part 1 — Understand the API Response")

st.markdown("""
This exercise uses `https://jsonplaceholder.typicode.com` — a free
fake REST API for testing.

**Q1:** What HTTP method retrieves data from an API?
- A) POST
- B) GET
- C) DELETE

**Q2:** What format do most REST APIs return?
- A) CSV
- B) XML
- C) JSON

**Q3:** What does the status code `404` mean?
- A) Server error
- B) Not found
- C) Unauthorized

<details>
<summary>Answers</summary>

Q1: **B** — GET retrieves data.
Q2: **C** — JSON is the standard REST response format.
Q3: **B** — 404 means the requested resource was not found.

</details>
""")

st.divider()

# ============================================================================
# PART 2 — Basic API Fetch
# ============================================================================

st.header("Part 2 — Fetch Users from API")

# TODO 2a: Import `requests` at the top of the file

# TODO 2b: Write a function `fetch_users()` that:
#   - Fetches https://jsonplaceholder.typicode.com/users
#   - Returns the list of user dicts
#   - Handles connection errors gracefully with try/except

def fetch_users():
    """Fetch users from jsonplaceholder API."""
    import requests
    try:
        response = requests.get(
            "https://jsonplaceholder.typicode.com/users",
            timeout=10
        )
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        st.error(f"API request failed: {e}")
        return []

# TODO 2c: Call fetch_users() and display the count
users = fetch_users()
if users:
    st.success(f"Loaded {len(users)} users from API")
else:
    st.warning("No users loaded")

st.divider()

# ============================================================================
# PART 3 — Display as DataFrame
# ============================================================================

st.header("Part 3 — Display as DataFrame")

# TODO 3a: Convert the users list to a DataFrame with columns:
#   "ID", "Name", "Username", "Email", "City"
#   (Extract city from user["address"]["city"])

import pandas as pd

if users:
    df = pd.DataFrame([
        {
            "ID": u["id"],
            "Name": u["name"],
            "Username": u["username"],
            "Email": u["email"],
            "City": u["address"]["city"],
        }
        for u in users
    ])
    st.dataframe(df, use_container_width=True, hide_index=True)

# TODO 3b: Add a selectbox to filter users by city
# TODO 3c: Display only matching users in the DataFrame

# Your code here:

st.divider()

# ============================================================================
# PART 4 — Nested Data Extraction
# ============================================================================

st.header("Part 4 — Extract Nested Data")

# TODO 4a: From the users data, extract company names
#   (users[i]["company"]["name"])

# TODO 4b: Create a bar chart showing how many users are in each city
#   using st.bar_chart()

# Your code here:

st.divider()

# ============================================================================
# PART 5 — Build an App
# ============================================================================

st.header("Part 5 — Design Challenge")

st.markdown("""
Build a mini "User Directory" app that:

1. Fetches users from the API on load
2. Lets the user search by name (text_input)
3. Lets the user filter by city (selectbox)
4. Shows matching users in a DataFrame
5. Shows user details in an expander when a user is selected
6. Displays the company info for the selected user

**Architecture question:** Where should the API call happen?
- A) Inside the sidebar widget callback
- B) At the top of the script, cached with @st.cache_data
- C) On every rerun without caching
- D) Inside a button click handler

<details>
<summary>Answer</summary>

**B** — Cache the API response at the top of the script with
`@st.cache_data(ttl=300)`. This avoids re-fetching on every rerun
while still refreshing periodically.

</details>
""")

# BONUS: Build the full app above
# Your code here:

st.divider()
st.caption("Exercise 09 complete. Proceed to Exercise 13 for architecture patterns.")

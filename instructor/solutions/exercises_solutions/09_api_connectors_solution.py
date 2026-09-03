"""
Exercise 09 — API Connectors SOLUTION
=======================================
INSTRUCTOR USE ONLY — Do not share with students.

Reference implementation with all TODOs completed.
Run: streamlit run instructor/solutions/exercises_solutions/09_api_connectors_solution.py
"""

import streamlit as st
import json
import pandas as pd

st.set_page_config(
    page_title="Exercise 09 — API Connectors (SOLUTION)",
    page_icon="✅",
    layout="wide",
)

st.title("✅ Exercise 09 — API Connectors (Solution)")
st.markdown("Complete reference implementation for instructor use.")
st.divider()

# ============================================================================
# Part 1 — Theory (answers embedded)
# ============================================================================

st.header("Part 1 — API Concepts")
st.info("Q1: **B** (GET) · Q2: **C** (JSON) · Q3: **B** (Not found)")

st.divider()

# ============================================================================
# Part 2 — Fetch Users
# ============================================================================

st.header("Part 2 — Fetch Users from API")


@st.cache_data(ttl=300)
def fetch_users():
    """Fetch users from jsonplaceholder API with caching."""
    import requests

    try:
        response = requests.get(
            "https://jsonplaceholder.typicode.com/users", timeout=10
        )
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        st.error(f"API request failed: {e}")
        return []


users = fetch_users()

if users:
    st.success(f"Loaded **{len(users)}** users from API")
else:
    st.warning("No users loaded")

st.divider()

# ============================================================================
# Part 3 — Display as DataFrame
# ============================================================================

st.header("Part 3 — Display as DataFrame")

if users:
    df = pd.DataFrame(
        [
            {
                "ID": u["id"],
                "Name": u["name"],
                "Username": u["username"],
                "Email": u["email"],
                "City": u["address"]["city"],
            }
            for u in users
        ]
    )

    # Filter by city
    cities = ["All"] + sorted(df["City"].unique().tolist())
    selected_city = st.selectbox("Filter by City", cities)

    if selected_city != "All":
        df = df[df["City"] == selected_city]

    st.dataframe(df, use_container_width=True, hide_index=True)
    st.write(f"Showing **{len(df)}** users")

st.divider()

# ============================================================================
# Part 4 — Nested Data Extraction
# ============================================================================

st.header("Part 4 — Company Data & City Distribution")

if users:
    companies = pd.DataFrame(
        [
            {
                "Name": u["name"],
                "Company": u["company"]["name"],
                "Catch Phrase": u["company"]["catchPhrase"],
            }
            for u in users
        ]
    )

    st.subheader("Company Information")
    st.dataframe(companies, use_container_width=True, hide_index=True)

    # City distribution chart
    city_counts = df["City"].value_counts()
    st.subheader("Users per City")
    st.bar_chart(city_counts)

st.divider()

# ============================================================================
# Part 5 — Full User Directory App (BONUS)
# ============================================================================

st.header("Part 5 — User Directory (Bonus)")

if users:
    search = st.text_input("🔍 Search by name", placeholder="Type a name...")
    all_cities = sorted(set(u["address"]["city"] for u in users))
    filter_city = st.selectbox("Filter by city", ["All"] + all_cities)

    filtered_users = users

    if search:
        filtered_users = [
            u for u in filtered_users if search.lower() in u["name"].lower()
        ]

    if filter_city != "All":
        filtered_users = [
            u for u in filtered_users if u["address"]["city"] == filter_city
        ]

    st.write(f"**{len(filtered_users)}** users found")

    for user in filtered_users:
        with st.expander(f"👤 {user['name']} ({user['username']})"):
            col1, col2 = st.columns(2)
            with col1:
                st.write(f"**Email:** {user['email']}")
                st.write(f"**Phone:** {user['phone']}")
                st.write(f"**City:** {user['address']['city']}")
            with col2:
                st.write(f"**Company:** {user['company']['name']}")
                st.write(f"**Catch Phrase:** {user['company']['catchPhrase']}")
                st.write(f"**Website:** {user['website']}")

st.divider()
st.caption("Solution: Exercise 09 — API Connectors · Module 09")

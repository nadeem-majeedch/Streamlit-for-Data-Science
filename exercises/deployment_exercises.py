"""
Deployment Exercises — Module 15
================================
Practice preparing Streamlit apps for deployment.

These exercises focus on deployment preparation, debugging,
and verification — NOT on running the app itself.

Complete each exercise by modifying the code as instructed.
Run `python exercises/deployment_exercises.py` to verify your answers.
"""

import os
import sys
from pathlib import Path


def check_file_exists(filepath: str) -> bool:
    """Check if a file exists."""
    return Path(filepath).exists()


def check_file_contains(filepath: str, required_content: list[str]) -> list[str]:
    """Check if a file contains required strings. Returns missing items."""
    if not check_file_exists(filepath):
        return [f"File '{filepath}' does not exist"]
    
    with open(filepath, 'r') as f:
        content = f.read()
    
    missing = []
    for item in required_content:
        if item not in content:
            missing.append(f"'{item}' not found in {filepath}")
    return missing


def check_file_not_contains(filepath: str, forbidden_content: list[str]) -> list[str]:
    """Check if a file does NOT contain forbidden strings. Returns found items."""
    if not check_file_exists(filepath):
        return []
    
    with open(filepath, 'r') as f:
        content = f.read()
    
    found = []
    for item in forbidden_content:
        if item in content:
            found.append(f"'{item}' found in {filepath} (should be removed!)")
    return found


# ─── Exercise 1: requirements.txt ───
def exercise_1_requirements():
    """
    Exercise 1: Create a proper requirements.txt
    
    Create a requirements.txt file that includes:
    - streamlit (with version >= 1.44.0)
    - pandas (with version >= 2.0.0)
    - numpy (with version >= 1.24.0)
    
    The file should NOT include:
    - jupyter
    - ipython
    - matplotlib (unless your app uses it)
    
    Create the file at: requirements_deploy_ex1.txt
    """
    print("\n" + "=" * 60)
    print("EXERCISE 1: requirements.txt")
    print("=" * 60)
    
    filepath = "requirements_deploy_ex1.txt"
    
    if not check_file_exists(filepath):
        print(f"❌ Create '{filepath}' with proper dependencies")
        print("   Hint: echo 'streamlit>=1.44.0' > requirements_deploy_ex1.txt")
        return False
    
    errors = []
    errors.extend(check_file_not_contains(filepath, ["jupyter", "ipython"]))
    errors.extend(check_file_contains(filepath, ["streamlit", "pandas", "numpy"]))
    
    if errors:
        for err in errors:
            print(f"  ❌ {err}")
        return False
    
    print("  ✅ requirements.txt is properly configured")
    return True


# ─── Exercise 2: .gitignore ───
def exercise_2_gitignore():
    """
    Exercise 2: Create a proper .gitignore
    
    Create a .gitignore that includes:
    - __pycache__/
    - .venv/
    - .streamlit/secrets.toml
    - *.pyc
    
    Create the file at: .gitignore_deploy_ex2
    """
    print("\n" + "=" * 60)
    print("EXERCISE 2: .gitignore")
    print("=" * 60)
    
    filepath = ".gitignore_deploy_ex2"
    
    if not check_file_exists(filepath):
        print(f"❌ Create '{filepath}' with proper ignore patterns")
        return False
    
    required = ["__pycache__", ".venv", "secrets.toml"]
    errors = check_file_contains(filepath, required)
    
    if errors:
        for err in errors:
            print(f"  ❌ {err}")
        return False
    
    print("  ✅ .gitignore is properly configured")
    return True


# ─── Exercise 3: Secure Code ───
def exercise_3_secure_code():
    """
    Exercise 3: Fix insecure code
    
    The following code has security issues. Fix them:
    - Hardcoded API key
    - SQL injection vulnerability
    - No input validation
    
    Create a file at: secure_app_deploy_ex3.py with the fixed version.
    """
    print("\n" + "=" * 60)
    print("EXERCISE 3: Secure Code")
    print("=" * 60)
    
    filepath = "secure_app_deploy_ex3.py"
    
    if not check_file_exists(filepath):
        print(f"❌ Create '{filepath}' with secure code")
        print("   Fix: hardcoded secrets, SQL injection, input validation")
        return False
    
    # Check for insecure patterns
    insecure = check_file_not_contains(filepath, [
        "sk-",           # Hardcoded API keys
        "password123",   # Hardcoded passwords
        "f\"SELECT",     # f-string SQL (injection risk)
        "f'SELECT",      # f-string SQL (injection risk)
    ])
    
    if insecure:
        for item in insecure:
            print(f"  ❌ {item}")
        return False
    
    print("  ✅ Code follows security best practices")
    return True


# ─── Exercise 4: Deployment Preparation ───
def exercise_4_deployment_prep():
    """
    Exercise 4: Verify deployment readiness
    
    Check that these files exist and are properly configured:
    - apps/deployable_app/app.py
    - apps/deployable_app/requirements.txt
    - apps/deployable_app/README.md
    """
    print("\n" + "=" * 60)
    print("EXERCISE 4: Deployment Readiness")
    print("=" * 60)
    
    required_files = [
        "apps/deployable_app/app.py",
        "apps/deployable_app/requirements.txt",
    ]
    
    all_ok = True
    for f in required_files:
        if check_file_exists(f):
            print(f"  ✅ {f} exists")
        else:
            print(f"  ❌ {f} missing")
            all_ok = False
    
    # Check app.py has key elements
    app_path = "apps/deployable_app/app.py"
    if check_file_exists(app_path):
        errors = check_file_contains(app_path, [
            "st.set_page_config",
            "def main",
            "if __name__",
        ])
        if errors:
            for err in errors:
                print(f"  ❌ {err}")
            all_ok = False
        else:
            print("  ✅ app.py has proper structure")
    
    return all_ok


# ─── Exercise 5: Debug a Broken App ───
def exercise_5_debugging():
    """
    Exercise 5: Find and fix deployment issues
    
    The following code has deployment problems. Create a fixed version
    at: fixed_app_deploy_ex5.py
    
    Issues to fix:
    1. Uses absolute file path
    2. Missing error handling
    3. No caching for expensive computation
    4. st.set_page_config() is not the first Streamlit call
    """
    print("\n" + "=" * 60)
    print("EXERCISE 5: Debug Deployment Issues")
    print("=" * 60)
    
    filepath = "fixed_app_deploy_ex5.py"
    
    if not check_file_exists(filepath):
        print(f"❌ Create '{filepath}' with fixed deployment issues")
        return False
    
    issues_found = []
    
    # Check for absolute paths
    with open(filepath, 'r') as f:
        content = f.read()
    
    if "/Users/" in content or "/home/" in content or "C:\\" in content:
        issues_found.append("Contains absolute file path")
    
    if "st.set_page_config" in content:
        # Check it's near the top (first few lines after imports)
        lines = content.split('\n')
        config_line = None
        first_streamlit_call = None
        for i, line in enumerate(lines):
            if 'st.set_page_config' in line and config_line is None:
                config_line = i
            if line.strip().startswith('st.') and first_streamlit_call is None:
                first_streamlit_call = i
        
        if config_line and first_streamlit_call:
            if config_line > first_streamlit_call + 5:
                issues_found.append("st.set_page_config() should be the first Streamlit call")
    
    if "@st.cache_data" not in content and "@st.cache_resource" not in content:
        if "def " in content:
            issues_found.append("No caching decorators found (add @st.cache_data or @st.cache_resource)")
    
    if issues_found:
        for issue in issues_found:
            print(f"  ⚠️  {issue}")
        return False
    
    print("  ✅ App is properly fixed for deployment")
    return True


# ─── Run All Exercises ───
def main():
    print("🚀 Deployment Exercises — Module 15")
    print("=" * 60)
    print("Complete each exercise by creating the required files.")
    print("Run this script to check your answers.\n")
    
    results = {
        "Exercise 1: requirements.txt": exercise_1_requirements(),
        "Exercise 2: .gitignore": exercise_2_gitignore(),
        "Exercise 3: Secure Code": exercise_3_secure_code(),
        "Exercise 4: Deployment Prep": exercise_4_deployment_prep(),
        "Exercise 5: Debugging": exercise_5_debugging(),
    }
    
    print("\n" + "=" * 60)
    print("RESULTS")
    print("=" * 60)
    
    passed = sum(1 for v in results.values() if v)
    total = len(results)
    
    for name, result in results.items():
        status = "✅" if result else "❌"
        print(f"  {status} {name}")
    
    print(f"\n  Score: {passed}/{total}")
    
    if passed == total:
        print("\n🎉 All exercises passed! You're ready for deployment.")
    else:
        print("\n📚 Keep working on the remaining exercises.")
        print("   Review the deployment guide for help:")
        print("   readings/deployment_guide.md")
    
    return passed == total


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)

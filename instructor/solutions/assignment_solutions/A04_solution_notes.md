# A04 — ML Production Application: Solution Notes

> **👩‍🏫 Instructor Reference**
> *Architecture, key implementation, grading breakdown, and common errors.*

---

## Expected Architecture

```
assignments/A04/
├── app.py                # Entry point with navigation
├── config.py             # MODEL_PATH, FEATURE_NAMES, CLASS_NAMES
├── model_utils.py        # train_model(), load_model(), predict()
├── data_processing.py    # preprocess_input(), validate_features()
├── components.py         # Reusable UI components
├── security.py           # sanitize_input(), check_file_type()
├── models/               # Saved model artifacts (gitignored)
│   └── .gitkeep
├── tests/
│   ├── __init__.py
│   ├── test_model_utils.py
│   ├── test_processing.py
│   └── test_app.py
├── requirements.txt
├── .gitignore
├── README.md
└── screenshots/
```

---

## Key Implementation Patterns

### model_utils.py
```python
import joblib
import numpy as np
from pathlib import Path

MODEL_DIR = Path("models")

def train_model():
    """Train and save model artifacts. Run once."""
    from sklearn.datasets import load_wine
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.model_selection import train_test_split
    from sklearn.preprocessing import StandardScaler

    data = load_wine()
    X_train, X_test, y_train, y_test = train_test_split(
        data.data, data.target, test_size=0.2, random_state=42
    )

    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train_scaled, y_train)

    accuracy = model.score(X_test_scaled, y_test)

    MODEL_DIR.mkdir(exist_ok=True)
    joblib.dump(model, MODEL_DIR / "model.joblib")
    joblib.dump(scaler, MODEL_DIR / "scaler.joblib")
    joblib.dump({
        "feature_names": list(data.feature_names),
        "class_names": list(data.target_names),
        "accuracy": accuracy,
        "n_features": len(data.feature_names),
    }, MODEL_DIR / "meta.joblib")

    return model, scaler, {"accuracy": accuracy}

@st.cache_resource
def load_model():
    """Load cached model, train if not found."""
    model_path = MODEL_DIR / "model.joblib"
    if not model_path.exists():
        return train_model()
    model = joblib.load(MODEL_DIR / "model.joblib")
    scaler = joblib.load(MODEL_DIR / "scaler.joblib")
    meta = joblib.load(MODEL_DIR / "meta.joblib")
    return model, scaler, meta

def predict(model, scaler, features):
    """Make prediction with preprocessing."""
    features_scaled = scaler.transform(features)
    prediction = model.predict(features_scaled)[0]
    probabilities = model.predict_proba(features_scaled)[0]
    return prediction, probabilities
```

### data_processing.py
```python
import numpy as np

def validate_features(features: list, feature_names: list) -> list:
    """Validate input features. Returns list of error messages."""
    errors = []
    if len(features) != len(feature_names):
        errors.append(f"Expected {len(feature_names)} features, got {len(features)}")
    for i, (val, name) in enumerate(zip(features, feature_names)):
        if val is None or (isinstance(val, float) and np.isnan(val)):
            errors.append(f"{name} cannot be empty")
    return errors

def preprocess_input(raw_features: list, feature_names: list) -> np.ndarray:
    """Convert raw input to model-ready array."""
    return np.array([[float(f) for f in raw_features]])
```

### security.py
```python
import re

def sanitize_text(text: str) -> str:
    """Remove potentially dangerous characters."""
    return re.sub(r'[<>&\'";\\]', '', text)

def validate_file_upload(uploaded_file, max_size_mb=10) -> tuple:
    """Validate uploaded file. Returns (is_valid, message)."""
    if uploaded_file is None:
        return False, "No file uploaded"
    if uploaded_file.size > max_size_mb * 1024 * 1024:
        return False, f"File too large (max {max_size_mb}MB)"
    if not uploaded_file.name.endswith('.csv'):
        return False, "Only CSV files accepted"
    return True, "OK"
```

### tests/test_model_utils.py
```python
import pytest
import numpy as np

def test_model_loads():
    from model_utils import load_model
    model, scaler, meta = load_model()
    assert model is not None
    assert scaler is not None
    assert "accuracy" in meta

def test_prediction():
    from model_utils import load_model, predict
    model, scaler, meta = load_model()
    features = np.random.randn(1, meta["n_features"])
    pred, probs = predict(model, scaler, features)
    assert pred in range(len(meta["class_names"]))
    assert abs(sum(probs) - 1.0) < 0.01

def test_preprocessing_consistency():
    from model_utils import load_model
    model, scaler, meta = load_model()
    features = np.random.randn(5, meta["n_features"])
    scaled = scaler.transform(features)
    assert scaled.shape == features.shape
    # Mean should be approximately 0 after scaling
    assert abs(scaled.mean()) < 0.5
```

### tests/test_app.py
```python
from streamlit.testing.v1 import AppTest

def test_app_loads():
    at = AppTest.from_file("app.py")
    at.run()
    assert not at.exception

def test_prediction_flow():
    at = AppTest.from_file("app.py")
    at.run()
    # Interact with sliders or inputs
    # Assert prediction appears
    assert at.success or at.info  # No errors
```

---

## Grading Breakdown by Task

### Task 1: Model Training & Persistence (15 marks)
| Criteria | Points |
|----------|--------|
| Train on real dataset | 3 |
| Save with joblib | 3 |
| Separate training function | 2 |
| @st.cache_resource for loading | 3 |
| Display model metadata | 2 |
| Handle missing model gracefully | 2 |

### Task 2: Preprocessing & Input UI (15 marks)
| Criteria | Points |
|----------|--------|
| Input widgets match feature types | 4 |
| Correct min/max for sliders | 3 |
| Categorical selectbox correct | 3 |
| Input validation with messages | 3 |
| Preprocessing matches training | 2 |

### Task 3: Prediction & Confidence (15 marks)
| Criteria | Points |
|----------|--------|
| Single prediction with result | 3 |
| Class probabilities displayed | 4 |
| Metric or success display | 2 |
| Prediction history in session_state | 3 |
| Clear result formatting | 3 |

### Task 6: Security (10 marks)
| Criteria | Points |
|----------|--------|
| No hardcoded secrets | 2 |
| Input validation | 2 |
| .gitignore correct | 2 |
| README secrets documentation | 1 |
| Input length limits | 1 |
| Safe file handling | 2 |

### Task 7: Testing (10 marks)
| Criteria | Points |
|----------|--------|
| Unit test for model loading | 2 |
| Unit test for preprocessing | 2 |
| AppTest for app loading | 2 |
| AppTest for widget interactions | 2 |
| All tests pass | 2 |

### Task 8: Deployment (10 marks)
| Criteria | Points |
|----------|--------|
| Deployed on Community Cloud | 3 |
| All features work | 2 |
| No hardcoded paths/secrets | 2 |
| requirements.txt correct | 1 |
| URL in README | 2 |

---

## Critical Issues (Automatic Deductions)

| Issue | Deduction |
|-------|-----------|
| Not deployed | -10 marks |
| Hardcoded secrets in source | -5 marks |
| SQL injection vulnerability | -5 marks |
| No tests | -10 marks |
| Model trained on every rerun | -5 marks |
| Preprocessing mismatch | -5 marks |
| Missing requirements.txt | -5 marks |

---

## Common Class-Wide Issues

1. **Training on every rerun** — Most common ML mistake
   ```python
   # WRONG: Trains on every page load
   model = RandomForestClassifier().fit(X, y)
   
   # RIGHT: Train once, save, load with caching
   @st.cache_resource
   def load_model():
       if not model_path.exists():
           train_and_save()
       return joblib.load(model_path)
   ```

2. **Preprocessing mismatch** — Scaler from training not used in inference
   ```python
   # WRONG: New scaler during inference
   scaler = StandardScaler()
   X_scaled = scaler.fit_transform(features)  # WRONG!
   
   # RIGHT: Use saved scaler
   X_scaled = scaler.transform(features)  # Only transform!
   ```

3. **No input validation** — App crashes on NaN or out-of-range values

4. **Missing tests** — 10 marks automatically lost

5. **Not deployed** — 10 marks automatically lost

---

## Grading Strategy

1. **Check deployment first** — Is the app live and working?
2. **Check tests** — Run `pytest tests/ -v`, do they pass?
3. **Run the app locally** — Does it start without errors?
4. **Test single prediction** — Does it work with valid input?
5. **Test invalid input** — Does it handle errors gracefully?
6. **Check code structure** — Are files properly separated?
7. **Check security** — No hardcoded secrets?
8. **Review README** — Complete documentation?

**Estimated grading time:** 20-30 minutes per student

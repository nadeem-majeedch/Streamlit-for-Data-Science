# Pre-Course Assessment

> **📝 Placement Assessment · Before Module 01**
> *Evaluate readiness for the Streamlit for Data Science course.*
> ⏱ Time: 30 minutes · 📊 Points: 50

---

## Purpose

This assessment determines if you have the prerequisite knowledge for this course. It covers Python, Pandas, NumPy, Matplotlib, basic ML concepts, and Git. **It does not count toward your grade** — it helps you and your instructor identify areas to review.

---

## Part A: Python Fundamentals (10 points)

### A1. (1 pt) What is the output of this code?

```python
x = [1, 2, 3]
y = x
y.append(4)
print(len(x))
```

(a) 3
(b) 4
(c) Error
(d) [1, 2, 3, 4]

---

### A2. (1 pt) Which correctly defines a function with a default argument?

(a) `def greet(name="World"):`
(b) `def greet(name = "World"):`
(c) `def greet("World"):`
(d) `function greet(name="World"):`

---

### A3. (2 pts) Write a list comprehension that creates a list of squares for numbers 0–9.

---

### A4. (2 pts) What is the difference between a **list** and a **tuple** in Python?

---

### A5. (2 pts) What does this code output?

```python
data = {"a": 1, "b": 2, "c": 3}
result = {v: k for k, v in data.items()}
print(result)
```

---

### A6. (2 pts) Write a try/except block that attempts to convert a string to an integer and prints "Invalid number" if it fails.

---

## Part B: Pandas (10 points)

### B1. (1 pt) Which method reads a CSV file into a DataFrame?

(a) `pd.load_csv()`
(b) `pd.read_csv()`
(c) `pd.open_csv()`
(d) `pd.import_csv()`

---

### B2. (1 pt) What does `df.groupby("col").mean()` return?

(a) The mean of all columns
(b) The mean of the "col" column
(c) A DataFrame with mean values grouped by unique values in "col"
(d) A list of means

---

### B3. (2 pts) Given a DataFrame `df` with columns "Name", "Age", "Score":

Write the code to:
1. Filter rows where Age > 20
2. Select only the "Name" and "Score" columns

---

### B4. (2 pts) What is the difference between `df.loc[]` and `df.iloc[]`?

---

### B5. (2 pts) Write code to create a new column "Grade" that is "A" if Score >= 90, "B" if Score >= 80, else "C".

---

### B6. (2 pts) What does `df.isnull().sum()` return? When would you use it?

---

## Part C: NumPy (5 points)

### C1. (1 pt) What is the shape of the array created by `np.zeros((3, 4))`?

(a) (3,)
(b) (4, 3)
(c) (3, 4)
(d) (12,)

---

### C2. (2 pts) What is the difference between `np.array([1,2,3]) * 2` and `np.array([1,2,3]) + 2`?

---

### C3. (2 pts) Write code to generate a 5×5 array of random numbers between 0 and 1, then compute the mean of each row.

---

## Part D: Matplotlib (5 points)

### D1. (1 pt) Which function creates a new Matplotlib figure?

(a) `plt.figure()`
(b) `plt.plot()`
(c) `plt.show()`
(d) `plt.new()`

---

### D2. (2 pts) What is the difference between `plt.plot()` and `plt.scatter()`?

---

### D3. (2 pts) Write code to create a bar chart with categories ["A", "B", "C"] and values [10, 25, 15].

---

## Part E: Machine Learning Basics (10 points)

### E1. (1 pt) What is the purpose of a **train/test split**?

(a) To make training faster
(b) To evaluate model performance on unseen data
(c) To reduce overfitting
(d) To increase accuracy

---

### E2. (1 pt) In `model.fit(X_train, y_train)`, what are X_train and y_train?

(a) The full dataset
(b) Features and labels for training
(c) Model parameters
(d) Evaluation metrics

---

### E3. (2 pts) Explain the difference between **classification** and **regression**. Give one example of each.

---

### E4. (2 pts) What is **overfitting** and how can you detect it?

---

### E5. (2 pts) What does `StandardScaler` do? Why is it important?

---

### E6. (2 pts) In scikit-learn, what is a **Pipeline** and why is it useful?

---

## Part F: Git & Command Line (5 points)

### F1. (1 pt) What command stages all changes for commit?

(a) `git add .`
(b) `git commit -a`
(c) `git push`
(d) `git status`

---

### F2. (1 pt) What is the difference between `git pull` and `git fetch`?

---

### F3. (1 pt) What does `git branch -a` show?

---

### F4. (2 pts) You made a commit but want to undo it without losing changes. What command do you use?

---

## Part G: Environment & Setup (5 points)

### G1. (1 pt) What command creates a virtual environment named `.venv`?

(a) `python create venv .venv`
(b) `python -m venv .venv`
(c) `pip install venv .venv`
(d) `conda create .venv`

---

### G2. (1 pt) How do you activate a virtual environment on macOS/Linux?

(a) `activate .venv`
(b) `.venv/activate`
(c) `source .venv/bin/activate`
(d) `python .venv/activate`

---

### G3. (1 pt) What does `pip install -r requirements.txt` do?

---

### G4. (2 pts) Explain why you should use a virtual environment instead of installing packages globally.

---

## Answer Key

> ⚠️ **Instructor copy — do not distribute to students**

<details>
<summary>Click to view answer key</summary>

### Part A: Python

| Q | Answer | Explanation |
|---|--------|-------------|
| A1 | **(b) 4** | Lists are mutable; `y = x` creates a reference, not a copy. Both point to the same list. |
| A2 | **(a)** | Default argument assigned with `=` in function signature. |
| A3 | `squares = [x**2 for x in range(10)]` | List comprehension syntax: `[expression for item in iterable]` |
| A4 | Lists are mutable (can be changed after creation), tuples are immutable. Lists use `[]`, tuples use `()`. |
| A5 | `{1: 'a', 2: 'b', 3: 'c'}` | Dictionary comprehension swaps keys and values. |
| A6 | `try: n = int("abc") except ValueError: print("Invalid number")` | |

### Part B: Pandas

| Q | Answer | Explanation |
|---|--------|-------------|
| B1 | **(b) `pd.read_csv()`** | |
| B2 | **(c)** | GroupBy creates groups by unique values, then computes mean for each group. |
| B3 | `df[df["Age"] > 20][["Name", "Score"]]` | Boolean indexing + column selection |
| B4 | `loc[]` uses labels/names; `iloc[]` uses integer positions (0-indexed). |
| B5 | `df["Grade"] = np.where(df["Score"] >= 90, "A", np.where(df["Score"] >= 80, "B", "C"))` |
| B6 | Returns a Series with null count per column. Used to assess data quality and decide on cleaning strategy. |

### Part C: NumPy

| Q | Answer | Explanation |
|---|--------|-------------|
| C1 | **(c) (3, 4)** | 3 rows, 4 columns |
| C2 | `* 2` multiplies each element by 2 (element-wise). `+ 2` adds 2 to each element. Both are element-wise operations. |
| C3 | `arr = np.random.rand(5, 5); row_means = arr.mean(axis=1)` |

### Part D: Matplotlib

| Q | Answer | Explanation |
|---|--------|-------------|
| D1 | **(a) `plt.figure()`** | |
| D2 | `plt.plot()` connects points with lines (for trends). `plt.scatter()` shows individual points (for relationships). |
| D3 | `plt.bar(["A", "B", "C"], [10, 25, 15]); plt.show()` |

### Part E: ML

| Q | Answer | Explanation |
|---|--------|-------------|
| E1 | **(b)** | Train/test split evaluates generalization to unseen data. |
| E2 | **(b)** | X_train = feature matrix, y_train = target labels. |
| E3 | Classification predicts discrete categories (e.g., spam/not spam). Regression predicts continuous values (e.g., house price). |
| E4 | Overfitting = model learns noise in training data, performs poorly on new data. Detected when training accuracy >> test accuracy. |
| E5 | StandardScaler standardizes features to mean=0, std=1. Important because many algorithms (SVM, KNN, neural nets) are sensitive to feature scales. |
| E6 | Pipeline chains preprocessing + model into one object. Prevents data leakage (scaler fit only on training data) and simplifies deployment. |

### Part F: Git

| Q | Answer | Explanation |
|---|--------|-------------|
| F1 | **(a) `git add .`** | |
| F2 | `git fetch` downloads changes but doesn't merge. `git pull` fetches AND merges. |
| F3 | Shows all branches: local and remote. |
| F4 | `git reset --soft HEAD~1` — undoes last commit but keeps changes staged. |

### Part G: Environment

| Q | Answer | Explanation |
|---|--------|-------------|
| G1 | **(b) `python -m venv .venv`** | |
| G2 | **(c) `source .venv/bin/activate`** | |
| G3 | Installs all packages listed in the requirements.txt file. |
| G4 | Prevents dependency conflicts between projects, ensures reproducibility, avoids permission issues with system Python. |

</details>

---

## Scoring Guide

| Score | Recommendation |
|-------|----------------|
| 45–50 | Excellent — ready for the course |
| 35–44 | Good — review weak areas before starting |
| 25–34 | Adequate — spend extra time on prerequisites |
| Below 25 | Needs preparation — review Python, Pandas, and Git fundamentals first |

---

## Related Materials

- 📖 Reading: [Streamlit Introduction](../readings/01_streamlit_introduction.md)
- 📓 Notebook: [01 — Introduction](../notebooks/01_Streamlit_Introduction.ipynb)
- 📋 Curriculum: [docs/curriculum.md](../docs/curriculum.md)

# 🐍 Python Cheat Sheet

A concise cheat sheet covering core Python concepts and syntax. Great for quick reference or as a beginner's guide.

---

## 🔤 Variables & Data Types

```python
x = 10               # int
name = "Alice"       # str
price = 19.99        # float
is_valid = True      # bool
```

---
# 🐍 Python Identifier Rules

Identifiers in Python are names used to identify variables, functions, classes, modules, and other objects. Follow these rules to ensure your identifiers are valid and follow Python conventions.

---

## ✅ Rules for Valid Identifiers

1. **Allowed Characters**  
   - Letters: `A–Z`, `a–z`  
   - Digits: `0–9`  
   - Underscore: `_`

2. **Must Start With**  
   - A letter (`A–Z`, `a–z`) **or** an underscore (`_`)  
   - ❌ Invalid: `1value`, `@user`  
   - ✅ Valid: `_temp`, `user1`

3. **Cannot Be a Keyword**  
   - Identifiers cannot be Python **reserved keywords** (like `class`, `def`, `if`, `else`, etc.)  
   - To see all Python keywords:  
     ```python
     import keyword  
     print(keyword.kwlist)
     ```

4. **Case Sensitive**  
   - `Data` and `data` are different identifiers.

5. **No Special Characters**  
   - Only `_` is allowed.  
   - ❌ Invalid: `email@id`, `user-name`, `cost$price`

6. **No Spaces Allowed**  
   - ❌ Invalid: `my var`  
   - ✅ Valid: `my_var`

---

## ✨ Best Practices (Recommended)

- Use **descriptive names**:  
  ✅ `student_name`, `calculate_total()`

- Use **snake_case** for variables and functions:  
  ✅ `user_input`, `get_data()`

- Use **PascalCase** for class names:  
  ✅ `CustomerInfo`, `DataManager`

- Avoid one-letter names except for counters (`i`, `j`)

- Avoid starting identifiers with double underscores unless defining special methods (e.g., `__init__`)

---

> ✅ Following these rules and conventions improves code readability, consistency, and maintainability across Python projects.
---

## 📦 Data Structures

### 🧺 Lists
```python
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
fruits[1] = "kiwi"
```

### 🧊 Tuples
```python
coords = (10, 20)
x, y = coords
```

### 🗂️ Dictionaries
```python
person = {"name": "Alice", "age": 25}
person["age"] = 26
```

### 🧮 Sets
```python
unique_nums = {1, 2, 3, 2}
unique_nums.add(4)
```

---

## 🔁 Conditionals & Loops

### If-Else
```python
if x > 0:
    print("Positive")
elif x == 0:
    print("Zero")
else:
    print("Negative")
```

### For Loop
```python
for i in range(5):
    print(i)
```

### While Loop
```python
count = 0
while count < 5:
    print(count)
    count += 1
```

---

## 🧰 Functions

```python
def greet(name):
    return f"Hello, {name}"

print(greet("Alice"))
```

---

## 📎 List Comprehensions

```python
squares = [x**2 for x in range(5)]
```

---

## 📁 File Handling

```python
with open("file.txt", "r") as f:
    content = f.read()
```

---

## 🧪 Exception Handling

```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero.")
```

---

## 📦 Common Modules

```python
import math
print(math.sqrt(16))

import random
print(random.choice([1, 2, 3]))
```

---

## 🐼 Pandas & 📊 NumPy (Basics)

```python
import pandas as pd
import numpy as np

df = pd.DataFrame({'Name': ['Alice', 'Bob'], 'Age': [25, 30]})
arr = np.array([1, 2, 3])
```

---

> 📌 Save this repo ⭐ and share with fellow Python learners!

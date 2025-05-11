
# 🗂️ Python Dictionary Methods Cheat Sheet

Dictionaries are unordered collections of key-value pairs in Python.

---

## 🧱 Creating Dictionaries

```python
d1 = {"name": "Alice", "age": 25}
d2 = dict(name="Bob", age=30)
empty = {}
```

---

## 🎯 Key Characteristics

- **Key-value pairs**
- **Keys must be unique and immutable**
- **Values can be any type**
- **Unordered in Python < 3.7 (ordered from 3.7+)**

---

## 🛠️ Common Dictionary Methods

| Method                | Description                                      | Example                              |
|------------------------|--------------------------------------------------|--------------------------------------|
| `get(key[, default])`  | Get value for key; return `default` if missing  | `d.get("age", 0)`                     |
| `keys()`              | Return all keys                                  | `d.keys()`                            |
| `values()`            | Return all values                                | `d.values()`                          |
| `items()`             | Return all key-value pairs as tuples             | `d.items()`                           |
| `update(other_dict)`  | Update with key-value pairs from another dict    | `d.update({"city": "Delhi"})`        |
| `pop(key[, default])` | Remove key and return its value                  | `d.pop("age")`                        |
| `popitem()`           | Remove and return last inserted key-value pair   | `d.popitem()`                         |
| `setdefault(key[, default])` | Get value or insert if key is missing    | `d.setdefault("gender", "female")`   |
| `clear()`             | Remove all items                                 | `d.clear()`                           |
| `copy()`              | Shallow copy of the dictionary                   | `new_d = d.copy()`                    |
| `fromkeys(keys[, v])` | Create new dict from given keys and value        | `dict.fromkeys(["a", "b"], 0)`        |

---

## 🔄 Accessing and Modifying

```python
d = {"a": 1, "b": 2}
d["a"]          # → 1
d["b"] = 3      # Modify value
d["c"] = 4      # Add new key-value pair
```

---

## 🧪 Iteration

```python
for key in d:
    print(key, d[key])

for key, value in d.items():
    print(f"{key} → {value}")
```

---

## 🚫 KeyError Example

```python
value = d["missing"]  # ❌ Raises KeyError if key not found
value = d.get("missing", "default")  # ✅ Safer
```

---

## 📘 More Python Resources

- [Python Dictionaries - Official Docs](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)
- [W3Schools Dictionary Tutorial](https://www.w3schools.com/python/python_dictionaries.asp)

---

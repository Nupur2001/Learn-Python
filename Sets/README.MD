
# 🧮 Python Set Methods Cheat Sheet

Sets are unordered, unindexed collections of unique elements in Python.

---

## 🔧 Creating Sets

```python
s1 = {1, 2, 3}
s2 = set([4, 5, 6])
empty = set()  # NOT empty = {} (this creates a dict)
```

---

## 🚩 Key Characteristics

- **Unordered** → No guaranteed order
- **No duplicates** → `{1, 1, 2}` becomes `{1, 2}`
- **Mutable** → Can add/remove items
- **Set elements must be immutable**

---

## 🛠️ Set Methods

| Method              | Description                                       | Example                            |
|---------------------|---------------------------------------------------|------------------------------------|
| `add(x)`            | Add element `x`                                   | `s.add(5)`                          |
| `update(iterable)`  | Add multiple elements                             | `s.update([6, 7])`                  |
| `remove(x)`         | Remove `x`; raises error if not present           | `s.remove(2)`                       |
| `discard(x)`        | Remove `x`; does nothing if not present           | `s.discard(10)`                     |
| `pop()`             | Remove and return an arbitrary element            | `s.pop()`                           |
| `clear()`           | Remove all elements                               | `s.clear()`                         |
| `copy()`            | Shallow copy of the set                           | `s2 = s.copy()`                     |

---

## 🔄 Set Operations

| Operation           | Description                          | Example                            |
|---------------------|--------------------------------------|------------------------------------|
| `union()` / `|`     | Combine elements                     | `s1.union(s2)` or `s1 | s2`         |
| `intersection()` / `&` | Common elements                  | `s1 & s2`                           |
| `difference()` / `-`| Elements in `s1` but not in `s2`     | `s1 - s2`                           |
| `symmetric_difference()` / `^` | In either set, not both | `s1 ^ s2`                           |
| `issubset()`        | Check if set is subset               | `s1.issubset(s2)`                   |
| `issuperset()`      | Check if set is superset             | `s1.issuperset(s2)`                 |
| `isdisjoint()`      | Check if sets have no common items   | `s1.isdisjoint(s2)`                 |

---

## 🧪 Examples

```python
a = {1, 2, 3}
b = {3, 4, 5}

a | b  # {1, 2, 3, 4, 5}
a & b  # {3}
a - b  # {1, 2}
a ^ b  # {1, 2, 4, 5}
```

---

## 📘 More Python Resources

- [Python Sets - Official Docs](https://docs.python.org/3/tutorial/datastructures.html#sets)
- [W3Schools Set Tutorial](https://www.w3schools.com/python/python_sets.asp)

---

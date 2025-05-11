
# 🐍 Python List Methods Cheat Sheet

Quick reference for commonly used list methods in Python.

---

## 📋 Creating a List

```python
my_list = [1, 2, 3]
```

---

## 🔄 Adding Items

| Method              | Description                              | Example                      |
|---------------------|------------------------------------------|------------------------------|
| `append(x)`         | Add item `x` to the end of the list      | `my_list.append(4)`          |
| `insert(i, x)`      | Insert `x` at index `i`                  | `my_list.insert(1, 10)`      |
| `extend(iterable)`  | Add all items from another iterable      | `my_list.extend([5, 6])`     |

---

## ❌ Removing Items

| Method              | Description                              | Example                      |
|---------------------|------------------------------------------|------------------------------|
| `remove(x)`         | Remove first occurrence of `x`           | `my_list.remove(2)`          |
| `pop([i])`          | Remove and return item at index `i`      | `my_list.pop()`              |
| `clear()`           | Remove all items                         | `my_list.clear()`            |

---

## 📍 Finding & Counting

| Method              | Description                              | Example                      |
|---------------------|------------------------------------------|------------------------------|
| `index(x)`          | Return first index of value `x`          | `my_list.index(3)`           |
| `count(x)`          | Count occurrences of value `x`           | `my_list.count(1)`           |

---

## 🔁 Reordering

| Method                    | Description                          | Example                          |
|---------------------------|--------------------------------------|----------------------------------|
| `reverse()`               | Reverse the list in-place            | `my_list.reverse()`              |
| `sort()`                  | Sort list in ascending order         | `my_list.sort()`                 |
| `sort(reverse=True)`      | Sort list in descending order        | `my_list.sort(reverse=True)`     |

---

## 🧬 Copying

| Method              | Description                              | Example                          |
|---------------------|------------------------------------------|----------------------------------|
| `copy()`            | Create a shallow copy of the list        | `new_list = my_list.copy()`      |

---

## 🧪 Code Examples

```python
a = [3, 1, 2]
a.append(4)       # [3, 1, 2, 4]
a.sort()          # [1, 2, 3, 4]
a.pop()           # Returns 4, a becomes [1, 2, 3]
```

---

## 📘 More Python Resources

- [Python Official Docs](https://docs.python.org/3/tutorial/datastructures.html)
- [W3Schools Python Lists](https://www.w3schools.com/python/python_lists.asp)

---

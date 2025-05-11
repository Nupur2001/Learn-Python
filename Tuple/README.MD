
# 📘 Python Tuple Cheat Sheet

Tuples are immutable, ordered sequences in Python. They are often used to store data that shouldn’t be changed.

---

## 🧱 Creating Tuples

```python
t1 = (1, 2, 3)
t2 = tuple([4, 5, 6])
t3 = (7,)        # Single-element tuple (note the comma!)
empty = ()
```

---

## 🎯 Key Characteristics

- **Ordered** → Elements have a defined order
- **Immutable** → Cannot be changed after creation
- **Allows Duplicates** → `(1, 1, 2)` is valid
- **Can contain mixed types** → `(1, "a", 3.5)`

---

## 🧰 Common Tuple Operations

| Operation              | Description                           | Example                      |
|------------------------|---------------------------------------|------------------------------|
| `len(t)`               | Returns number of elements            | `len(t1)` → `3`              |
| `t[i]`                 | Access element at index `i`           | `t1[0]` → `1`                |
| `t[i:j]`               | Slice tuple                           | `t1[1:3]` → `(2, 3)`         |
| `t + t2`               | Concatenate two tuples                | `(1, 2) + (3, 4)` → `(1, 2, 3, 4)` |
| `t * 2`                | Repeat tuple                          | `(1, 2) * 2` → `(1, 2, 1, 2)` |
| `x in t`               | Check membership                      | `2 in t1` → `True`           |

---

## 🔍 Tuple Methods

> Tuples have only **2 built-in methods** due to their immutability:

| Method          | Description                              | Example                      |
|-----------------|------------------------------------------|------------------------------|
| `count(x)`      | Counts occurrences of `x`                | `(1, 2, 1).count(1)` → `2`   |
| `index(x)`      | Returns index of first occurrence of `x` | `(1, 2, 3).index(2)` → `1`   |

---

## 🧪 Tuple Unpacking

```python
a, b, c = (1, 2, 3)  # a=1, b=2, c=3

# Extended unpacking
a, *b = (1, 2, 3, 4) # a=1, b=[2, 3, 4]
```

---

## 🔄 Converting Between Lists and Tuples

```python
list_to_tuple = tuple([1, 2, 3])
tuple_to_list = list((4, 5, 6))
```

---

## 🛑 Tuples Are Immutable

```python
t = (1, 2, 3)
t[0] = 10  # ❌ TypeError
```

---

## 📘 More Python Resources

- [Python Tuples - Official Docs](https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences)
- [W3Schools Tuple Tutorial](https://www.w3schools.com/python/python_tuples.asp)

---

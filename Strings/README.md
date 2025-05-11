# 🧵 Python String Methods Cheatsheet

A quick reference for Python string methods, useful for beginners and pros alike.

---

## 🔤 Basic String Methods

| Method | Description | Example |
|--------|-------------|---------|
| `.lower()` | Converts string to lowercase | `"Hello".lower()` → `'hello'` |
| `.upper()` | Converts string to uppercase | `"Hello".upper()` → `'HELLO'` |
| `.title()` | Capitalizes first letter of each word | `"hello world".title()` → `'Hello World'` |
| `.capitalize()` | Capitalizes first character | `"hello".capitalize()` → `'Hello'` |
| `.strip()` | Removes leading/trailing whitespace | `" hello ".strip()` → `'hello'` |
| `.lstrip()` | Removes leading whitespace | `" hello ".lstrip()` → `'hello '` |
| `.rstrip()` | Removes trailing whitespace | `" hello ".rstrip()` → `' hello'` |

---

## 🔎 Search & Find

| Method | Description | Example |
|--------|-------------|---------|
| `.find(sub)` | Returns lowest index of `sub`, or `-1` | `"hello".find("e")` → `1` |
| `.rfind(sub)` | Returns highest index of `sub` | `"hello hello".rfind("e")` → `9` |
| `.index(sub)` | Like `.find()` but raises `ValueError` if not found | `"hello".index("e")` → `1` |
| `.startswith(sub)` | Checks if string starts with `sub` | `"hello".startswith("he")` → `True` |
| `.endswith(sub)` | Checks if string ends with `sub` | `"hello".endswith("lo")` → `True` |
| `'sub' in str` | Checks if substring exists | `"el" in "hello"` → `True` |

---

## 🔄 Replace & Modify

| Method | Description | Example |
|--------|-------------|---------|
| `.replace(old, new)` | Replace occurrences of `old` with `new` | `"hello".replace("l", "x")` → `'hexxo'` |
| `.split(sep)` | Splits string into list | `"a,b,c".split(",")` → `['a', 'b', 'c']` |
| `.rsplit(sep)` | Splits from the right | `"a,b,c".rsplit(",", 1)` → `['a,b', 'c']` |
| `.join(list)` | Joins list into a string | `",".join(['a', 'b'])` → `'a,b'` |

---

## 📐 Format & Align

| Method | Description | Example |
|--------|-------------|---------|
| `.center(width)` | Centers string | `"hi".center(6)` → `'  hi  '` |
| `.ljust(width)` | Left-aligns string | `"hi".ljust(6)` → `'hi    '` |
| `.rjust(width)` | Right-aligns string | `"hi".rjust(6)` → `'    hi'` |
| `.zfill(width)` | Pads with zeros on the left | `"42".zfill(5)` → `'00042'` |
| `.format()` | Inserts values | `"{} and {}".format("Tea", "Coffee")` → `'Tea and Coffee'` |
| `f"{}"` | f-string formatting | `f"{2+3}"` → `'5'` |

---

## 🧪 Type Checks

| Method | Description | Example |
|--------|-------------|---------|
| `.isalpha()` | Only letters | `"abc".isalpha()` → `True` |
| `.isdigit()` | Only digits | `"123".isdigit()` → `True` |
| `.isalnum()` | Letters and digits | `"abc123".isalnum()` → `True` |
| `.isspace()` | Only whitespace | `" ".isspace()` → `True` |
| `.islower()` | All lowercase | `"abc".islower()` → `True` |
| `.isupper()` | All uppercase | `"ABC".isupper()` → `True` |
| `.istitle()` | Titlecase | `"Hello World".istitle()` → `True` |

---

> 💡 Tip: Combine multiple methods to clean and format user input for validation or storage.

---

## 📎 License

Feel free to copy and share. No attribution required — but always appreciated!


# Lesson 03 — Python Programming: Loops

> **CS50 Harvard** | Python track | Lesson 03  
> Topics: `while` loops, Infinity loops, `for` loops, Escape Characters, Lists, Dictionaries

---

## Table of Contents

1. [The `while` Loop](#1-the-while-loop)
2. [Infinite Loops and `break`](#2-infinite-loops-and-break)
3. [The `for` Loop](#3-the-for-loop)
4. [The `range()` Function](#4-the-range-function)
5. [The `_` Throwaway Variable](#5-the--throwaway-variable)
6. [Escape Characters — `\n` and Friends](#6-escape-characters--n-and-friends)
7. [Lists](#7-lists)
8. [The `len()` Function](#8-the-len-function)
9. [Iterating with Index](#9-iterating-with-index)
10. [Dictionaries](#10-dictionaries)
11. [List of Dictionaries](#11-list-of-dictionaries)
12. [Program Walkthroughs](#12-program-walkthroughs)

---

## 1. The `while` Loop

A `while` loop repeats a block of code **as long as a condition is `True`**. It checks the condition before each iteration.

**Syntax:**

```python
while condition:
    # body — runs repeatedly while condition is True
```

**Example — count down:**

```python
i = 3
while i > 0:
    print("meow")
    i -= 1
# Output:
# meow
# meow
# meow
```

**How it works step by step:**
1. Check `i > 0` → `True` → run body → `i` becomes `2`
2. Check `i > 0` → `True` → run body → `i` becomes `1`
3. Check `i > 0` → `True` → run body → `i` becomes `0`
4. Check `i > 0` → `False` → exit loop

> Always make sure the condition will eventually become `False`, otherwise you create an **infinite loop** (covered next).

---

## 2. Infinite Loops and `break`

An **infinite loop** runs forever because its condition never becomes `False`. The most explicit form uses `while True:`.

```python
while True:
    print("meow")
# This prints "meow" endlessly — never stops on its own
```

Infinite loops are intentional when you need to keep asking for input until the user provides a valid value. Use the `break` keyword to exit the loop from inside the body.

**`break`** immediately stops the loop and jumps to the code after it.

**Example — validate user input:**

```python
while True:
    n = int(input("What is n? "))
    if n > 0:
        break   # exit loop only when n is a positive number
```

**Flow:**
- User enters `-3` → `n > 0` is `False` → loop continues, asks again
- User enters `0` → `n > 0` is `False` → loop continues, asks again
- User enters `5` → `n > 0` is `True` → `break` → loop exits

> This is the recommended pattern for input validation in Python — keep asking until you get what you need.

---

## 3. The `for` Loop

A `for` loop **iterates over a sequence** — a range of numbers, a list, a string, or any iterable. It runs the body once for each item.

**Syntax:**

```python
for variable in sequence:
    # body — runs once per item, variable holds the current item
```

**Example — iterate over a range:**

```python
for i in range(3):
    print(i)
# Output: 0  1  2
```

**Example — iterate over a list:**

```python
students = ["harry", "hermione", "ron"]
for student in students:
    print(student)
# Output:
# harry
# hermione
# ron
```

**`for` vs `while`:**

| | `for` | `while` |
|---|---|---|
| Use when | Number of iterations is known | Number of iterations is unknown |
| Typical use | Iterating over a sequence | Waiting for a condition |
| Risk of infinite loop | No | Yes, if condition is never `False` |

---

## 4. The `range()` Function

`range()` generates a sequence of integers. It is most commonly used with `for` loops.

**Signatures:**

```python
range(stop)              # 0 up to (not including) stop
range(start, stop)       # start up to (not including) stop
range(start, stop, step) # start up to stop, incrementing by step
```

**Examples:**

```python
range(3)        # 0, 1, 2
range(1, 4)     # 1, 2, 3
range(0, 10, 2) # 0, 2, 4, 6, 8
range(5, 0, -1) # 5, 4, 3, 2, 1  (count down)
```

`range()` does not produce a list — it generates numbers on demand. Use `list(range(3))` if you need an actual list.

---

## 5. The `_` Throwaway Variable

When a loop variable is not used inside the body, Python convention is to name it `_` (underscore). This signals to other developers that the value is intentionally ignored.

```python
# We only care about the count (3 times), not the loop index
for _ in range(3):
    print("meow")
```

Using `_` is purely a convention — it works like any variable name, but it clearly communicates intent.

---

## 6. Escape Characters — `\n` and Friends

**Escape characters** are special character sequences beginning with a backslash `\`. They represent characters that cannot be typed directly or that have special meaning inside a string.

| Sequence | Meaning | Result |
|----------|---------|--------|
| `\n` | Newline | Moves to the next line |
| `\t` | Tab | Inserts a horizontal tab |
| `\\` | Backslash | Prints a literal `\` |
| `\"` | Double quote | Prints `"` inside a double-quoted string |
| `\'` | Single quote | Prints `'` inside a single-quoted string |

**`\n` in practice:**

```python
print("meow\nmeow\nmeow")
# Output:
# meow
# meow
# meow
```

**Using `\n` with string multiplication:**

```python
print("meow\n" * 3, end="")
# Output:
# meow
# meow
# meow
```

The `end=""` argument suppresses `print()`'s default trailing newline — without it you would get an extra blank line after the last `meow`.

**Using `end=` to control line endings:**

```python
# Default: print adds \n at the end
print("meow")   # → "meow\n"

# Custom end: no newline
print("meow", end="")  # → "meow"

# Custom end: space separator
print("#", end="")
print("#", end="")
# Output: ##  (on the same line)
```

> See `mario.py` — `print_rows()` uses `end=""` to build a row of `#` characters on a single line.

---

## 7. Lists

A **list** is an ordered, mutable (changeable) sequence of items. Lists can hold any type of value and allow duplicates.

**Defining a list:**

```python
students = ["harry", "hermione", "ron"]
```

- Defined with square brackets `[...]`
- Items are separated by commas
- Items are **zero-indexed** — first item is at index `0`

**Accessing items by index:**

```python
students[0]   # "harry"
students[1]   # "hermione"
students[-1]  # "ron"  (negative index counts from the end)
```

**Modifying a list:**

```python
students.append("neville")       # add to end
students.remove("ron")           # remove by value
students[0] = "ginny"            # replace by index
```

**Iterating over a list:**

```python
for student in students:
    print(student)
```

**Common list operations:**

| Operation | Syntax | Description |
|-----------|--------|-------------|
| Length | `len(students)` | Number of items |
| Add item | `students.append("neville")` | Appends to end |
| Remove item | `students.remove("ron")` | Removes first match |
| Check membership | `"harry" in students` | Returns `True`/`False` |
| Sort | `students.sort()` | Sorts in place |

---

## 8. The `len()` Function

`len()` returns the number of items in a sequence — a list, string, or other iterable.

```python
students = ["harry", "hermione", "ron"]
print(len(students))  # 3

print(len("hello"))   # 5
```

---

## 9. Iterating with Index

Sometimes you need both the **index** and the **value** while iterating. There are two approaches.

**Using `range(len(...))`:**

```python
students = ["harry", "hermione", "ron"]

for i in range(len(students)):
    print(i, students[i])
# Output:
# 0 harry
# 1 hermione
# 2 ron
```

**Using `enumerate()` (more Pythonic):**

```python
for i, student in enumerate(students):
    print(i, student)
# Same output — cleaner syntax
```

`enumerate()` returns pairs of `(index, value)` and avoids manual indexing.

---

## 10. Dictionaries

A **dictionary** (`dict`) stores data as **key-value pairs**. Each key maps to a value, like a real-world dictionary where a word maps to its definition.

**Defining a dictionary:**

```python
student = {
    "name": "harry",
    "house": "gryffindor",
    "age": 17
}
```

- Defined with curly braces `{...}`
- Each entry is `key: value`
- Keys must be **unique** — duplicate keys overwrite the previous value
- Keys are typically strings; values can be any type

**Accessing values:**

```python
student["name"]    # "harry"
student["house"]   # "gryffindor"
```

**Adding and updating entries:**

```python
student["patronus"] = "stag"   # add new key
student["age"] = 18            # update existing key
```

**Iterating over a dictionary:**

```python
for key in student:
    print(key, student[key])
```

**Common dictionary operations:**

| Operation | Syntax | Description |
|-----------|--------|-------------|
| Access value | `d["key"]` | Returns value for key |
| Add / update | `d["key"] = value` | Sets key to value |
| Check key | `"key" in d` | Returns `True`/`False` |
| All keys | `d.keys()` | View of all keys |
| All values | `d.values()` | View of all values |
| All pairs | `d.items()` | View of `(key, value)` tuples |

**Why not use parallel lists?**

```python
# Fragile — index positions must stay in sync manually
students = ["harry", "hermione", "ron"]
houses   = ["gryffindor", "gryffindor", "gryffindor"]
```

If you add a student to `students` but forget to add to `houses`, the data breaks silently. A dictionary keeps related data together and removes that risk.

---

## 11. List of Dictionaries

For multiple records with the same fields, the standard Python pattern is a **list of dictionaries** — each dict represents one record.

```python
students = [
    {"name": "harry",    "house": "gryffindor", "patronus": "stag"},
    {"name": "hermione", "house": "gryffindor", "patronus": "otter"},
    {"name": "ron",      "house": "gryffindor", "patronus": "jack russell terrier"},
    {"name": "draco",    "house": "slytherin",  "patronus": "dragon"}
]

for student in students:
    print(student["name"], student["house"], student["patronus"], sep=" | ")
```

**Output:**

```
harry | gryffindor | stag
hermione | gryffindor | otter
ron | gryffindor | jack russell terrier
draco | slytherin | dragon
```

This pattern scales cleanly — adding a new field means adding one key to each dictionary, not adding and synchronizing a new list.

---

## 12. Program Walkthroughs

### `cat.py` — Meow N Times

> [`cat.py`](cat.py)

Demonstrates the evolution from repetitive manual code to a clean, validated loop using functions.

| Version | Approach | Notes |
|---------|----------|-------|
| V1 | `print("meow")` × 3 | Hardcoded — does not scale |
| V2 | `while True:` with no exit | Infinite loop — prints forever |
| V3 | `while True:` + `break` on valid input | Validates input, then loops exactly n times |
| V4 (final) | `get_number()` + `meow(n)` functions | Separated concerns, reusable, clean |

**Key technique — `\n` multiplication:**

```python
def meow(n):
    print("meow\n" * n, end="")
```

Multiplying a string repeats it. `"meow\n" * 3` produces `"meow\nmeow\nmeow\n"`. The `end=""` removes the extra blank line `print()` would add.

---

### `meow.py` — Compact Loop

> [`meow.py`](meow.py)

A concise standalone example of combining a validated `while True` / `break` input loop with a `for _ in range(n)` output loop.

```python
while True:
    n = int(input("What is n? "))
    if n > 0:
        break

for _ in range(n):
    print("meow")
```

`_` is used because the loop counter value is never needed — only the repetition count matters.

---

### `mario.py` — Printing a Square

> [`mario.py`](mario.py)

Builds a square of `#` characters using nested loops. Demonstrates `end=""` to keep characters on the same line and `print()` with no arguments to move to the next line.

```python
def print_rows(w):
    for _ in range(w):
        print("#", end="")   # prints # without newline

def print_square(size):
    for i in range(size):
        print_rows(size)     # fill one row
        print()              # newline after each row
```

For `size = 3`:

```
###
###
###
```

---

### `hogwarts.py` — Lists and Dictionaries

> [`hogwarts.py`](hogwarts.py)

Three functions that demonstrate progressively richer data structures:

| Function | Data structure | What it shows |
|----------|---------------|---------------|
| `list_function()` | `list` of strings | Basic iteration over a list |
| `len_function()` | `list` + `range(len(...))` | Iterating with index |
| `dict_function()` | `list` of `dict` | Rich records with multiple fields, printed with `sep=" \| "` |

---

## Summary

| Concept | Quick Reference |
|---------|----------------|
| `while` loop | `while condition:` — runs while `True` |
| Infinite loop | `while True:` — runs until `break` |
| `break` | Exits the current loop immediately |
| `for` loop | `for x in sequence:` — once per item |
| `range(n)` | Generates `0` to `n-1` |
| `_` variable | Throwaway loop variable — value is unused |
| `\n` | Newline escape character |
| `end=""` | Suppress `print()`'s trailing newline |
| List | `["a", "b", "c"]` — ordered, mutable, indexed from `0` |
| `len()` | `len(x)` — number of items in a sequence |
| Index iteration | `for i in range(len(x)):` or `enumerate(x)` |
| Dictionary | `{"key": "value"}` — key-value pairs |
| Access dict value | `d["key"]` |
| List of dicts | `[{"name": "harry", ...}, ...]` — records pattern |

---

*Part of the [python-learn](https://github.com/) repository. Based on CS50's Introduction to Programming with Python.*

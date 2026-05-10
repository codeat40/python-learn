# Lesson 02 — Python Programming: Conditionals

> **CS50 Harvard** | Python track | Lesson 02  
> Topics: Comparison Operators, `if` / `elif` / `else`, Logical Operators, `match`, Parity

---

## Table of Contents

1. [Comparison Operators](#1-comparison-operators)
2. [The `if` Statement](#2-the-if-statement)
3. [`elif` and `else`](#3-elif-and-else)
4. [Logical Operators — `and`, `or`, `not`](#4-logical-operators--and-or-not)
5. [Comparing x and y — Approaches and Recommendation](#5-comparing-x-and-y--approaches-and-recommendation)
6. [Grade Example — Optimizing `if` Chains](#6-grade-example--optimizing-if-chains)
7. [Parity — Even or Odd](#7-parity--even-or-odd)
8. [The `match` Statement](#8-the-match-statement)

---

## 1. Comparison Operators

**Comparison operators** evaluate a relationship between two values and always return a **boolean** — either `True` or `False`.

| Operator | Meaning | Example | Result |
|----------|---------|---------|--------|
| `==` | Equal to | `3 == 3` | `True` |
| `!=` | Not equal to | `3 != 4` | `True` |
| `<` | Less than | `2 < 5` | `True` |
| `>` | Greater than | `5 > 2` | `True` |
| `<=` | Less than or equal to | `3 <= 3` | `True` |
| `>=` | Greater than or equal to | `4 >= 5` | `False` |

> Do not confuse `=` (assignment) with `==` (comparison). `x = 5` stores a value; `x == 5` checks if x equals 5.

**Python also supports chained comparisons** — a readable shorthand for range checks:

```python
# Standard way:
if score >= 80 and score < 90:
    ...

# Chained (Pythonic):
if 80 <= score < 90:
    ...
```

---

## 2. The `if` Statement

The `if` statement executes a block of code only when a condition is `True`.

**Syntax:**

```python
if condition:
    # runs when condition is True
```

**Example:**

```python
x = int(input("What's x? "))

if x > 0:
    print("x is positive")
```

- The condition is any expression that evaluates to `True` or `False`.
- The indented block below `if` is called the **body** — Python uses indentation (4 spaces) to define blocks, not braces.

---

## 3. `elif` and `else`

When you need to handle multiple branches of logic, use `elif` ("else if") and `else`.

**Syntax:**

```python
if condition_a:
    # runs if condition_a is True
elif condition_b:
    # runs if condition_a is False AND condition_b is True
else:
    # runs if ALL above conditions are False
```

**Rules:**
- You can have **zero or more** `elif` blocks.
- You can have **zero or one** `else` block — it must come last.
- Python evaluates conditions **top to bottom** and stops at the first `True` match.

**Example:**

```python
x = int(input("What's x? "))
y = int(input("What's y? "))

if x < y:
    print("x is less than y")
elif x > y:
    print("x is greater than y")
else:
    print("x is equal to y")
```

---

## 4. Logical Operators — `and`, `or`, `not`

Logical operators combine multiple conditions into one expression.

| Operator | Meaning | Example | Result |
|----------|---------|---------|--------|
| `and` | Both must be `True` | `True and False` | `False` |
| `or` | At least one must be `True` | `True or False` | `True` |
| `not` | Inverts the boolean | `not True` | `False` |

**Examples:**

```python
# and — both conditions required
if score >= 90 and score <= 100:
    print("Grade: A")

# or — either condition is enough
if x < y or x > y:
    print("x is not equal to y")

# not — inverts the result
if not is_even(x):
    print("x is odd")
```

**Short-circuit evaluation:**
- `and` stops evaluating as soon as it finds a `False`.
- `or` stops evaluating as soon as it finds a `True`.

---

## 5. Comparing x and y — Approaches and Recommendation

> Source: [`compare.py`](compare.py)

This lesson explored three different ways to compare two integers. Each has trade-offs in clarity and informativeness.

---

### Approach 1 — Full `if / elif / else` (Most Informative)

```python
def compare(x, y):
    if x < y:
        print("x is less than y")
    elif x > y:
        print("x is greater than y")
    else:
        print("x is equal to y")
```

**Pros:** Tells the user exactly how x and y relate — less than, greater than, or equal.  
**Cons:** More lines of code.

---

### Approach 2 — Using `or` (Less Informative)

```python
def compare(x, y):
    if x < y or x > y:
        print("x is not equal to y")
    else:
        print("x is equal to y")
```

**Pros:** Shorter.  
**Cons:** Loses information — only tells you *whether* values differ, not *how* they differ.

---

### Approach 3 — Using `!=` directly (Most Concise)

```python
def compare(x, y):
    if x == y:
        print("x is equal to y")
    else:
        print("x is not equal to y")
```

**Pros:** Clean and direct — uses `==` which maps exactly to the intent.  
**Cons:** Still loses the less-than / greater-than distinction.

---

### Recommended Approach

**Use Approach 1** when the relationship between values matters to the user (e.g. sorting, ranking, scoring).  
**Use Approach 3** when you only need to know equality (e.g. password confirmation, menu choice matching).

The key principle: **match your logic to what the user actually needs to know.** More conditions are only worth the extra lines if they provide meaningful information. Approach 2 (using `or` to check `x < y or x > y`) is the weakest option — it is longer than Approach 3 while providing the same amount of information, so it should be avoided in favor of a direct `!=` check.

```python
# Preferred when only equality matters:
if x != y:
    print("x is not equal to y")
else:
    print("x is equal to y")
```

---

## 6. Grade Example — Optimizing `if` Chains

> Source: [`grade.py`](grade.py)

This example shows how Python's top-down evaluation of `if / elif` lets you eliminate redundant range checks.

---

### Version 1 — Explicit ranges with `and`

```python
if score >= 90 and score <= 100:
    print("Your grade is A.")
elif score >= 80 and score < 90:
    print("Your grade is B.")
elif score >= 70 and score < 80:
    print("Your grade is C.")
elif score >= 60 and score < 70:
    print("Your grade is D.")
elif score >= 0 and score < 60:
    print("Your grade is F.")
else:
    print("Invalid score.")
```

Correct, but verbose — each branch checks both the lower and upper bound.

---

### Version 2 — Chained comparisons

```python
if 90 <= score <= 100:
    print("Your grade is A.")
elif 80 <= score < 90:
    print("Your grade is B.")
elif 70 <= score < 80:
    print("Your grade is C.")
elif 60 <= score < 70:
    print("Your grade is D.")
elif 0 <= score < 60:
    print("Your grade is F.")
else:
    print("Invalid score.")
```

More readable than Version 1. Chained comparisons are a Python feature — `80 <= score < 90` is evaluated left to right as `80 <= score and score < 90`.

---

### Version 3 — Optimized (Recommended)

```python
if score >= 90:
    print("Your grade is A.")
elif score >= 80:
    print("Your grade is B.")
elif score >= 70:
    print("Your grade is C.")
elif score >= 60:
    print("Your grade is D.")
elif score >= 0:
    print("Your grade is F.")
else:
    print("Invalid score.")
```

**Why this works:** Because `elif` only runs when all previous conditions were `False`, the upper bound check is implicit. If `score >= 90` is `False`, we already know `score < 90` by the time we reach the next `elif`. This removes all redundant upper-bound checks and makes the code significantly shorter without losing any correctness.

> **Rule of thumb:** When chaining `elif` blocks with descending thresholds, you only need to check the lower bound of each range.

---

## 7. Parity — Even or Odd

> Source: [`parity.py`](parity.py)

Parity describes whether a number is **even** (divisible by 2) or **odd** (not divisible by 2). This is checked using the **modulo operator** `%`, which returns the remainder of a division.

```python
10 % 2 == 0   # True  → even
7  % 2 == 1   # True  → odd
```

---

### Version 1 — Explicit `if / else`

```python
def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False
```

Clear and readable. Good for beginners.

---

### Version 2 — Ternary expression

```python
def is_even(n):
    return True if n % 2 == 0 else False
```

Shorter, but still redundant — we are returning a boolean based on a boolean expression.

---

### Version 3 — Direct boolean return (Recommended)

```python
def is_even(n):
    return n % 2 == 0
```

`n % 2 == 0` already evaluates to `True` or `False`, so returning it directly is the cleanest approach.

**Full program:**

```python
def is_even(n):
    return n % 2 == 0

def main():
    x = int(input("What's x? "))
    if is_even(x):
        print("x is even.")
    else:
        print("x is odd.")

main()
```

> Notice that `if is_even(x):` reads almost like plain English — "if x is even". Writing functions that return booleans and naming them `is_*` is a common and recommended Python convention.

---

## 8. The `match` Statement

> Source: [`house.py`](house.py)

The `match` statement (introduced in Python 3.10) is a **structural pattern matching** tool — similar to `switch` in other languages. It compares a value against a series of patterns and runs the first matching case.

**Syntax:**

```python
match variable:
    case pattern_1:
        # runs if variable matches pattern_1
    case pattern_2:
        # runs if variable matches pattern_2
    case _:
        # wildcard — runs if nothing else matched (like else)
```

The `_` (underscore) is the **wildcard pattern** — it matches anything and acts as the default fallback.

---

### Evolution of `house.py`

**Version 1 — Long `if / elif` chain:**

```python
if name.lower() == "harry":
    print("Gryffindor!")
elif name.lower() == "hermione":
    print("Gryffindor!")
elif name.lower() == "ron":
    print("Gryffindor!")
elif name.lower() == "draco":
    print("Slytherin!")
# ...
```

Repetitive — multiple branches share the same output.

---

**Version 2 — Grouped with `in` list:**

```python
if name.lower() in ["harry", "hermione", "ron", "neville", "george", "fred"]:
    print("Gryffindor!")
elif name.lower() == "draco":
    print("Slytherin!")
elif name.lower() == "luna":
    print("Ravenclaw!")
else:
    print("I don't know which house you belong to.")
```

Better — multiple values share one branch using a list and `in`.

---

**Version 3 — `match` with `|` (pipe) patterns (Recommended):**

```python
match name.lower():
    case "harry" | "hermione" | "ron" | "neville" | "george" | "fred":
        print("Gryffindor!")
    case "draco":
        print("Slytherin!")
    case "luna":
        print("Ravenclaw!")
    case _:
        print("I don't know which house you belong to.")
```

The `|` operator inside a `case` means **"or"** — match any of these values. This version is the most expressive and readable when you are matching one variable against many specific literal values.

**When to prefer `match` over `if / elif`:**

| Scenario | Prefer |
|----------|--------|
| Comparing one variable to many specific values | `match` |
| Checking ranges or complex conditions | `if / elif` |
| Combining multiple variables or expressions | `if / elif` |
| Python version < 3.10 | `if / elif` (match not available) |

---

## Summary

| Concept | Quick Reference |
|---------|----------------|
| Equal | `x == y` |
| Not equal | `x != y` |
| Less / greater | `x < y`, `x > y`, `x <= y`, `x >= y` |
| Chained range | `80 <= score < 90` |
| Basic conditional | `if condition:` |
| Multiple branches | `if ... elif ... else` |
| Both conditions true | `and` |
| Either condition true | `or` |
| Invert condition | `not` |
| Parity check | `n % 2 == 0` → even |
| Boolean return | `return n % 2 == 0` |
| Pattern matching | `match` / `case` / `case _:` |
| Multiple values in one case | `case "a" \| "b" \| "c":` |

---

*Part of the [python-learn](https://github.com/) repository. Based on CS50's Introduction to Programming with Python.*

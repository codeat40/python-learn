# Lesson 04 — Python Programming: Exceptions

> **CS50 Harvard** | Python track | Lesson 04  
> Topics: `try`, `except`, `else`, `ValueError`, `NameError`, `SyntaxError`, `pass`, `raise`, Exception handling patterns

---

## Table of Contents

1. [What Is an Exception?](#1-what-is-an-exception)
2. [The `try` Block](#2-the-try-block)
3. [The `except` Block](#3-the-except-block)
4. [`ValueError` — What It Is and When It Occurs](#4-valueerror--what-it-is-and-when-it-occurs)
5. [The `else` Block (Catch)](#5-the-else-block-catch)
6. [The `pass` Keyword](#6-the-pass-keyword)
7. [Full `try / except / else` Structure](#7-full-try--except--else-structure)
8. [Common Exception Types](#8-common-exception-types)
9. [`NameError`](#9-nameerror)
10. [`SyntaxError`](#10-syntaxerror)
11. [The `raise` Keyword](#11-the-raise-keyword)
12. [Program Walkthrough — `number.py`](#12-program-walkthrough--numberpy)

---

## 1. What Is an Exception?

An **exception** is an error that occurs at runtime — when the program is already running. Unlike syntax errors (which prevent the program from starting), exceptions happen when Python encounters something it cannot handle during execution.

**Example — unhandled exception:**

```python
x = int(input("What is x? "))
print(f"x is {x}")
```

If the user types `"hello"` instead of a number:

```
ValueError: invalid literal for int() with base 10: 'hello'
```

The program **crashes**. Without exception handling, any bad input ends the program immediately.

**Exception handling** lets you anticipate these errors and respond to them gracefully — instead of crashing, your program can inform the user and try again.

---

## 2. The `try` Block

The `try` block wraps the code that **might** raise an exception. Python attempts to execute it, and if an error occurs, execution jumps to the matching `except` block immediately — the rest of the `try` body is skipped.

**Syntax:**

```python
try:
    # code that might raise an exception
```

**Example:**

```python
try:
    x = int(input("What is x? "))
```

If the user enters a valid integer, `int()` succeeds and `x` is assigned.  
If the user enters `"cat"`, `int()` raises a `ValueError` and execution immediately moves to `except`.

> Only put code that can realistically fail in a `try` block. Keep the body as small and focused as possible — wrapping too much code makes it harder to know what caused the error.

---

## 3. The `except` Block

The `except` block runs **only when the specified exception is raised** inside the `try` block. You name the exception type you want to catch after the `except` keyword.

**Syntax:**

```python
except ExceptionType:
    # runs only if ExceptionType was raised in try
```

**Example:**

```python
try:
    x = int(input("What is x? "))
except ValueError:
    print("That is not an integer.")
```

If the user types `"hello"`:
1. `int("hello")` raises `ValueError`
2. The `try` block is abandoned at that line
3. `except ValueError:` catches it and prints the message

If the user types `3`:
1. `int("3")` succeeds — no exception
2. `except` block is skipped entirely

---

## 4. `ValueError` — What It Is and When It Occurs

`ValueError` is raised when a function receives an argument of the **right type** but an **inappropriate value**.

The most common case in beginner Python is passing a non-numeric string to `int()` or `float()`:

```python
int("hello")    # ValueError: invalid literal for int() with base 10: 'hello'
int("")         # ValueError: invalid literal for int() with base 10: ''
float("abc")    # ValueError: could not convert string to float: 'abc'
```

Note the distinction:

| Exception | Cause |
|-----------|-------|
| `ValueError` | Right type, wrong value — e.g. `int("hello")` |
| `TypeError` | Wrong type entirely — e.g. `int([1, 2, 3])` |
| `ZeroDivisionError` | Division by zero — e.g. `10 / 0` |

`ValueError` is the exception you will encounter most often when working with user input, because `input()` always returns a string and users frequently type unexpected things.

---

## 5. The `else` Block (Catch)

The `else` block in a `try / except` structure runs **only when no exception was raised** in the `try` block. It is the "success path" — code that should only execute if everything in `try` worked.

**Syntax:**

```python
try:
    # code that might fail
except ValueError:
    # runs on failure
else:
    # runs only on success — no exception was raised
```

**Example:**

```python
try:
    x = int(input("What is x? "))
except ValueError:
    print("That is not an integer.")
else:
    print(f"x is {x}")   # only runs if int() succeeded
```

**Why use `else` instead of putting the success code at the end of `try`?**

```python
# Less clear — print() is inside try but cannot raise ValueError
try:
    x = int(input("What is x? "))
    print(f"x is {x}")   # this works, but it is inside try unnecessarily
except ValueError:
    print("That is not an integer.")

# More clear — try contains only the risky line; else contains the success logic
try:
    x = int(input("What is x? "))
except ValueError:
    print("That is not an integer.")
else:
    print(f"x is {x}")
```

`else` makes the intent explicit: the code in `else` only belongs to the success scenario and has nothing to do with the error scenario.

---

## 6. The `pass` Keyword

`pass` is a **no-op** — it does absolutely nothing. It is a placeholder that satisfies Python's requirement that a block cannot be empty.

```python
try:
    x = int(input("What is x? "))
except ValueError:
    pass   # silently ignore the error — do nothing
```

When used in an `except` block, `pass` means: *"I know this error can happen, I choose to ignore it and continue."*

**Common use cases for `pass`:**

```python
# Silent retry loop — no error message, just ask again
while True:
    try:
        x = int(input("What is x? "))
    except ValueError:
        pass   # bad input — loop back silently and prompt again
    else:
        break  # valid input — exit the loop
```

**`pass` vs printing an error message:**

| Approach | Behaviour | When to use |
|----------|-----------|-------------|
| `pass` | Silently ignores the error | When the user doesn't need to know why it failed |
| `print("error message")` | Informs the user | When feedback helps the user correct their input |

Neither is universally correct — choose based on what makes your program most usable.

---

## 7. Full `try / except / else` Structure

Putting it all together:

```python
try:
    # 1. Attempt the risky operation
    x = int(input("What is x? "))
except ValueError:
    # 2. Handle the specific error — runs only on failure
    print("x is not an integer")
else:
    # 3. Success path — runs only when try succeeded with no exception
    return x
```

**Execution flow:**

```
User input: "hello"
  → try: int("hello") → raises ValueError
  → except ValueError: print("x is not an integer")
  → else: skipped

User input: "5"
  → try: int("5") → succeeds, x = 5
  → except ValueError: skipped
  → else: return x → returns 5
```

**Combined with a `while True` loop for repeated input validation:**

```python
while True:
    try:
        x = int(input("What is x? "))
    except ValueError:
        print("x is not an integer")   # or: pass
    else:
        return x   # valid input received — exit the loop by returning
```

This is the **standard Python pattern for validated input** — keep asking until you get what you need, using exceptions to detect invalid responses.

---

## 8. Common Exception Types

| Exception | Raised when |
|-----------|-------------|
| `ValueError` | Right type, wrong value — `int("hello")` |
| `TypeError` | Wrong type for the operation — `"a" + 1` |
| `ZeroDivisionError` | Division or modulo by zero — `10 / 0` |
| `IndexError` | List index out of range — `[1,2,3][5]` |
| `KeyError` | Dictionary key does not exist — `d["missing"]` |
| `FileNotFoundError` | File does not exist when opening — `open("x.txt")` |
| `NameError` | Variable used before it was defined |
| `RecursionError` | Maximum recursion depth exceeded |

You can catch multiple exception types in one block:

```python
except (ValueError, TypeError):
    print("Invalid input.")
```

Or catch any exception (use sparingly — too broad, hides real bugs):

```python
except Exception:
    print("Something went wrong.")
```

---

## 9. `NameError`

A `NameError` is raised when Python encounters a **name (variable, function, or module) that has not been defined** at the point where it is used.

**Common causes:**

```python
# Using a variable before assigning it
print(x)
# NameError: name 'x' is not defined

# Typo in a variable name
name = "Alice"
print(nane)
# NameError: name 'nane' is not defined

# Calling a function before defining it (at module level, order matters)
result = add(2, 3)
def add(a, b):
    return a + b
# NameError: name 'add' is not defined
```

**How it differs from `ValueError`:**

| Exception | Cause |
|-----------|-------|
| `NameError` | The name itself doesn't exist — Python can't find it |
| `ValueError` | The name exists and has the right type, but the value is wrong |

**Catching a `NameError`:**

```python
try:
    print(x)
except NameError:
    print("Variable is not defined.")
```

> `NameError` almost always signals a bug in the code — a typo, wrong scope, or missing import. It is rarely something you should silently catch and ignore.

---

## 10. `SyntaxError`

A `SyntaxError` is raised when Python **cannot parse the code** because it violates the language's grammar rules. Unlike other exceptions, `SyntaxError` is detected **before the program runs** — at the parsing stage.

**Common causes:**

```python
# Missing colon after if
if x > 0
    print("positive")
# SyntaxError: expected ':'

# Mismatched parentheses
print("hello"
# SyntaxError: '(' was never closed

# Invalid assignment target
5 = x
# SyntaxError: cannot assign to literal here

# Missing quotes
name = hello
# This raises NameError, not SyntaxError — 'hello' is treated as a variable name
```

**Key distinction — `SyntaxError` cannot be caught at runtime:**

```python
# This does NOT work — the file won't even start executing
try:
    if x > 0    # missing colon — SyntaxError at parse time
        print(x)
except SyntaxError:
    print("syntax problem")
```

Because Python parses the entire file before running it, a `SyntaxError` anywhere in the file prevents the whole program from starting. There is nothing to catch.

**When `SyntaxError` can be caught** — only when you are dynamically compiling or executing code as a string:

```python
code = "if x > 0"   # incomplete code as a string

try:
    compile(code, "<string>", "exec")
except SyntaxError:
    print("The code string has a syntax error.")
```

> In practice, fix `SyntaxError` in your editor — don't try to handle it at runtime.

---

## 11. The `raise` Keyword

The `raise` keyword lets you **deliberately trigger an exception** from your own code. This is how you enforce rules and signal to callers that something is wrong.

**Syntax:**

```python
raise ExceptionType("descriptive message")
```

**Example — enforcing a positive number:**

```python
def get_integer():
    while True:
        try:
            x = int(input("What is x? "))
        except ValueError:
            print("x is not an integer")
        else:
            if x <= 0:
                raise ValueError("x must be a positive integer")
            return x
```

**Why raise an exception instead of just printing an error?**

- Printing only informs the user visually — the calling code has no way to know something went wrong.
- `raise` communicates failure to the **code** that called your function, giving it the chance to handle it.

**Re-raising an exception you caught:**

```python
try:
    x = int(input("What is x? "))
except ValueError:
    raise   # re-raises the same ValueError without modification
```

Plain `raise` with no arguments re-raises the current exception — useful when you want to log or inspect the error before letting it propagate.

**Raising inside a function for input validation:**

```python
def set_age(age):
    if not isinstance(age, int):
        raise TypeError("age must be an integer")
    if age < 0 or age > 150:
        raise ValueError(f"age {age} is out of range")
    return age
```

The caller can then decide how to handle it:

```python
try:
    set_age(-5)
except ValueError as e:
    print(f"Invalid age: {e}")
# Output: Invalid age: age -5 is out of range
```

**`as e` — capturing the exception object:**

```python
except ValueError as e:
    print(e)   # prints the exception message
```

`as e` binds the exception instance to the name `e`, letting you read its message or inspect it.

---

## 12. Program Walkthrough — `number.py`

> [`number.py`](number.py)

`number.py` demonstrates the complete validated-input pattern using `try / except / else` inside a `while True` loop.

```python
def main():
    x = get_integer()
    print(f"x is {x}")

def get_integer():
    while True:
        try:
            x = int(input("What is x? "))
        except ValueError:
            print("x is not an integer")
        else:
            return x

main()
```

**Breakdown:**

| Part | Role |
|------|------|
| `while True:` | Keeps the prompt running until valid input is received |
| `try:` | Attempts to convert user input to an integer |
| `int(input(...))` | `input()` returns a string; `int()` converts it — raises `ValueError` if it can't |
| `except ValueError:` | Catches the error when input is not a valid integer |
| `print("x is not an integer")` | Informs the user — could be replaced with `pass` to fail silently |
| `else:` | Runs only when `int()` succeeded — no exception was raised |
| `return x` | Returns the valid integer and exits the loop |

**Alternative — using `pass` instead of printing:**

```python
except ValueError:
    pass   # silently ignore, loop back and prompt again
```

**Alternative — returning directly from `try` (valid but less clear):**

```python
try:
    return int(input("What is x? "))
except ValueError:
    print("x is not an integer")
```

This works but puts the `return` inside `try`, making it less obvious that the return only happens on success. The `try / except / else` version with `return` in `else` communicates that intent more clearly.

---

## Summary

| Concept | Quick Reference |
|---------|----------------|
| Exception | Runtime error that crashes the program if unhandled |
| `try` | Wraps code that might raise an exception |
| `except ValueError` | Catches a `ValueError` raised inside `try` |
| `else` | Runs only when `try` succeeded — no exception raised |
| `pass` | No-op placeholder — silently ignores the exception |
| `ValueError` | Right type, wrong value — `int("hello")` |
| `NameError` | Name (variable/function) used before it was defined |
| `SyntaxError` | Code violates Python grammar — caught at parse time, not runtime |
| `raise` | Deliberately trigger an exception from your own code |
| `raise ValueError("msg")` | Raise with a descriptive message |
| `raise` (bare) | Re-raise the current exception |
| `except ValueError as e` | Capture the exception object to read its message |
| Validated input pattern | `while True` + `try/except/else` + `return` in `else` |

---

*Part of the [python-learn](https://github.com/) repository. Based on CS50's Introduction to Programming with Python.*

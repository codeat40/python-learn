# Lesson 01 — Python Programming: Introduction

> **CS50 Harvard** | Python track | Lesson 01  
> Topics: Environment setup, Functions, Variables, Types, and Core Concepts

---

## Table of Contents

1. [Setting Up the Programmatic Environment](#1-setting-up-the-programmatic-environment)
2. [Functions and Arguments](#2-functions-and-arguments)
3. [Side Effects](#3-side-effects)
4. [Return Values](#4-return-values)
5. [Variables](#5-variables)
6. [Comments](#6-comments)
7. [Pseudocode](#7-pseudocode)
8. [Strings — `str`](#8-strings--str)
9. [Parameters](#9-parameters)
10. [f-Strings](#10-f-strings)
11. [String Methods](#11-string-methods)
12. [Integers — `int`](#12-integers--int)
13. [Math Symbols](#13-math-symbols)
14. [Interactive Mode](#14-interactive-mode)
15. [Floats — `float`](#15-floats--float)
16. [The `round()` Function](#16-the-round-function)
17. [Defining Functions — `def` and Scope](#17-defining-functions--def-and-scope)
18. [The `return` Keyword](#18-the-return-keyword)

---

## 1. Setting Up the Programmatic Environment

Before writing any code, you need a working Python environment.

**Steps:**

1. Install Python from the [official Python website](https://www.python.org/downloads/). Prefer the latest stable version.
2. Verify the installation by running the following in your terminal:

```bash
python --version
# or on some systems:
python3 --version
```

3. Choose an editor or IDE. Common choices:
   - **VS Code** with the Python extension
   - **PyCharm**
   - **CS50 Codespace** (browser-based, used in the course)

4. Create your first file with a `.py` extension:

```bash
touch hello.py
```

5. Run a Python file from the terminal:

```bash
python hello.py
```

---

## 2. Functions and Arguments

A **function** is a named block of reusable code that performs a specific task. You *call* (invoke) a function by writing its name followed by parentheses.

An **argument** is a value you pass into a function so it can use that value during execution.

**Syntax:**

```python
function_name(argument)
```

**Example:**

```python
print("Hello, world!")
```

Here:
- `print` is the function.
- `"Hello, world!"` is the argument passed to it.

Functions can accept **multiple arguments** separated by commas:

```python
print("Hello,", "world!")
# Output: Hello, world!
```

---

## 3. Side Effects

A **side effect** is anything a function does *beyond* returning a value — such as printing output to the screen, writing to a file, or modifying a variable outside its own scope.

**Example:**

```python
print("This is a side effect")
```

`print()` does not return a useful value — its purpose is the *side effect* of displaying text on screen.

> Side effects are not inherently bad, but understanding when a function has them (versus when it purely computes and returns a value) is key to writing predictable code.

---

## 4. Return Values

A **return value** is the output a function hands back to the caller. Not all functions return a value — some only produce side effects.

**Example:**

```python
result = len("hello")
print(result)  # Output: 5
```

Here `len()` *returns* the integer `5`, which is then stored in `result`.

Functions that do not explicitly return anything return `None` by default:

```python
x = print("hi")
print(x)  # Output: None
```

---

## 5. Variables

A **variable** is a name that stores a value in memory. In Python, you do not need to declare a type — Python infers it automatically.

**Syntax:**

```python
variable_name = value
```

**Examples:**

```python
name = "Alice"
age = 25
height = 5.7
```

**Rules for naming variables:**
- Must start with a letter or underscore (`_`)
- Cannot start with a number
- Can contain letters, numbers, and underscores
- Case-sensitive: `name` and `Name` are different variables
- Use `snake_case` by convention in Python

**Reassigning a variable:**

```python
name = "Alice"
name = "Bob"   # name now holds "Bob"
```

---

## 6. Comments

A **comment** is a note in your code that Python ignores during execution. Comments are for humans — they explain what the code does.

**Single-line comment** — use `#`:

```python
# This prints a greeting
print("Hello!")
```

**Inline comment:**

```python
age = 25  # user's age in years
```

**Multi-line comment** — Python has no dedicated multi-line comment syntax, but you can use multiple `#` lines or a multi-line string (though the latter is not a true comment):

```python
# This function calculates
# the area of a rectangle
def area(w, h):
    return w * h
```

> Good comments explain *why* something is done, not *what* — the code itself shows what.

---

## 7. Pseudocode

**Pseudocode** is an informal, plain-language description of the steps in an algorithm. It is not valid Python — it is a planning tool used before writing real code.

**Example — pseudocode for greeting a user:**

```
ask the user for their name
store the name in a variable
print "Hello, " followed by the name
```

**Translated into Python:**

```python
name = input("What is your name? ")
print("Hello,", name)
```

Pseudocode helps you think through logic without worrying about syntax.

---

## 8. Strings — `str`

A **string** (`str`) is a sequence of characters used to represent text. Strings are enclosed in either single quotes `'...'` or double quotes `"..."`.

```python
greeting = "Hello, world!"
language = 'Python'
```

**Official Python docs reference:**

> [`str`](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str) — Python's built-in text type.

**The `print()` function signature (from the official docs):**

```python
print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
```

| Parameter | Default | Description |
|-----------|---------|-------------|
| `*objects` | — | One or more values to print |
| `sep` | `' '` | String inserted between values |
| `end` | `'\n'` | String appended after the last value |
| `file` | `sys.stdout` | Output stream (defaults to the terminal) |
| `flush` | `False` | Whether to forcibly flush the stream |

**Examples using `print()` parameters:**

```python
print("Hello", "World", sep=", ")
# Output: Hello, World

print("Loading", end="...")
# Output: Loading...  (no newline at the end)
```

---

## 9. Parameters

**Parameters** are the named placeholders defined in a function's signature. They describe what a function expects to receive. **Arguments** are the actual values passed when calling the function.

```python
# 'name' is a parameter
def greet(name):
    print("Hello,", name)

# "Alice" is the argument
greet("Alice")
```

**Positional vs. keyword arguments:**

```python
print("a", "b", "c")               # positional
print("a", "b", "c", sep="-")      # 'sep' is a keyword argument
# Output: a-b-c
```

Keyword arguments are passed by name and can appear in any order.

---

## 10. f-Strings

An **f-string** (formatted string literal) lets you embed expressions directly inside a string by prefixing it with `f` or `F`. Expressions go inside `{}`.

**Syntax:**

```python
f"...{expression}..."
```

**Examples:**

```python
name = "Alice"
age = 25

print(f"Hello, {name}!")
# Output: Hello, Alice!

print(f"In 10 years you will be {age + 10} years old.")
# Output: In 10 years you will be 35 years old.
```

f-strings are the preferred way to build strings dynamically in modern Python (3.6+).

---

## 11. String Methods

A **method** is a function that belongs to an object. String methods are called on a string value using dot notation:

```python
string.method_name()
```

**Commonly used string methods:**

| Method | Description | Example |
|--------|-------------|---------|
| `.upper()` | Converts to uppercase | `"hello".upper()` → `"HELLO"` |
| `.lower()` | Converts to lowercase | `"HELLO".lower()` → `"hello"` |
| `.strip()` | Removes leading/trailing whitespace | `"  hi  ".strip()` → `"hi"` |
| `.replace(old, new)` | Replaces a substring | `"cat".replace("c", "b")` → `"bat"` |
| `.split(sep)` | Splits into a list | `"a,b,c".split(",")` → `["a","b","c"]` |
| `.title()` | Capitalizes first letter of each word | `"hello world".title()` → `"Hello World"` |

**Example:**

```python
name = input("Enter your name: ")
name = name.strip().title()
print(f"Hello, {name}!")
```

> Full reference: [Python `str` methods](https://docs.python.org/3/library/stdtypes.html#string-methods)

---

## 12. Integers — `int`

An **integer** (`int`) is a whole number — positive, negative, or zero — with no decimal point.

```python
x = 10
y = -3
z = 0
```

You can convert other types to integers using `int()`:

```python
n = int("42")   # string → int
n = int(3.9)    # float → int (truncates, does NOT round) → 3
```

**Type checking:**

```python
print(type(42))   # <class 'int'>
```

---

## 13. Math Symbols

Python supports standard arithmetic operators:

| Operator | Operation | Example | Result |
|----------|-----------|---------|--------|
| `+` | Addition | `3 + 2` | `5` |
| `-` | Subtraction | `5 - 1` | `4` |
| `*` | Multiplication | `4 * 3` | `12` |
| `/` | Division (float result) | `7 / 2` | `3.5` |
| `//` | Floor division (int result) | `7 // 2` | `3` |
| `%` | Modulo (remainder) | `7 % 2` | `1` |
| `**` | Exponentiation | `2 ** 8` | `256` |

**Examples:**

```python
print(1 + 2)    # 3
print(10 / 3)   # 3.3333...
print(10 // 3)  # 3
print(10 % 3)   # 1
print(2 ** 10)  # 1024
```

**Order of operations** follows standard mathematical precedence (PEMDAS/BODMAS). Use parentheses to control evaluation:

```python
print(2 + 3 * 4)    # 14
print((2 + 3) * 4)  # 20
```

---

## 14. Interactive Mode

Python's **interactive mode** (also called the REPL — Read-Eval-Print Loop) lets you type and execute Python expressions one line at a time directly in the terminal.

**Starting interactive mode:**

```bash
python
# or
python3
```

You'll see a prompt:

```
Python 3.x.x ...
>>>
```

**Using it:**

```python
>>> 2 + 2
4
>>> name = "Alice"
>>> print(f"Hello, {name}!")
Hello, Alice!
```

To exit:

```python
>>> exit()
```

Interactive mode is useful for quickly testing small snippets of code without writing a full script.

---

## 15. Floats — `float`

A **float** (floating-point value) is a number with a decimal point. Floats are used when precision beyond whole numbers is needed.

```python
price = 9.99
pi = 3.14159
temperature = -2.5
```

You can convert other types to float using `float()`:

```python
x = float("3.14")  # string → float
y = float(5)       # int → float → 5.0
```

**Floating-point precision:**

Floats can produce small rounding errors due to how computers represent decimal numbers in binary:

```python
print(0.1 + 0.2)
# Output: 0.30000000000000004
```

This is expected behavior, not a bug. Use `round()` when precision matters.

---

## 16. The `round()` Function

**`round()`** rounds a number to a specified number of decimal places.

**Signature (from the official docs):**

```python
round(number[, ndigits])
```

| Parameter | Description |
|-----------|-------------|
| `number` | The number to round |
| `ndigits` | Number of decimal places (optional; defaults to `0`) |

**Examples:**

```python
round(3.14159)       # 3
round(3.14159, 2)    # 3.14
round(2.675, 2)      # 2.67  (floating-point quirk)
round(10.5)          # 10    (banker's rounding — rounds to even)
round(11.5)          # 12
```

> Python uses **banker's rounding** (round half to even), which differs from the "round half up" rule taught in school.

**Practical use:**

```python
price = 19.9999
print(f"${round(price, 2)}")
# Output: $20.0
```

---

## 17. Defining Functions — `def` and Scope

### `def`

The `def` keyword defines a new function. Once defined, you can call the function by name anywhere *after* its definition.

**Syntax:**

```python
def function_name(parameter1, parameter2):
    # function body
    ...
```

**Example:**

```python
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")   # Output: Hello, Alice!
greet("Bob")     # Output: Hello, Bob!
```

### Scope

**Scope** refers to the region of code where a variable is accessible.

- **Local scope** — a variable created *inside* a function exists only within that function.
- **Global scope** — a variable created *outside* all functions is accessible throughout the file.

```python
x = 10  # global scope

def show():
    y = 5  # local scope — only exists inside show()
    print(x)  # can read global x
    print(y)

show()
print(x)  # works
print(y)  # NameError: name 'y' is not defined
```

> Best practice: avoid relying on global variables inside functions. Pass values in as parameters instead.

---

## 18. The `return` Keyword

The `return` keyword exits a function and optionally sends a value back to the caller.

**Syntax:**

```python
def function_name():
    return value
```

**Example:**

```python
def add(a, b):
    return a + b

result = add(3, 4)
print(result)  # Output: 7
```

**Key points:**

- A function can only `return` once per call — execution stops at `return`.
- If no `return` is specified (or `return` is used with no value), the function returns `None`.
- The returned value can be stored in a variable, passed to another function, or used in an expression.

```python
def square(n):
    return n ** 2

print(square(5))            # 25
print(square(3) + square(4)) # 25
```

**`return` vs side effects:**

```python
# Side effect only — prints but returns None
def greet_side_effect(name):
    print(f"Hello, {name}!")

# Returns a value — caller decides what to do with it
def greet_return(name):
    return f"Hello, {name}!"

message = greet_return("Alice")
print(message.upper())  # HELLO, ALICE!
```

---

## Summary

| Concept | Quick Reference |
|---------|----------------|
| Function | `print("hello")` |
| Argument | Value passed to a function: `"hello"` |
| Return value | Output of a function: `len("hi")` → `2` |
| Side effect | Action beyond returning: printing, writing to file |
| Variable | `name = "Alice"` |
| Comment | `# this is a comment` |
| String `str` | `"hello"` or `'hello'` |
| Integer `int` | `42` |
| Float `float` | `3.14` |
| f-String | `f"Hello, {name}!"` |
| String method | `"hello".upper()` → `"HELLO"` |
| Math operators | `+`, `-`, `*`, `/`, `//`, `%`, `**` |
| `round()` | `round(3.14159, 2)` → `3.14` |
| `def` | Define a function |
| `return` | Send a value back from a function |
| Scope | Local (inside function) vs. Global (outside) |
| Interactive mode | Run `python` in terminal, use `>>>` prompt |
| Pseudocode | Plain-language planning before writing code |

---

*Part of the [python-learn](https://github.com/) repository. Based on CS50's Introduction to Programming with Python.*

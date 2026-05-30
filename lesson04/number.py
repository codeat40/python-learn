# number.py
# Demonstrates: try / except / else for exception handling, ValueError, pass, validated input loop.

def main():
    x = get_integer()
    print(f"x is {x}")

def get_integer():
    # while True keeps asking until valid input is received — exit happens via return in else.
    while True:
        try:
            # int() raises ValueError if the string cannot be converted to an integer.
            # e.g. int("hello") → ValueError: invalid literal for int() with base 10: 'hello'
            x = int(input("What is x? "))

        except ValueError:
            # Catches the ValueError raised by int() on bad input.
            # Option A: inform the user (chosen here).
            print("x is not an integer")
            # Option B: silent retry — replace the line above with: pass

        else:
            # else runs only when try succeeded — no exception was raised.
            # Returning here exits both the else block and the while loop.
            return x

main()

# mario.py
# Demonstrates: nested loops, end="" to suppress newlines, print() with no args for a newline.

# \n printed before and after the welcome message to add blank lines around it.
print("\n" + "welcome to mario.py" + "\n")

def print_columns(h):
    # Prints h rows of a single "#" — each print() adds its default newline.
    for _ in range(h):
        print("#")

def print_rows(w):
    # Prints w "#" characters on a single line.
    # end="" overrides print()'s default newline so characters stay on the same line.
    for _ in range(w):
        print("#", end="")

def print_square(size):
    # Outer loop: one iteration per row.
    for i in range(size):
        print_rows(size)   # fill the row with # characters (no newline after each)
        print()            # print() with no arguments outputs only a newline — moves to the next row

def main():
    print_square(int(input("Size: ")))

main()

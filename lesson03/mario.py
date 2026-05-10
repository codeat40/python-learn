print("\n" + "welcome to mario.py" + "\n")

def print_columns(h):
    for _ in range(h):
        print("#")

def print_rows(w):
    for _ in range(w):
        print("#", end="")

def print_square(size):
    for i in range(size):
        print_rows(size)
        print()

def main():
    print_square(int(input("Size: ")))

main()
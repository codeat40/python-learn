# cat.py
# Demonstrates: evolution from hardcoded prints → infinite loop → validated input loop → clean functions.

# --- Version 1: Hardcoded (does not scale) ---
# print("meow")
# print("meow")
# print("meow")
# Problem: to change the count you must add or remove lines manually.

# --- Version 2: Infinite loop (no exit condition) ---
# while True:
#     print("meow")
# Problem: runs forever — never stops.

# --- Version 3 / Final: Validated input + separated functions ---

def main():
    n = get_number()   # ask for a valid number
    meow(n)            # print "meow" that many times

def get_number():
    # while True / break pattern: keep asking until the user gives a positive integer.
    while True:
        n = int(input("What is n? "))
        if n > 0:
            break   # exit loop — input is valid
    return n

def meow(n):
    # for loop with _ : the loop counter is unused, we only care about repeating n times.
    for _ in range(n):
        print("meow")

# --- Alternative one-liner for meow() using string multiplication and \n ---
# def meow(n):
#     print("meow\n" * n, end="")
# "meow\n" * n repeats the string n times (each with its own newline).
# end="" prevents print() from adding an extra blank line after the last "meow".

main()

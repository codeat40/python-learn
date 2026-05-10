# This program determines if a number is even or odd.

def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

    # this code is replaced by the code above, but it is still valid code
    # return True if n % 2 == 0 else False
    # this code is replaced by the code above, but it is still valid code
    # return n % 2 == 0

def main():
    x = int(input("What's x?"))

    if is_even(x):
        print("x is even.")
    else:
        print("x is odd.")
    
main()
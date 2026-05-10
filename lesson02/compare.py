x = int(input("What's x?"))
y = int(input("What's y?"))

# version 1 if statements
# this version is more informative than the second version because it tells us if x is less than, greater than, or equal to y, but it is less concise than the second version because it requires more lines of code.

def compare(x, y):
    if x < y:
        print("x is less than y")

    # this code is replaced by the elif and else statements below, but it is still valid code
    # if x > y:
    #     print("x is greater than y")
    # if x == y:
    #     print("x is equal to y")

    elif x > y:
        print("x is greater than y")
    else:    
        print("x is equal to y")

# version 2 if statements 
# this version is more concise, but it is less informative than the first version because it only tells us if x and y are equal or not equal, but it doesn't tell us if x is less than or greater than y.

# this code uses OR to check if x is less than or greater than y, but it is not as informative as the first version because it doesn't tell us if x is less than or greater than y, it only tells us that x is not equal to y.

"""
def compare(x, y):
    if x < y or x > y:
        print("x is not equal to y")
    else:    
        print("x is equal to y")
"""

# this is replacing the code above, but it is not as concise as the second version because it requires more lines of code, but it is more informative than the second version because it tells us if x is less than, greater than, or equal to y.
def compare(x, y):
    if x == y:
        print("x is equal to y")
    else:    
        print("x is not equal to y")

def main():
    choice = input("Which version of compare do you want to use? (1 or 2) ")
    if choice == "1 - is less than, greater than, or equal to.":
        compare(x, y)
    elif choice == "2 - is equal or not equal.":
        compare(x, y)
    else:
        print("Invalid choice.")

main()

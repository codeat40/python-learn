x = input("what is x? ")

try:
    x = int(x)
except ValueError:
    print("x is not an integer")
else:
    print(f"x is {x}")

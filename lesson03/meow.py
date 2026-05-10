# meow.py
# Demonstrates: while True / break for input validation, for loop with range(), _ throwaway variable.

# Step 1: Keep asking until the user gives a positive integer.
# while True creates an intentional infinite loop — break exits it once the condition is met.
while True:
    n = int(input("What is n? "))

    if n > 0:
        break   # valid input received — exit the loop

# Step 2: Print "meow" exactly n times.
# _ is used instead of a named variable because the loop counter value is never needed.
for _ in range(n):
    print("meow")

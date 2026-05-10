# calculator.py
# This program asks the user for two numbers, adds them together, and prints the result.

"""
# The input() function is used to get input from the user. The string inside the parentheses is the prompt that will be displayed to the user.
# The input from the user is stored in the variables 'x' and 'y'.
# The int() function is used to convert the input from the user (which is a string) into an integer so that we can perform arithmetic operations on it.
# The result of adding 'x' and 'y' is stored in the variable 'z'.
# The print() function is used to output the result to the console.
"""

#version 1: using int() to convert the input to integers
# Ask the user for two numbers
print("\n" + "welcome to calculator.py" + "\n")
print("version 1: using int() to convert the input to integers")
x = input("what is x (use int)? ")
y = input("what is y (use int)? ")

z = int(x) + int(y)

print(z)

#version 2: using int() directly on the input() function
# Ask the user for two numbers
print("\n" + "version 2: using int() directly on the input() function" + "\n")
x = int(input("what is x (use int)? "))
y = int(input("what is y (use int)? "))

print(x + y)

#version 3 not recommended: using int() directly on the input() function without storing the values in variables
print("\n" + "version 3: using int() directly on the input() function without storing the values in variables" + "\n")
print(int(input("what is x (use int)? ")) + int(input("what is y (use int)? ")))

#floating point numbers
# Ask the user for two floating-point numbers
x = float(input("what is x (use float)? "))
y = float(input("what is y (use float)? "))

# The result of adding 'x' and 'y' is stored in the variable 'z'.
z = x + y

print("result of adding x and y:")
print(z)

#floating point numbers
# Ask the user for two floating-point numbers
x = float(input("what is x (use float)? "))
y = float(input("what is y (use float)? "))

# The round() function is used to round a number to a specified number of decimal places. In this case, we are rounding the result of adding x and y to the nearest integer (0 decimal places).
# The result of rounding the sum of x and y is stored in the variable 'z'.
z = round(x + y)

# The format specifier :, is used to format the number with commas as thousands separators. This makes it easier to read large numbers by grouping digits into thousands.
# syntax: {variable:format_specifier}
# In this case, the format specifier is :, which tells Python to format the number with commas as thousands separators. For example, if z is 1000000, it will be formatted as 1,000,000 when printed.
print("result of adding x and y rounded to the nearest integer with commas as thousands separators:")
print(f"{z:,}")

#floating point numbers
# Ask the user for two floating-point numbers
x = float(input("what is x (use float)? "))
y = float(input("what is y (use float)? "))

# The round() function is used to round a number to a specified number of decimal places. In this case, we are rounding the result of dividing x by y to the nearest integer (0 decimal places).
# The result of rounding the division of x by y is stored in the variable 'z'.
z = round(x / y)

# The format specifier .2f is used to format the number with 2 decimal places. This makes it easier to read decimal numbers.
# syntax: {variable:format_specifier}
# In this case, the format specifier is .2f, which tells Python to format the number with 2 decimal places. For example, if z is 1000000.123456, it will be formatted as 1000000.12 when printed.
print("result of dividing x by y rounded to 2 decimal places:")
print(f"{z:.2f}")

#using def to define a function that takes the user's name as an argument and prints a greeting. This allows us to reuse the code and makes it more organized.

"""
# The main() function is defined to encapsulate the code that performs the calculations. This allows
# us to call the main() function at the end of the script to execute the code. This is a common practice in Python to improve code organization and readability.
# By defining a main() function, we can also easily reuse the code in other contexts, such as importing this script as a module in another script. It also allows us to separate the logic of the program from the execution, making it easier to read and maintain.
# In this case, the main() function contains the code that asks the user for two floating-point numbers, performs the division, rounds the result, and prints it formatted to 2 decimal places.
# At the end of the script, we call the main() function to execute the code when the script is run.
# This structure is a common pattern in Python programming and is considered good practice for organizing code.
"""

def main():
    x = int(input("what is x (use int)? "))
    print(f"x squared is {square(x)}")

def square(n):
    return n ** 2 # this is the same as n * n and pow(n, 2)

main()
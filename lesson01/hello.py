# This is a simple Python program that asks for the user's name and then prints "hello world".

"""
# input() function is used to get input from the user. The string inside the parentheses is the prompt that will be displayed to the user.
# The input from the user is stored in the variable 'name'.
"""

# Ask the user for their name
name = input("what is your name? ")

"""
# The print() function is used to output text to the console. The f-string allows us to include the value of the variable 'name' in the output string.
# The f-string (formatted string) is used to format the output. The variable name is enclosed in curly braces {} and will be replaced with its value when the string is printed.
# end="" is used to prevent the print() function from adding a newline character at the end of the output. By default, print() adds a newline character after the output, but by setting end="" we can change this behavior and keep the output on the same line.
"""

# Say hello to the user
print(f"hello, {name}!", end="")

print("\n" + "welcome to hello.py" + "\n")

"""
# The following code demonstrates various string methods that can be used to manipulate the user's name. Each method is applied to the variable 'name' and the result is printed to the console.
# The methods used are:
# - upper(): converts all characters in the string to uppercase.
# - lower(): converts all characters in the string to lowercase.
# - title(): converts the first character of each word to uppercase and the rest to lowercase.
# - capitalize(): converts the first character of the string to uppercase and the rest to lowercase.
# - swapcase(): converts uppercase characters to lowercase and vice versa.
# - replace(): replaces all occurrences of a specified substring with another substring.
# - strip(): removes any leading and trailing whitespace from the string.
# Each method is applied to the variable 'name' and the result is printed to the console using an f-string.
"""

# Demonstrate various string methods

# Convert the name to uppercase
name = name.upper()
print(f"hello, {name}! Convert the name to uppercase")

# Convert the name to lowercase
name = name.lower()
print(f"hello, {name}! Convert the name to lowercase")

# Convert the name to title case
name = name.title()
print(f"hello, {name}! Convert the name to title case")

# Convert the name to capitalize case
name = name.capitalize()
print(f"hello, {name}! Convert the name to capitalize case")

# Replace all occurrences of "a" with "4"
name = name.replace("a", "4")
print(f"hello, {name}! Replace all occurrences of 'a' with '4'")

# Swap the case of the name
name = name.swapcase()
print(f"hello, {name}! Swap the case of the name")

# Remove leading and trailing whitespace
name = name.strip()
print(f"hello, {name}! Remove leading and trailing whitespace")

#version 4: using def to define a function that takes the user's name as an argument and prints a greeting. This allows us to reuse the code and makes it more organized.

"""
# The def keyword is used to define a function in Python. The function is named 'hello' and it takes one parameter, 'name'. The function prints a greeting using an f-string that includes the value of the 'name' parameter.
# The main() function is defined to get the user's name and call the hello() function with
# the user's name as an argument. The main() function is then called to execute the program.
# This structure allows us to separate the logic of getting user input and printing the greeting into different functions, making the code more organized and reusable.
"""

def hello(name):
    print(f"hello, {name}!")

def main():
    name = input("what is your name? ")
    hello(name)

main()

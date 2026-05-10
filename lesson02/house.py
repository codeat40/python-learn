name = input("What is the name of your house? ")

# this is original code, but it is not as concise as the code below because it requires more lines of code, but it is more informative than the code below because it tells us which house each character belongs to, but it is less concise than the code below because it requires more lines of code.

# if name.lower() == "Harry":
#     print("Gryffindor!")
# elif name.lower() == "Hermione":
#     print("Gryffindor!")
# elif name.lower() == "Ron":
#     print("Gryffindor!")
# elif name.lower() == "Draco":
#     print("Slytherin!")
# elif name.lower() == "Luna":
#     print("Ravenclaw!")
# elif name.lower() == "Neville":
#     print("Gryffindor!")
# elif name.lower() == "George":
#     print("Gryffindor!")
# elif name.lower() == "Fred":
#     print("Gryffindor!")
# else:
#     print("I don't know which house you belong to.")

# this is replacing the code above, but it is not as concise as the code below because it requires more lines of code, but it is more informative than the code below because it tells us which house each character belongs to, but it is less concise than the code below because it requires more lines of code.
# this is optimized code, but it is less informative than the code above because it doesn't tell us which house each character belongs to, it only tells us if the character belongs to Gryffindor or not, but it is more concise than the code above because it requires fewer lines of code.

# if name.lower() in ["harry", "hermione", "ron", "neville", "george", "fred"]:
#     print("Gryffindor!")
# elif name.lower() == "draco":
#     print("Slytherin!")
# elif name.lower() == "luna":
#     print("Ravenclaw!")
# else:
#     print("I don't know which house you belong to.") 

# using match case statements, but it is not as concise as the code below because it requires more lines of code, but it is more informative than the code below because it tells us which house each character belongs to, but it is less concise than the code below because it requires more lines of code.
# match method is more concise than the if statements because it requires fewer lines of code, but it is less informative than the if statements because it doesn't tell us which house each character belongs to, it only tells us if the character belongs to Gryffindor or not, but it is more concise than the if statements because it requires fewer lines of code.

match name.lower():
    case "harry" | "hermione" | "ron" | "neville" | "george" | "fred":
        print("Gryffindor!")
    case "draco":
        print("Slytherin!")
    case "luna":
        print("Ravenclaw!")
    case _:
        print("I don't know which house you belong to.")   
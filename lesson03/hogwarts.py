# list is a data structure in Python that can hold multiple items. It is ordered, changeable, and allows duplicate values. Lists are defined using square brackets [].
def list_function():
    students = ["harry", "hermione", "ron"]

    for student in students:
        print(student)

    print("list is a data structure in Python that can hold multiple items. It is ordered, changeable, and allows duplicate values. Lists are defined using square brackets [].")

# len() function returns the number of items in a list. In this case, it will return 3 because there are three students in the list.

def len_function():

    students = ["harry", "hermione", "ron"]

    for i in range(len(students)):
        print(i, students[i])
    
    print("len() function returns the number of items in a list. In this case, it will return 3 because there are three students in the list.")

# dict is a data structure in Python that can hold key-value pairs. It is unordered, changeable, and does not allow duplicate keys. Dictionaries are defined using curly braces {}.

def dict_function():

# this is basic matrix for students and their houses. It is a dictionary where the keys are the names of the students and the values are their houses. However, this is not a good way to represent this data because it does not allow us to store additional information about the students,
#    students = {
#        "harry": "gryffindor",
#        "hermione": "gryffindor",
#        "ron": "gryffindor",
#        "draco": "slytherin"
#    }

    students = [
        {"name": "harry", "house": "gryffindor", "age": 17, "gender": "male", "wand": "holly, phoenix feather", "patronus": "stag"},
        {"name": "hermione", "house": "gryffindor", "age": 17, "gender": "female", "wand": "walnut, dragon heartstring", "patronus": "otter"},
        {"name": "ron", "house": "gryffindor", "age": 17, "gender": "male", "wand": "hawthorn, unicorn hair", "patronus": "jack Russell terrier"},
        {"name": "draco", "house": "slytherin", "age": 17, "gender": "male", "wand": "yew, phoenix feather", "patronus": "dragon"}
    ]

    # this code below can be problematic because it assumes that the keys in the dictionary are the same as the values. In this case, it will print "harry gryffindor", "hermione gryffindor", and "ron gryffindor". However, if the values were different, it would not work as expected.
    # students = ["harry", "hermione", "ron"]
    # houses = ["gryffindor", "gryffindor", "gryffindor"]

    for student in students:
        print(student["name"], student["house"], student["age"], student["gender"], student["wand"], student["patronus"], sep=" | ")
    
    print("dict is a data structure in Python that can hold key-value pairs. It is unordered, changeable, and does not allow duplicate keys. Dictionaries are defined using curly braces {}.")

# this is an interface to run each function from main 

def main():

#which function do you want to run?
    choice = input("which function do you want to run? (list, len, dict) ")

    if choice == "list":
        list_function()
    elif choice == "len":
        len_function()
    elif choice == "dict":
        dict_function()
    else:
        print("invalid choice")

main()


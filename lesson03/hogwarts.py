# hogwarts.py
# Demonstrates: lists, len(), index-based iteration, dictionaries, list of dictionaries.

def list_function():
    # A list holds an ordered sequence of items in a single variable.
    # Defined with square brackets []. Items are zero-indexed.
    students = ["harry", "hermione", "ron"]

    # for loop iterates over each item — student holds the current value each time.
    for student in students:
        print(student)

def len_function():
    students = ["harry", "hermione", "ron"]

    # range(len(students)) generates indices 0, 1, 2 — one per item in the list.
    # Useful when you need both the index (i) and the value (students[i]) at the same time.
    for i in range(len(students)):
        print(i, students[i])

def dict_function():
    # --- Basic dictionary approach (simple but limited) ---
    # A dict maps keys to values. Keys must be unique.
    # students = {
    #     "harry": "gryffindor",
    #     "hermione": "gryffindor",
    #     "ron": "gryffindor",
    #     "draco": "slytherin"
    # }
    # Problem: only stores one value per student — cannot add age, wand, etc. without restructuring.

    # --- List of dictionaries (recommended pattern for multiple records) ---
    # Each dictionary is one complete record. Adding a new field means adding one key per dict,
    # not creating and synchronizing a separate parallel list.
    students = [
        {"name": "harry",    "house": "gryffindor", "age": 17, "gender": "male",   "wand": "holly, phoenix feather",      "patronus": "stag"},
        {"name": "hermione", "house": "gryffindor", "age": 17, "gender": "female", "wand": "walnut, dragon heartstring",   "patronus": "otter"},
        {"name": "ron",      "house": "gryffindor", "age": 17, "gender": "male",   "wand": "hawthorn, unicorn hair",       "patronus": "jack russell terrier"},
        {"name": "draco",    "house": "slytherin",  "age": 17, "gender": "male",   "wand": "yew, phoenix feather",         "patronus": "dragon"}
    ]

    # --- Why not parallel lists? ---
    # students = ["harry", "hermione", "ron"]
    # houses   = ["gryffindor", "gryffindor", "gryffindor"]
    # Problem: indices across two lists must be kept in sync manually — easy to break silently.

    # Iterate over the list; each `student` is a dict — access fields by key with student["key"].
    # sep=" | " passes a custom separator to print(), replacing the default space between arguments.
    for student in students:
        print(student["name"], student["house"], student["age"], student["gender"], student["wand"], student["patronus"], sep=" | ")

# Menu interface — lets the user choose which function to run.
def main():
    choice = input("Which function do you want to run? (list, len, dict) ")

    if choice == "list":
        list_function()
    elif choice == "len":
        len_function()
    elif choice == "dict":
        dict_function()
    else:
        print("Invalid choice.")

main()

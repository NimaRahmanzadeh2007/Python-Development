students = [
    {"name": "Ali", "family": "Rezaei", "class_number": 301},
    {"name": "Reza", "family": "Karimi", "class_number": 301},
    {"name": "Hossein", "family": "Rostami", "class_number": 303},
    {"name": "Mohammad", "family": "Jafari", "class_number": 302},
    {"name": "Mehdi", "family": "Gholami", "class_number": 303},
    {"name": "Amir", "family": "Najafi", "class_number": 301}
]


def find_student():
    found = False
    try:
        user_search = input("Enter the name of student: ")
        for i in students:
            if i["name"] == user_search:
                found = True
                print("student found!")
                print("info:")
                print(f"name: {i['name']}")
                print(f"family: {i['family']}")
                print(f"class number: {i['class_number']}")
                break
            else:
                found = False
        if found == False:
            print("student not found...")

    except:
        print("something went wrong, try again...\n")


find_student()

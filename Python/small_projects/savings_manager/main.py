from modules import *

while True:
    try:
        print("1. Calculate savings")
        print("2. Exit\n")
        print("------------------------")
        user_input = int(input("Enter your choice: "))

        match user_input:
            case 1:
                calculate_budget()
            case 2:
                print("Exiting the program. Goodbye!")
                break
            case _:
                print("Invalid input, please try again...\n")

    except ValueError:
        print("Invalid input! Please enter a number (1 or 2).\n")

    except Exception as e:
        print(f"Something went wrong: {e}\n")

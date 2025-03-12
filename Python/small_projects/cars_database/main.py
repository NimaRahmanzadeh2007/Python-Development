from module_car import Car

cars = Car()


while True:

    print("\n1. Show cars\n2. Add car\n3. Remove car\n4. Find car\n5. Exit")

    choice = input("Enter your choice: ")

    match choice:
        case "1":
            cars.show_cars()
        case "2":
            cars.add_car()
        case "3":
            cars.remove_car()
        case "4":
            cars.find_car()
        case "5":
            print("\nExiting the program")
            break
        case _:
            print("Invalid choice")

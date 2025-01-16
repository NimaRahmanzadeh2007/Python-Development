while True:

    user_input = input("\nEnter the color of TrafficLight(red, green, yellow): ")
    user_input = user_input.lower().strip()


    if user_input == "red" or user_input == "yellow" or user_input == "green":
        if user_input == "red":
            print("STOP!")
        elif user_input == "yellow":
            print("READY TO GO!")
        else:
            print("GO!")

    
    else:
        print('Wrong input!')

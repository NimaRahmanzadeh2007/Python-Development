while True:

    try:
        user_input = float(input("\nEnter the score of the student: "))

        if 0 <= user_input <= 100:
            if user_input >= 90:
                print("\ngreat!")
            elif user_input < 90 and user_input >= 70:
                print("\ngood.")
            elif user_input < 70 and user_input >= 50:
                print("\nneed more practice...")
            else:
                print("\nvery bad.....")
        else:
            print("\nnumber is out of the range (only between 0 and 100)...")
    
    except ValueError:
        print("\ninvalid input, try again...")


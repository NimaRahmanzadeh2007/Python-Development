while True:
    current_year = 1403

    user_birth = int(input("Enter your birth year: "))
    
    try:

        if(current_year < user_birth):
            print("wrong input!")
        else:
            print(f"you are {1403 - user_birth} years old")
    
    except:
        print("Somthing went wrong!")
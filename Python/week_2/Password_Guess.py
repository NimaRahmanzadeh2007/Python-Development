default_password = "python123"

tries = 3

while tries != 0:

    user_guess = input("\nguess the password: ")

    if user_guess.strip() == default_password:
        print("\nYou did it! You guessed the password!")
        break
    else:
        tries-=1
        if tries != 0:
            print("\noh no! you didn't guess the password! try again...")
            print(f"\nyou have {tries} tries now...")
        else:
            print(f"\nyou lost in guessing the password...\nbecause you have {tries} try...")
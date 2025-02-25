from random import randint

number = 0

def random_number_generate():
    global number
    number = randint(0, 101)

def guess_number():
    global number
    tries = 0

    if number == 0:
        print("Random number not generated yet! Generating now...")
        random_number_generate()

    while True:
        try:
            user_input = int(input("Guess the number between 0 and 100: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        tries += 1

        if number > user_input:
            print("More!")
        elif number < user_input:
            print("Less!")
        else:
            print("You guessed the number!")
            print(f"Tries = {tries}")
            break

import calculator.module as module

while True:

    print("Options:")
    print("1. +")
    print("2. -")
    print("3. *")
    print("4. /")
    print("5. sinus")
    print("6. cosinus")
    print("7. tangens")
    print("8. cotangens")
    user_selection = int(input("select one: "))

    match user_selection:

        case 1:
            module.Addition()

        case 2:
            module.Subtraction()

        case 3:
            module.Multiplication()

        case 4:
            module.Division()
            
        case 5:
            module.Sin()

        case 6:
            module.Cos()

        case 7:
            module.Tan()

        case 8:
            module.CoTan()

        case _:
            print("Invalid input\n")

import functions

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
            functions.Addition()

        case 2:
            functions.Subtraction()

        case 3:
            functions.Multiplication()

        case 4:
            functions.Division()
            
        case 5:
            functions.Sin()

        case 6:
            functions.Cos()

        case 7:
            functions.Tan()

        case 8:
            functions.CoTan()

        case _:
            print("Invalid input\n")

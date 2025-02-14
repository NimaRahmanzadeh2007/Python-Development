import math


def Addition():
    number_a = int(input("Enter the first number: "))
    number_b = int(input("Enter the second number: "))
    try:
        print(f"The result is: {number_a + number_b}\n")
    except:
        print("Invalid input\n")


def Subtraction():
    number_a = int(input("Enter the first number: "))
    number_b = int(input("Enter the second number: "))
    try:
        print(f"The result is: {number_a - number_b}\n")
    except:
        print("Invalid input\n")


def Multiplication():
    number_a = int(input("Enter the first number: "))
    number_b = int(input("Enter the second number: "))
    try:
        print(f"The result is: {number_a * number_b}\n")
    except:
        print("Invalid input\n")


def Division():
    number_a = int(input("Enter the first number: "))
    number_b = int(input("Enter the second number: "))
    try:
        print(f"The result is: {number_a / number_b}\n")
    except:
        print("Invalid input\n")


def Sin():
    number_a = int(input("Enter the number: "))
    try:
        number_a = float(number_a)
        print(f"The result is: {math.sin(math.radians(number_a))}\n")
    except:
        print("Invalid input\n")


def Cos():
    number_a = int(input("Enter the number: "))
    try:
        number_a = float(number_a)
        print(f"The result is: {math.cos(math.radians(number_a))}\n")
    except:
        print("Invalid input\n")


def Tan():
    number_a = int(input("Enter the number: "))
    try:
        number_a = float(number_a)
        print(f"The result is: {math.tan(math.radians(number_a))}\n")
    except:
        print("Invalid input\n")


def CoTan():
    number_a = int(input("Enter the number: "))
    try:
        number_a = float(number_a)
        print(f"The result is: {1/math.tan(math.radians(number_a))}\n")
    except:
        print("Invalid input\n")

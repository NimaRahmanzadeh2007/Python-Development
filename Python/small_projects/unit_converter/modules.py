def celsius_to_fahrenheit(celsius):
    try:
        result = celsius * 1.8 + 32
        print(f"{celsius} Celsius is {result} Fahrenheit\n")
    except:
        print("Something went wrong...\n")


def fahrenheit_to_celsius(fahrenheit):
    try:
        result = (fahrenheit - 32) / 1.8
        print(f"{fahrenheit} Fahrenheit is {result} Celsius\n")
    except:
        print("Something went wrong...\n")


def meter_to_feet(meter):
    try:
        result = meter * 3.2808399
        print(f"{meter} meters is {result} feet\n")
    except:
        print("Something went wrong...\n")


def feet_to_meter(feet):
    try:
        result = feet * 0.3048
        print(f"{feet} feet is {result} meters\n")
    except:
        print("Something went wrong...\n")


def kilogram_to_pound(kilogram):
    try:
        result = kilogram * 2.2046
        print(f"{kilogram} kilograms is {result} pounds\n")
    except:
        print("Something went wrong...\n")


def pound_to_kilogram(pound):
    try:
        result = pound * 0.4536
        print(f"{pound} pounds is {result} kilograms\n")
    except:
        print("Something went wrong...\n")


def second_to_minute_and_hour(second):
    try:
        hour = second // 3600
        second %= 3600

        minute = second // 60
        second %= 60

        print(f"{hour} hours, {minute} minutes, and {second} seconds\n")
    except:
        print("Something went wrong...\n")

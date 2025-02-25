from modules import *

while True:
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Meter to Feet")
    print("4. Feet to Meter")
    print("5. Kilogram to Pound")
    print("6. Pound to Kilogram")
    print("7. Second to Minute and Hour")
    print("8. Exit\n")
    print("------------------------")
    user_input = int(input("Enter your choice: "))

    match(user_input):
        case 1:

            celsius = float(input("Enter temperature in Celsius: "))
            celsius_to_fahrenheit(celsius)
            

        case 2:

            fahrenheit = float(input("Enter temperature in Fahrenheit: "))
            fahrenheit_to_celsius(fahrenheit)
            

        case 3:

            meter = float(input("Enter length in meter: "))
            meter_to_feet(meter)
            

        case 4:

            feet = float(input("Enter length in feet: "))
            feet_to_meter(feet)
            

        case 5:

            kilogram = float(input("Enter weight in kilogram: "))
            kilogram_to_pound(kilogram)
            

        case 6:

            pound = float(input("Enter weight in pound: "))
            pound_to_kilogram(pound)
            

        case 7:

            second = int(input("Enter time in second: "))
            second_to_minute_and_hour(second)
            

        case 8:

            exit()

        case _:

            print("inalid input...")
            
import sqlite3


class Car:

    def __init__(self):

        with sqlite3.connect("cars_database/cars.db") as conn:

            c = conn.cursor()

            c.execute("""CREATE TABLE IF NOT EXISTS cars (
                      name TEXT NOT NULL,
                      model TEXT NOT NULL,
                      year INTEGER NOT NULL
                      )""")

            conn.commit()

    def show_cars(self):

        with sqlite3.connect("cars_database/cars.db") as conn:

            c = conn.cursor()

            c.execute("SELECT * FROM cars")

            all_cars = c.fetchall()

            for i in all_cars:

                print(f"\nname: {i[0]} / model: {i[1]} / year: {i[2]}")

    def add_car(self):

        self.car_name = input("Enter the car name: ").strip().capitalize()
        self.car_model = input("Enter the car model: ").strip().capitalize()
        self.car_year = int(input("Enter the car year: "))

        with sqlite3.connect("cars_database/cars.db") as conn:

            c = conn.cursor()

            c.execute("INSERT INTO cars VALUES (?,?,?)",
                      (self.car_name, self.car_model, self.car_year))

            conn.commit()

            print(f"\n{self.car_name} {self.car_model} added to the database")

    def remove_car(self):

        self.car_name = input("Enter the car name: ").strip().capitalize()
        self.car_model = input("Enter the car model: ").strip().capitalize()
        self.car_year = int(input("Enter the car year: "))

        with sqlite3.connect("cars_database/cars.db") as conn:

            c = conn.cursor()

            c.execute("SELECT * FROM cars WHERE name = ? AND model = ? AND year = ?",
                      (self.car_name, self.car_model, self.car_year))

            exists = c.fetchone()

            if exists:
                c.execute("DELETE FROM cars WHERE name = ? AND model = ? AND year = ?",
                          (self.car_name, self.car_model, self.car_year))

                conn.commit()
                print(
                    f"\n{self.car_name} {self.car_model} removed from the database")

            else:
                print(
                    f"\n{self.car_name} {self.car_model} not found in the database")

    def find_car(self):

        self.car_name = input("Enter the car name: ").strip().capitalize()
        self.car_model = input("Enter the car model: ").strip().capitalize()
        self.car_year = int(input("Enter the car year: "))

        with sqlite3.connect("fifth_program/cars.db") as conn:

            c = conn.cursor()

            c.execute("SELECT * FROM cars WHERE name = ? AND model = ? AND year = ?",
                      (self.car_name, self.car_model, self.car_year))

            exists = c.fetchone()

            if exists:
                print(
                    f"\n{self.car_name} {self.car_model} found in the database")

            else:
                print(
                    f"\n{self.car_name} {self.car_model} not found in the database")

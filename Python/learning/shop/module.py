import json


class Shop:

    def __init__(self, file_path):
        self.file_path = file_path
        with open(self.file_path, 'r') as file:
            self.shop = json.load(file)


# def load_db():
#     with open('data.json', 'r') as file:
#         return json.load(file)

    def add_product(self):
        while True:
            try:
                product_name = input("Enter the name of the product: ")
                product_price = int(
                    input(f"Enter the price of the {product_name}: "))
                new_data = {'name': product_name, 'price': product_price}
                self.shop.append(new_data)
                print(
                    f"{product_name} with price: {product_price} added successfully...\n")
                break
            except:
                print("something went wrong, try again...\n")

    def find_product(self):
        found = False
        try:
            user_search = str(input("Enter the name of the product: "))
            for i in self.shop:
                if i['name'] == user_search:
                    found = True
                    print("product found!")
                    print("info:")
                    print(f"name: {i['name']}\nprice: {i['price']}\n")
                    break
                else:
                    found = False

            if found == False:
                print("product not found!\n")

        except:
            print("something went wrong, try again...\n")

    def remove_product(self):
        deleted = False
        try:
            user_search = input("Enter the name of the product: ")
            for i in self.shop:
                if i["name"] == user_search:
                    self.shop.remove(i)
                    deleted = True
            if deleted == False:
                print("product not found!\n")
            else:
                print("Product has been deleted successfully.\n")

        except:
            print("something went wrong, try again...\n")

    def update_product(self):
        found = False
        try:
            user_search = str(input("Enter the name of the product: "))
            for i in self.shop:
                if i['name'] == user_search:
                    found = True
                    print("product found!")
                    print("info:")
                    print(f"name: {i['name']}\nprice: {i['price']}\n")
                    new_name = input("Enter the new name of the product: ")
                    new_price = int(
                        input("Enter the new price of the product: "))
                    new_data = {'name': new_name, 'price': new_price}
                    i.update(new_data)
                    print("product updated successfully...\n")
                    break
                else:
                    found = False

            if found == False:
                print("product not found!\n")

        except:
            print("something went wrong, try again...\n")

    def save_db(self):
        with open(self.file_path, 'w') as file:
            json.dump(self.shop, file)
            return "data saved successfully...\n"

    def show_db(self):
        for i in self.shop:
            print(f"name: {i['name']}, price: {i['price']}")
        print("\n")

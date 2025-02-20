import json


def load_db():
    with open('shop/data.json', 'r') as file:
        return json.load(file)


def add_product(products):
    while True:
        try:
            product_name = input("Enter the name of the product: ")
            product_price = int(
                input(f"Enter the price of the {product_name}: "))
            new_data = {'name': product_name, 'price': product_price}
            products.append(new_data)
            print(
                f"{product_name} with price: {product_price} added successfully...\n")
            break
        except:
            print("something went wrong, try again...\n")

    return products


def find_product(products):
    found = False
    try:
        user_search = str(input("Enter the name of the product: "))
        for i in products:
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


def remove_product(products):
    deleted = False
    try:
        user_search = input("Enter the name of the product: ")
        for i in products:
            if i["name"] == user_search:
                products.remove(i)
                deleted = True
        if deleted == False:
            print("product not found!\n")
        else:
            print("Product has been deleted successfully.\n")

    except:
        print("something went wrong, try again...\n")

    return products


def update_product(products):
    found = False
    try:
        user_search = str(input("Enter the name of the product: "))
        for i in products:
            if i['name'] == user_search:
                found = True
                print("product found!")
                print("info:")
                print(f"name: {i['name']}\nprice: {i['price']}\n")
                new_name = input("Enter the new name of the product: ")
                new_price = int(input("Enter the new price of the product: "))
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

    return products


def save_db(products):
    with open('shop/data.json', 'w') as file:
        json.dump(products, file)
        return "data saved successfully!"


def show_db(products):
    for i in products:
        print(f"name: {i['name']}, price: {i['price']}")
    print("\n")

products = [
    {
        "name": "shampo",
        "price": 180,
    },
    {
        "name": "meat",
        "price": 800,
    },
    {
        "name": "coca-cola",
        "price": 60,
    },
    {
        "name": "cocoa milk",
        "price": 15,
    },
    {
        "name": "rangarang",
        "price": 5,
    },
]


def add_product():
    while True:
        try:
            product_name = input("Enter the name of the product: ")
            product_price = int(
                input(f"Enter the price of the {product_name}: "))
            products.append(dict(name=product_name, price=product_price))
            print(
                f"{product_name} with price: {product_price} added successfully...\n")
            break
        except:
            print("something went wrong, try again...\n")


def find_product():
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


def remove_product():
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


def update_product():
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
                i.update({'name': new_name, 'price': new_price})
                print("product updated successfully...\n")
                break
            else:
                found = False

        if found == False:
            print("product not found!\n")

    except:
        print("something went wrong, try again...\n")


while True:
    try:
        print("1.add product")
        print("2.find product")
        print("3.remove product")
        print("4.update product")
        print("-----------------------")
        user_input = int(input("Choose one(enter the number):"))

        match user_input:
            case 1:

                add_product()
            case 2:

                find_product()
            case 3:

                remove_product()
            case 4:

                update_product()

            case _:
                print("invalid input...\n")
    except:
        print("something went wrong, try again...\n")

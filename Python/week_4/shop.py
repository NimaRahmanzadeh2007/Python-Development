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
            print(f"{product_name} with price: {product_price} added successfully...")
            break
        except:
            print("something went wrong, try again...")


def find_product():
    try:
        user_search = input("Enter the name of the product: ")
        for i in products:
            if i["name"] == user_search:
                print("product found!")
                print("info:")
                print(f"name: {i['name']}\nprice: {i['price']}")
        print("product not found!")
    except:
        print("something went wrong, try again...")


def remove_product():
    try:
        user_search = input("Enter the name of the product: ")
        for i in products:
            if i["name"] == user_search:
                products.remove(i)
                print("Product has been deleted successfully.")
                return
        print("product not found!")

    except:
        print("something went wrong, try again...")


# remove_product()
print(products)

# add_product()

# print(products)

# find_product()

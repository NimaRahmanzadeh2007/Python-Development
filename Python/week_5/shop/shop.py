import module


products = list()

products = module.load_db()

while True:
    try:
        print("1.add product")
        print("2.find product")
        print("3.remove product")
        print("4.update product")
        print("5.save database")
        print("6.show database")  
        print("-----------------------")
        user_input = int(input("Choose one(enter the number):"))

        match user_input:
            case 1:

                products = module.add_product(products)
            case 2:

                module.find_product(products)
            case 3:

                module.remove_product(products)
            case 4:

                products = module.update_product(products)
            case 5:

                module.save_db(products)
            case 6:

                module.show_db(products)

            case _:
                print("invalid input...\n")
    except:
        print("something went wrong, try again...\n")

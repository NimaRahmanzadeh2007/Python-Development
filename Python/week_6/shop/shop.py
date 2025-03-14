from module import Shop


products = Shop('shop/data.json')

while True:
    try:
        print("1.add product")
        print("2.find product")
        print("3.remove product")
        print("4.update product")
        print("5.save database")
        print("6.show database")
        print("7.exit")
        print("-----------------------")
        user_input = int(input("Choose one(enter the number):"))

        match user_input:
            case 1:

                products.add_product()
            case 2:

                products.find_product()
            case 3:

                products.remove_product()
            case 4:

                products.update_product()
            case 5:

                products.save_db()
            case 6:

                products.show_db()
            case 7:

                print("exiting...")
                break

            case _:
                print("invalid input...\n")
    except:
        print("something went wrong, try again...\n")

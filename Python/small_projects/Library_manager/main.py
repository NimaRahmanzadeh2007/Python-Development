import modules

books = []

books = modules.load_db()

while True:
    print("1. Add a book")
    print("2. Find a book")
    print("3. Show all books")
    print("4. Delete a book")
    print("5. Exit")
    user_input = input("Enter your choice: ")

    match user_input:

        case "1":

            books = modules.add_book(books)

        case "2":

            modules.find_book(books)

        case "3":

            modules.show_books(books)

        case "4":

            books = modules.delete_book(books)

        case "5":

            modules.save_db(books)
            break

        case _:
            print("Invalid choice!")

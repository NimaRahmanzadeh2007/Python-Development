import json


def load_db():
    with open("library/books.json", 'r') as file:
        return json.load(file)


def save_db(books):
    with open("library/books.json", 'w') as file:
        json.dump(books, file)


def add_book(books):
    subject = input("Enter the subject: ")
    writer = input("Enter the writer: ")
    year = int(input("Enter the year: "))
    new_book = {"subject": subject, "writer": writer, "year": year}
    books.append(new_book)
    return books


def find_book(books):
    founded_books = []
    user_input = input("Enter the subject or writer: ")
    for i in books:
        if i["subject"] == user_input or i["writer"] == user_input:
            founded_books.append(i)
    if len(founded_books) == 0:
        print("No book found!")
    else:
        print(f"founded books are:\n{founded_books}")


def show_books(books):
    if len(books) != 0:
        for i in books:
            print(
                f"Subject: {i['subject']}, Writer: {i['writer']}, Year: {i['year']}")
    else:
        print("No book found!")


def delete_book(books):
    user_input = input("Enter the subject:")
    for i in books:
        if i["subject"] == user_input:
            books.remove(i)
            print("Book deleted!")
            return books
    print("No book found!")

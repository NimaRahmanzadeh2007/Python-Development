from module_song import Songify


songs = Songify()

while True:
    print("1. Search by name")
    print("2. Search by type")
    print("3. Search by artist")
    print("4. show all")
    print("5. Exit")
    print("--------------------")

    user_input = input("Enter your choice: ").strip()

    match user_input:
        case "1":
            songs.search_by_name()
        case "2":
            songs.search_by_type()
        case "3":
            songs.search_by_artist()
        case "4":
            songs.show_songs()
        case "5":
            print("Goodbye")
            break

        case _:
            print("Invalid choice")

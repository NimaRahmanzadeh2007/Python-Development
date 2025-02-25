from modules import *

todo_list = list()

todo_list = load_db()

while True:
    print("1. add todo")
    print("2. remove todo")
    print("3. show list")
    print("4. check todo")
    print("5. save")
    print("6. exit")
    print()
    print("--------------------")
    print()
    user_input = int(input("enter the number: "))
    try:
        match(user_input):

            case 1:
                add_todo(todo_list)
            
            case 2:
                remove_todo(todo_list)

            case 3:
                show_list(todo_list)

            case 4:
                check_todo(todo_list)

            case 5:
                save_db(todo_list)

            case 6:
                exit()
            
            case _:
                print("invalid input...")
    
    except:
        print("invalid input...")
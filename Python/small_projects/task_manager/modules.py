import json


def load_db():
    with open("task_manager/data.json", 'r') as file:
        return json.load(file)


def save_db(todo_list):
    with open("task_manager/data.json", 'w') as file:
        json.dump(todo_list, file)
        print("saved successfully...\n")


def add_todo(todo_list):
    try:
        title = input("enter the title: ")
        checked = False
        print()
        new_todo = {"title": title, "checked": checked}
        todo_list.append(new_todo)
        print("added successfully...\n")

    except:
        print("something went wrong...\n")


def remove_todo(todo_list):

    try:
        title = input("enter the title: ")
        for item in todo_list:
            if item['title'] == title:
                todo_list.remove(item)
                print("deletd successfully...\n")
                break
    except:
        print("something went wrong...\n")


def show_list(todo_list):
    print()
    for item in todo_list:
        print(
            f"title: {item['title']}\nchecked: {item['checked']}\n----------")


def check_todo(todo_list):
    try:

        title = input("enter the title: ")
        found = False

        for item in todo_list:
            if item['title'] == title:

                found = True

                check = input("check: y / n ?")

                if check.lower().strip() == 'y':

                    item['checked'] = True
                    print("checked successfully\n")

                elif check.lower().strip() == 'n':

                    item['checked'] = False
                    print("unchecked successfully\n")

                else:

                    print("invalid input, try again...\n")
                    return
        if not found:    
            print("not found...\n")

    except:
        print("something went wrong...\n")

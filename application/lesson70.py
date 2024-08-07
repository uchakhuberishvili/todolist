# To do task


tasks = []

def add_task(task):
    tasks.append(task)
    print("Task added:",task)

def delete_task(tasks_number):
    tasks_number = int(tasks_number)
    if 1 <= tasks_number <= len(tasks):
        task = tasks.pop(tasks_number - 1)
        print("Task Deleted:", task)
    else:
        print("Incorrect Task Number")

def tasks_view():
    if not tasks:
        print("No Tasks In The List")
    else:
        print("Tasks:")
        index = 1
        for i in tasks:
            print(f"{index}. {i}")
            index += 1


while True:
    print("Options: ")
    print("Enter   'add'   To Add A Task")
    print("Enter   'delete'   To Delete A Task")
    print("Enter   'view'   To View Tasks")
    print("Enter   'exit'   To Exit The Program")

    user_input = input("Enter: ").lower()

    if user_input == "exit":
        break

    elif user_input == "add":
        task = input("Enter A Task: ")
        add_task(task)

    elif user_input == "delete":
        task_number = int(input("Enter The Task Number: "))
        delete_task(task_number)

    elif user_input == "view":
        tasks_view()

    else:
        print("Invalid Option. Please Try Again.")
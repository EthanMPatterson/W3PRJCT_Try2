from wrappers import ToDoList
from wrappers import Tasks 

def run_taskmanager():
    print("Menue:")
    print("\n1. Add a new task")
    print("\n2. View a task")
    print("\n3. View all tasks")
    print("\n4. Mark task as completed/incomplete")
    print("\n5. Edit a task description or ID")
    print("\n6. Quit")
    my_list = ToDoList()
    while True: 
        selection = input('Choose a menue option to select')
        if selection == '1':
            id = input('Enter a unique task ID or name')
            description = input('Enter a task description')
            my_list.add_task(id, description)
        elif selection == '2':
            id = input('Enter a task ID (name) to view the task details')
            my_list.view_task_details(id)
        elif selection == '3':
            my_list.view_tasks()
        elif selection == '4':
            id = input('Enter a task ID to mark as completed/incomplete: ')
            my_list.complete_uncomplete(id)
        elif selection == '5':
            id = input('Enter a task ID to edit: ')
            my_list.edit_task(id)
        elif selection == '6':
            print("Exiting task manager")
            break 
        else: 
            print('Invalid selection. Please enter a menue selection between 1 and 6')

if __name__ == "__main__":
    run_taskmanager()
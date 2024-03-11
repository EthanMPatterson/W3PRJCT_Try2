class Tasks:
    def __init__(self, id, description):
        self.id = id 
        self.description = description
        self.completed = False
    def task_data(self):
        if self.completed:
            status = 'Completed'
        else: status = 'Uncomplete'
        return f"ID: {self.id}, Description: {self.description}, Status: {status}"

class ToDoList:
    def __init__(self):
        self.tasks = []


    def add_task(self, id, description):
        task = Tasks(id, description)
        self.tasks.append(task)
        print(f"Task: {id} added witha description of {description}")
    
    def view_tasks(self):
        for task in self.tasks:
            print(task.task_data())
        else: 
            print('No tasks found')

    def complete_uncomplete(self, id):
        for task in self.tasks:
            if task.id == id:
                task.completed = not task.completed
            if task.completed:
                print(f"Task: {id} has been marked complete")
            else: 
                print(f"Task: {id} has been marked incomplete")
    
    def edit_task(self, id):
        for task in self.tasks:
            if task.id == id:
                print("What would you like to edit?")
                print("1. Task ID")
                print("2. Task Description")
            choice = input("Enter your choice (1 or 2) ")
            if choice == "1":
                new_id = input('Enter a new task ID ')
                task.id = new_id
                print(f"Task ID successfully changed to {new_id}")
            elif choice == "2":
                new_description = input('Enter a new task description ')
                task.description = new_description
                print(f"Task description successfully updated to {new_description}")
            else:
                print("Invalid choice.")
            return
    print("Task not found.")
            
    def view_task_details(self, id):
        for task in self.tasks:
            if task.id == id:
                print(task.task_data())
                return
    print("Task not found.")
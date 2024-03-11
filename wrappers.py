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
                print(task)

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
                print(task)
        new_id = input('Enter a new task ID')
        for task in self.tasks:
            if new_id != task.id:
                task.id = new_id
            print(f"Task ID successfully changed to {new_id} ")
            
    def view_task_details(self, id):
        for task in self.tasks:
            if task.id == id:
                print(task.task_data())
                return
    print("Task not found.")
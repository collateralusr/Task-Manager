class Task:
    def __init__(self, title, description, status='To Do'):
        self.title = title
        self.description = description
        self.status = status

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def display_tasks(self):
        for index, task in enumerate(self.tasks, start=1):
            print(f"{index}. {task.title} - {task.status}")

if __name__ == "__main__":
    task_manager = TaskManager()

    while True:
        print("\nTask Manager Menu:")
        print("1. Add Task")
        print("2. Display Tasks")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            new_task = Task(title, description)
            task_manager.add_task(new_task)
            print("Task added successfully!")

        elif choice == '2':
            print("\nTask List:")
            task_manager.display_tasks()

        elif choice == '3':
            print("Exiting Task Manager. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

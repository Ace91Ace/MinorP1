# task_manager.py

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task_name):
        self.tasks = [task for task in self.tasks if task.name != task_name]

    def list_tasks(self):
        for task in self.tasks:
            print(task)

    def run_tasks(self):
        for task in self.tasks:
            task.execute()

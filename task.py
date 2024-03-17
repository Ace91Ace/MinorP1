# task.py

class Task:
    def __init__(self, name, description, action, schedule):
        self.name = name
        self.description = description
        self.action = action
        self.schedule = schedule

    def __str__(self):
        return f"Task: {self.name}\nDescription: {self.description}\nSchedule: {self.schedule}"

    def execute(self):
        print(f"Executing task: {self.name}")
        self.action()
        print(f"Task '{self.name}' completed.")

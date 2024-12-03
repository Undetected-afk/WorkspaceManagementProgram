from Node import Node

class TaskDatabase:
    def __init__(self):
        self.tasks = []

    def add_task(self, task_name):
        task = TaskNode(task_name)
        self.tasks.append(task)
        return task

    def __str__(self):
        return f"Tasks: {', '.join([task.data for task in self.tasks])}"

class TaskNode(Node):
    def __init__(self, task_name):
        super().__init__(task_name)
        self.dependencies = []

    def add_dependency(self, task):
        self.dependencies.append(task)

    def __repr__(self):
        return f"Task({self.data}), Dependencies: {len(self.dependencies)}"

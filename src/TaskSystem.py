from Node import Node

class TaskNode(Node):
    def __init__(self, data):
        super().__init__(data)
        self.status = "not_started"  # Possible statuses: not_started, in_progress, completed
        self.dependencies = []  # Tasks that need to be completed before this task can start
        self.dependents = []  # Tasks that depend on this task being completed

    def add_dependency(self, task):
        if task not in self.dependencies:
            self.dependencies.append(task)
            task.dependents.append(self)
        else:
            print(f"Task '{task.data}' is already a dependency of '{self.data}'.")

    def complete(self):
        # Check if all dependencies are completed before marking this task as complete
        if all(dep.status == "completed" for dep in self.dependencies):
            self.status = "completed"
            print(f"Task '{self.data}' is now completed.")
        else:
            print(f"Task '{self.data}' cannot be completed as its dependencies are not finished.")

    def __repr__(self):
        return f"Task({self.data}, Status: {self.status}, Dependencies: {len(self.dependencies)})"

class TaskDatabase:
    def __init__(self):
        self.tasks = []

    def add_task(self, task_name):
        task = TaskNode(task_name)
        self.tasks.append(task)
        return task

    def __str__(self):
        return f"Tasks: {', '.join([task.data for task in self.tasks])}"

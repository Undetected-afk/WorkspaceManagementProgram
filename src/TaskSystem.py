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
    def __init__(self, data, priority=1, deadline=None, status="not_started"):
        super().__init__(data)
        self.priority = priority
        self.deadline = deadline
        self.status = status  # Task status
        self.connections = []

    def add_connections(self, node):
        if node == self:
            raise ValueError("A task cannot depend on itself.")
        if node in self.connections:
            raise ValueError(f"Task {node.data} already connected to {self.data}")
        self.connections.append(node)

    def __repr__(self):
        return f"Task({self.data}, Priority: {self.priority}, Deadline: {self.deadline}, Status: {self.status})"


# Node.py
class Node:
    def __init__(self, data=None):
        self.data = data  # This could be any data, like a name or any other attribute
        self.name = data  # Store the name as well for easier access (assuming the name is passed as data)

    def __repr__(self):
        return f"Node({self.name})"  # Show the name for clarity

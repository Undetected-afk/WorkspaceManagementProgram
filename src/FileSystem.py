# FileSystem.py
from Node import Node

class FolderNode(Node):
    def __init__(self, name):
        super().__init__(name)  # Initialize the Node (parent class) with the name attribute
        self.files = []  # List to hold files in this folder

    def add_file(self, file):
        self.files.append(file)

    def __repr__(self):
        return f"Folder({self.name})"  # This ensures the folder's name is displayed

class FileNode(Node):
    def __init__(self, name, data=None):
        super().__init__(name)  # Initialize the parent Node class with the file name
        self.data = data  # Store optional extra data for the file (can be used later)

    def __repr__(self):
        return f"File({self.name})"  # This ensures the file's name is displayed

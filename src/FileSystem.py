# FileSystem.py
from Node import Node

class FolderNode(Node):
    def __init__(self, name):
        super().__init__(name)  # Initialize with name
        self.files = []  # List to hold files in this folder

    def add_file(self, file):
        self.files.append(file)

    def __repr__(self):
        return f"Folder({self.name})"

class FileNode(Node):
    def __init__(self, name, data=None):
        super().__init__(data)  # Initialize with optional extra data (could be used later)
        self.name = name  # Store the file name separately

    def __repr__(self):
        return f"File({self.name})"

from Node import Node

class FolderNode(Node):
    def __init__(self, name):
        super().__init__(name)
        self.files = []

    def add_file(self, file):
        self.files.append(file)

class FileNode(Node):
    def __init__(self, name, data=None):
        super().__init__(data)
        self.name = name

# FileSystemDriver.py
from FileSystem import FolderNode, FileNode

# Create folders and files
folder1 = FolderNode("Documents")
folder2 = FolderNode("Downloads")

file1 = FileNode("file1.txt")
file2 = FileNode("file2.txt")
file3 = FileNode("file3.pdf")

# Add files to folders
folder1.add_file(file1)
folder1.add_file(file2)

folder2.add_file(file3)

# Print folder information
print(f"Folder: {folder1.name}, Files: {[file.name for file in folder1.files]}")
print(f"Folder: {folder2.name}, Files: {[file.name for file in folder2.files]}")

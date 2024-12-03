from FileSystem import FolderNode, FileNode

# Create folder and file structure
folder1 = FolderNode("Folder 1")
file1 = FileNode("File 1")
folder1.add_file(file1)

print(f"Folder: {folder1.name}, Files: {[file.name for file in folder1.files]}")

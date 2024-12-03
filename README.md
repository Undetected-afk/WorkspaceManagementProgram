# Workspace Management Program

## Overview
The Workspace Management Program is designed to manage tasks, files, and budgets in a workspace environment. The project is organized into three primary systems:
1. **Task Management System** (using graphs)
2. **Workspace File System** (using trees)
3. **Budget Management System** (using trees)

## Features
- Manage tasks and their dependencies.
- Organize files into a hierarchical system of folders and files.
- Manage budgets for different departments with transaction tracking.

## Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/WorkspaceManagementProgram.git

## Project Structure

WorkspaceManagementProgram/ │ ├── src/ # Source code directory │ ├── Node.py # Base Node class for all systems │ ├── FileSystem.py # File system classes (FolderNode, FileNode) │ ├── FileSystemDriver.py # Driver script for file system functionality │ ├── TaskSystem.py # Task management classes (TaskDatabase, TaskNode) │ ├── TaskSystemDriver.py # Driver script for task management functionality │ ├── BudgetSystem.py # Budget management classes (DepartmentNode, BudgetNode) │ ├── BudgetSystemDriver.py # Driver script for budget management functionality ├── README.md # Project overview and instructions


### Systems Overview

#### 1. **Task Management System**
   - This system tracks tasks and their dependencies. Tasks are represented as nodes in a graph, with each task potentially depending on others.
   - The `TaskDatabase` class manages all tasks, while the `TaskNode` class represents individual tasks.
   - Dependencies are modeled by connecting `TaskNode` instances to each other.

#### 2. **File System**
   - This system models a file system where files are organized into folders. The file system is represented as a tree of `FolderNode` and `FileNode` objects.
   - The `FolderNode` class represents a folder, while the `FileNode` class represents an individual file.
   - Files can be added to folders using the `add_file()` method in `FolderNode`.

#### 3. **Budget Management System**
   - This system handles workspace budgets for different departments. Budgets are represented as nodes in a tree structure, with each department having a budget node and transaction nodes under it.
   - The `DepartmentNode` class represents a department, while the `BudgetNode` class represents its budget.
   - Transaction nodes represent individual transactions for each department.

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Undetected-afk/WorkspaceManagementProgram.git


## Code Explanation

   - Node.py: Contains the base Node class. Other classes (task, file, and budget) inherit from this base class to implement their respective behaviors.
   - FileSystem.py: Defines the FolderNode and FileNode classes for representing the file system structure. The FolderNode class handles file storage, while the FileNode class handles individual files.
   - TaskSystem.py: Defines the TaskDatabase and TaskNode classes for managing tasks and dependencies. The TaskDatabase class stores tasks, and the TaskNode class represents a task with potential dependencies.
   - BudgetSystem.py: Defines classes for managing budgets (DepartmentNode and BudgetNode) and handling transactions for departments in the workspace.

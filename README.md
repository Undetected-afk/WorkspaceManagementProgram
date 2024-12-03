# Workspace Management Program

## Overview
The Workspace Management Program is a Python-based application designed to help manage and organize key elements of a workspace. It consists of three main systems: a Task Management System that tracks tasks and their dependencies, ensuring they are completed in the correct order; a File System that organizes files into folders, allowing users to efficiently manage and retrieve files; and a Budget Management System that helps manage department budgets, track transactions, and monitor financial allocations. Together, these components provide a comprehensive solution for organizing tasks, files, and finances within a workspace, making it easier to manage and optimize daily operations:
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

### Project Directory Structure

- **src/**: The source code directory where all Python scripts for the project are stored.
  - **Node.py**: Contains the base `Node` class that is used for all components (task system, file system, and budget system).
  - **FileSystem.py**: Contains classes related to the file system (`FolderNode` and `FileNode`) to model the directory and files structure.
  - **FileSystemDriver.py**: A driver script to test and demonstrate the functionality of the file system.
  - **TaskSystem.py**: Contains classes for managing tasks and task dependencies (e.g., `TaskDatabase`, `TaskNode`).
  - **TaskSystemDriver.py**: A driver script to test and demonstrate the functionality of the task management system.
  - **BudgetSystem.py**: Contains classes for managing budgets and departments (`DepartmentNode`, `BudgetNode`, etc.).
  - **BudgetSystemDriver.py**: A driver script to test and demonstrate the functionality of the budget management system.
- **README.md**: The project overview, installation instructions, and usage guide.


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

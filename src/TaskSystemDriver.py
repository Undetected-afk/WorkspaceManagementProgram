from TaskSystem import TaskDatabase

# Create task database
db = TaskDatabase()

# Add tasks
t1 = db.add_task("Task 1")
t2 = db.add_task("Task 2")
t3 = db.add_task("Task 3")

# Add dependencies
t3.add_dependency(t2)
t2.add_dependency(t1)

# Print the database
print(db)

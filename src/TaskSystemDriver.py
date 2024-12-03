from TaskSystem import TaskDatabase

# Create task database
db = TaskDatabase()

# Add tasks
t1 = db.add_task("Task 1")
t2 = db.add_task("Task 2")
t3 = db.add_task("Task 3")

# Add dependencies
t3.add_dependency(t2)  # Task 3 depends on Task 2
t2.add_dependency(t1)  # Task 2 depends on Task 1

# Try completing tasks
print("Attempting to complete Task 3 (should fail):")
t3.complete()  # Should fail because Task 1 and Task 2 are not completed

print("\nCompleting Task 1:")
t1.status = "completed"  # Manually marking Task 1 as completed

print("\nAttempting to complete Task 3 (should fail again):")
t3.complete()  # Should fail because Task 2 is not completed yet

print("\nCompleting Task 2:")
t2.status = "completed"  # Manually marking Task 2 as completed

print("\nAttempting to complete Task 3 (should succeed now):")
t3.complete()  # Now Task 3 should be able to be completed

# Print the task database
print("\nTask Database:")
print(db)

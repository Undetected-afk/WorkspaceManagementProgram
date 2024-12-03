from BudgetSystem import DepartmentNode, BudgetNode

# Create department and budget system
dept = DepartmentNode("Marketing")
budget = BudgetNode(5000)
dept.set_budget(budget)

print(f"Department: {dept.data}, Budget: {dept.budget.data}")

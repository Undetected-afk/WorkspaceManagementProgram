from Node import Node

class DepartmentNode(Node):
    def __init__(self, department_name):
        super().__init__(department_name)
        self.budget = None

    def set_budget(self, budget):
        self.budget = budget

class BudgetNode(Node):
    def __init__(self, amount):
        super().__init__(amount)
        self.transactions = []

    def add_transaction(self, transaction):
        self.transactions.append(transaction)

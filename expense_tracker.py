class ExpenseTracker:
    def __init__(self):
        # List to store all expenses
        self.expenses = []

    def add_expense(self, description, category, amount):
        # Add a new expense with description, category, and amount
        expense = {
            "Description": description,
            "Category": category,
            "Amount": amount
        }
        self.expenses.append(expense)

    def get_expense_summary(self):
        # Summary of expenses by category
        summary = {}
        for expense in self.expenses:
            category = expense.get("Category")
            if category:
                amount = float(expense.get("Amount", 0))
                summary[category] = summary.get(category, 0) + amount
        return summary

    def get_total_expense(self):
        # Calculate total expenses
        total = sum(float(expense.get("Amount", 0)) for expense in self.expenses)
        return total

    def show_expenses(self):
        # Display all recorded expenses
        for expense in self.expenses:
            print(f"Description: {expense['Description']}, Category: {expense['Category']}, Amount: {expense['Amount']}")


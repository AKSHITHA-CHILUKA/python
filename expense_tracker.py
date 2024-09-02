import json
from datetime import datetime

class ExpenseTracker:
    def __init__(self):
        self.expenses = self.load_expenses()

    def add_expense(self, amount, category, date):
        expense = {'amount': amount, 'category': category, 'date': date}
        self.expenses.append(expense)
        self.save_expenses()
        print("Expense added successfully!")

    def view_expenses(self):
        if not self.expenses:
            print("No expenses to display.")
            return
        print("Expenses:")
        for expense in self.expenses:
            print(f"{expense['date']} - {expense['category']} - ${expense['amount']:.2f}")

    def save_expenses(self):
        with open('expenses.json', 'w') as f:
            json.dump(self.expenses, f)

    def load_expenses(self):
        try:
            with open('expenses.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

def main():
    tracker = ExpenseTracker()
    while True:
        print("\n1. Add Expense")
        print("2. View Expenses")
        print("3. Exit")
        choice = input("Enter choice: ")
        
        if choice == '1':
            amount = float(input("Enter amount: "))
            category = input("Enter category: ")
            date = input("Enter date (YYYY-MM-DD): ")
            tracker.add_expense(amount, category, date)
        elif choice == '2':
            tracker.view_expenses()
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please select a valid option.")

if __name__ == "__main__":
    main()

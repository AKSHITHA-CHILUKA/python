import tkinter as tk
from tkinter import ttk, messagebox
import matplotlib.pyplot as plt
from expense_tracker import ExpenseTracker
class ExpenseTrackerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Personal Expense Tracker")
        self.tracker = ExpenseTracker()

        # Create the main frame
        main_frame = ttk.Frame(root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Category
        ttk.Label(main_frame, text="Category:").grid(row=0, column=0, sticky=tk.W)
        self.category_var = tk.StringVar()
        ttk.Entry(main_frame, textvariable=self.category_var).grid(row=0, column=1, sticky=tk.E)

        # Amount
        ttk.Label(main_frame, text="Amount:").grid(row=1, column=0, sticky=tk.W)
        self.amount_var = tk.StringVar()
        ttk.Entry(main_frame, textvariable=self.amount_var).grid(row=1, column=1, sticky=tk.E)

        # Description
        ttk.Label(main_frame, text="Description:").grid(row=2, column=0, sticky=tk.W)
        self.description_var = tk.StringVar()
        ttk.Entry(main_frame, textvariable=self.description_var).grid(row=2, column=1, sticky=tk.E)

        # Add Expense Button
        ttk.Button(main_frame, text="Add Expense", command=self.add_expense).grid(row=3, column=1, sticky=tk.E)

        # Summary Button
        ttk.Button(main_frame, text="Show Summary", command=self.show_summary).grid(row=4, column=1, sticky=tk.E)

    def add_expense(self):
        category = self.category_var.get()
        amount = self.amount_var.get()
        description = self.description_var.get()

        if not category or not amount:
            messagebox.showerror("Error", "Category and Amount are required")
            return

        try:
            amount = float(amount)
        except ValueError:
            messagebox.showerror("Error", "Amount must be a number")
            return

        self.tracker.add_expense(category, amount, description)
        messagebox.showinfo("Success", "Expense added successfully")

        # Clear the input fields
        self.category_var.set("")
        self.amount_var.set("")
        self.description_var.set("")

    def show_summary(self):
        summary = self.tracker.get_expense_summary()

        if not summary:
            messagebox.showinfo("Summary", "No expenses recorded")
            return

        # Display summary in a new window
        summary_window = tk.Toplevel(self.root)
        summary_window.title("Expense Summary")

        figure = plt.Figure(figsize=(6, 5), dpi=100)
        ax = figure.add_subplot(111)

        categories = list(summary.keys())
        amounts = list(summary.values())

        ax.bar(categories, amounts, color="blue")
        ax.set_title("Expense Summary")
        ax.set_ylabel("Amount")
        ax.set_xlabel("Category")

        canvas = plt.FigureCanvasTkAgg(figure, summary_window)
        canvas.get_tk_widget().pack()

        plt.show()

if __name__ == "__main__":
    root = tk.Tk()
    gui = ExpenseTrackerGUI(root)
    root.mainloop()

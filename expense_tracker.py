# Program to track expenses using CSV
# Features:
# Store/modify budget through user input, store/modify 
# imports

income = 0
expenses = {}

def load_expenses():
    print("Loading monthly expenses...")
    print("Loaded!")

def save_expenses():
    print("Saving monthly expenses...")
    print("Saved!")

def add_expense():
    expense = input("Enter the name of the monthly expense:\n> ").title()
    value = input("Enter the value of the monthly expense:\n> ")
    expenses[expense] = value.lstrip("$")

def load_income():
    print("Loading monthly income...")
    print("Loaded!")

def save_income():
    print("Saving monthly income...")
    print("Saved!")

def calc_total():
    total = 0
    for expense in expenses.values():
        total += float(expense)
    leftover_income = income - total
    print(f"Income is: ${income}")
    print(f"Expenses list:")
    for expense, value in expenses.items():
        print(f"{expense}: ${value}")

def display_expenses():
    pass

def main():
    print("-" * 15 + " Monthly Expense Tracker " + "-" * 15)
    load_expenses()

if __name__ == "__main__":
    main()
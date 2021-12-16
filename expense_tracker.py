# Program to track expenses using CSV
# Features:
# Store/modify budget through user input, store/modify 
import csv

expenses = {} 
income = {}

def load_expenses():
    expense_list = {}
    print("Loading monthly expenses...")
    with open("expenses.csv", "r") as file:
        reader = csv.reader(file)
        try:
            for expense, value in reader: # reads row by row
                expense_list[expense] = value
            print("Loaded!")
        except ValueError:
            print("There are no expenses to load.")
    file.close()
    return expense_list

def save_expenses():
    print("Saving monthly expenses...")
    with open("expenses.csv", "w", newline='') as file:
        writer = csv.writer(file)
        for expense, value in expenses.items():
            writer.writerow([expense, value])
    file.close()
    print("Saved!")

def add_expense():
    source = input("Enter the name of the monthly expense:\n> ").title()
    value = input("Enter the value of the monthly expense:\n> ")
    expenses[source] = value.lstrip("$")
    
def remove_expense():
    expense = input("Enter the name of the monthly expense:\n> ").title()
    del expenses[expense]

def load_income():
    income_sources = {}
    print("Loading monthly income...")
    with open('income.csv', 'r') as file:
        reader = csv.reader(file)
        try:
            for source, value in reader: # reads row by row
                income_sources[source] = value
            print("Loaded!")
        except ValueError:
            print("There are no expenses to load.")
    file.close()
    return income_sources

def save_income():
    print("Saving monthly income...")
    with open("income.csv", "w", newline='') as file:
        writer = csv.writer(file)
        for source, value in income.items():
            writer.writerow([source, value])
    print("Saved!")
    
def add_income():
    source = input("Enter the name of the monthly expense:\n> ").title()
    value = input("Enter the value of the monthly expense:\n> ")
    income[source] = value.lstrip("$")
    
def remove_income():
    source = input("Enter the name of the monthly expense:\n> ").title()
    del income[source]

def calc_total():
    total_expenses = 0
    total_income = 0
    for expense in expenses.values():
        total_expenses += float(expense)
    for source in income.values():
        total_income += float(source)
    leftover_income = total_income - total_expenses
    leftover_income = round(leftover_income, 2)
    display_income()
    display_expenses()
    print(f"\nYour leftover income is: ${leftover_income}")
    if leftover_income < 0:
          print("Look for ways to cut out expenses to save more money each month!")

def display_expenses():
    print(f"Your monthly expenses list:")
    for expense, value in expenses.items():
        print(f"{expense}: ${value}")

def display_income():
    print(f"Your monthly income list:")
    for source, value in income.items():
        print(f"{source}: ${value}")


if __name__ == "__main__":
    print("-" * 15 + " Monthly Expense Tracker " + "-" * 15)
    expenses = load_expenses()
    income = load_income()
    while True:
        action = input("""
What would you like to do?

1. Add/update a monthly income source
2. Remove a monthly income source
3. Add/update a monthly expense
4. Remove a monthly expense
5. View your monthly income
6. View your monthly expenses
7. Calculate your leftover monthly income
8. Exit

>  """)
        if action == "1":
            add_income()
        if action == "2":
            remove_income()
        if action == "3":
            add_expense()
        if action == "4":
            remove_expense()
        if action == "5":
            display_income()
        if action == "6":
            display_expenses()
        if action == "7":
            calc_total()
        if action == "8":
            save_expenses()
            save_income()
            print("Goodbye!")
            exit()
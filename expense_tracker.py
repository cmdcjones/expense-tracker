# Program to track expenses using CSV
# Features:
# Store/modify budget through user input, store/modify 
# imports

income = {}
expenses = {}

def load_expenses():
    print("Loading monthly expenses...")
    print("Loaded!")

def save_expenses():
    print("Saving monthly expenses...")
    print("Saved!")

def add_expense():
    source = input("Enter the name of the monthly expense:\n> ").title()
    value = input("Enter the value of the monthly expense:\n> ")
    expenses[source] = value.lstrip("$")
    
def remove_expense():
    pass

def load_income():
    print("Loading monthly income...")
    print("Loaded!")

def save_income():
    print("Saving monthly income...")
    print("Saved!")
    
def add_income():
    source = input("Enter the name of the monthly expense:\n> ").title()
    value = input("Enter the value of the monthly expense:\n> ")
    income[source] = value.lstrip("$")
    
def remove_income():
    pass

def calc_total():
    total = 0
    for expense in expenses.values():
        total += float(expense)
    leftover_income = income - total
    print(f"Your monthly income is: ${income}")
    print(f"Your monthly expenses list:")
    display_expenses()
    print(f"\nYour leftover income is: ${leftover_income})
    if leftover_income < 0:
          print("Look for ways to cut out expenses to save more money each month!")

def display_expenses():
    for expense, value in expenses.items():
        print(f"{expense}: ${value}")

def main():
    print("-" * 15 + " Monthly Expense Tracker " + "-" * 15)
    load_income()
    load_expenses()
    while True:
          action = input("""What would you like to do?

1. Add a monthly income source
2. Remove a monthly income source
3. Add a monthly expense
4. Remove a monthly expense
5. View your monthly income
6. View your monthly expenses
7. Exit

>  """
    if action == "1":
       add_income()

if __name__ == "__main__":
    main()

# 🧾 Mini Project – Expense Tracker

# Question / Problem Statement: Create a console-based Expense Tracker
# program in Python that allows the user to record daily expenses and view
# summaries like total spending. Use only the concepts learned till Chapter 6
# (loops, conditionals, lists, dictionaries, and basic input/output).

# Project Details / Description:
# You are required to build a simple personal finance management tool.
# The program should allow the user to:
# ● Add an expense with details like date, category, description, and amount.
# ● View all recorded expenses in a clean format.
# ● Calculate total spending so far.
# ● Exit the program gracefully when the user chooses to.

# All tasks must be implemented using loops, if-else, lists, and dictionaries
# only. No user-defined functions or file handling should be used.

# Sample Output:
# Welcome to Expense Tracker 💸
expense_details = []
print("Welcome to Expense Tracker 💸")

# ======= MENU =======
while True:
    print("\n======= MENU =======")
    print("1️⃣Add Expense")
    print("2️⃣View All Expenses")
    print("3️⃣View Total Spending")
    print("4️⃣View Spending by Category")
    print("5️⃣Exit")
    print("=====================")
    
    choice = input("Enter your choice (1-5): ")
    
  # 1️⃣Add Expense  
    if choice == '1':
        date = input("Enter date (DD-MM-YYYY): ")
        category = input("Enter category (Food, Travel, Shopping, etc): ")
        description = input("Enter short description: ")
        amount = float(input("Enter amount (₹): "))
        
        expenses = {
            "date": date,
            "category": category,
            "description": description,
            "amount": amount
        }
        
        expense_details.append(expenses)
        print(f"✅ Expense added successfully!")

# 2️⃣View All Expenses
    elif choice == '2':
        if not expense_details:
            print("No expenses recorded yet.")
        else:
            print("✅ All Expenses:")
            for i in expense_details:
                print(f"  Date: {i['date']}, Category: {i['category']}, Description: {i['description']}, Amount: ₹{i['amount']}")
# 3️⃣View Total Spending

    elif choice == '3':
        total_spending = sum(i['amount'] for i in expense_details)
        print(f"💰 Total Spending = ₹{total_spending}")
        
# 4️⃣Exit
    elif choice == '4':
        category_spending = {}
        for i in expense_details:
            if i['category'] in category_spending:
                category_spending[i['category']] += i['amount']
            else:
                category_spending[i['category']] = i['amount']
        
        if not category_spending:
            print("No expenses recorded yet.")
        else:
            print("✅ Spending by Category:")
            for category, amount in category_spending.items():
                print(f"  Category: {category}, Total Spending: ₹{amount}")
    
    elif choice == '5':
        print("Exiting the program. Goodbye! 👋")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
# =====================
# Enter your choice (1-4): 1
# Enter date (DD-MM-YYYY): 05-11-2025
# Enter category (Food, Travel, Shopping, etc): Food

# Enter short description: Lunch
# Enter amount (₹): 150
# ✅ Expense added successfully!
# ======= MENU =======
# 1️⃣Add Expense
# 2️⃣View All Expenses
# 3️⃣View Total Spending
# 4️⃣Exit
# =====================
# Enter your choice (1-4): 3
# 💰 Total Spending = ₹150

# Concept Purpose
# while loop To repeat the menu until user exits
# if-elif-else To handle menu options
# list To store multiple expenses
# dictionary To store details of each expense
# for loop To display and calculate totals
# input() / print() For user interaction
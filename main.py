"""

📝 Problem Statement

Build a Personal Finance Manager in Python

The program should allow a user to:

1. Register/Login with username & password (store credentials in a file).

2. Add transactions → income or expense (date, category, amount, description).

3. View all transactions stored.

4. Search/Filter transactions by category or date.

5. Generate summary report → total income, total expense, balance.

6. Export data into a CSV/text file.

7. Exit the program safely.

All data should be stored in a file (CSV/JSON) so that it persists after program exits.

🔹 Sample Input / Output


**Case 1: Login/Register

Welcome to Personal Finance Manager
1. Register
2. Login
Choose option: 1
Enter username: bubuu
Enter password: 1234
User registered successfully!

Choose option: 2

Enter username: bubuu
Enter password: 1234
Login successful! Welcome, bubuu.


**Case 2: Add Income/Expense

1. Add Transaction
2. View Transactions
3. Summary
4. Export Data
5. Logout

Choose option: 1

Enter date (YYYY-MM-DD): 2025-09-12
Enter type (income/expense): expense
Enter category: food
Enter amount: 250
Enter description: Pizza with friends
Transaction added successfully!


**Case 3: View Transactions

Date        Type      Category    Amount   Description
------------------------------------------------------
2025-09-12  expense   food        250      Pizza with friends


**Case 4: Summary Report

Summary Report
--------------
Total Income  : 10000
Total Expense : 2500
Balance       : 7500


**Case 5: Export

Data exported to finance_data.csv

"""


from login_register import register_user, login_user
from transactions import init_file, add_transaction, view_transactions, Summary_Report, Export_Data

init_file()

print("\n\n=== Welcome to Personal Finance Manager ===")
print("1. Register\n2. Login")
choice = int(input("\nChoose option: "))

if choice == 1:
    user = register_user()
elif choice == 2:
    user = login_user()
else:
    print("\n❌ Invalid choice!")
    exit()

if user:
    while True:
        print("\nWhat do you want to do?")
        print("1. Add Transaction\n2. View Transactions\n3. Summary Report\n4. Export Data\n5. Logout")
        choice2 = int(input("Choose option: "))
        print("\n")
        if choice2 == 1:
            add_transaction(user)
        elif choice2 == 2:
            view_transactions(user)
        elif choice2 == 3:
            Summary_Report(user)
        elif choice2 == 4:
            Export_Data()
        elif choice2 == 5:
            print("Logging out...")
            break
        else:
            print("❌ Invalid choice! Choose between 1 to 5.")

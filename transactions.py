import csv
import shutil  # for file copy
from datetime import datetime

filename = "finance_data.csv"

def get_valid_amount():
    while True:
        amt_str = input("Enter amount: ")
        if amt_str.isdigit():  # only numbers allowed
            return int(amt_str)
        else:
            print("❌ Invalid amount! Please enter numbers only.")


def get_valid_date():
    while True:
        date_str = input("Enter date (YYYY-MM-DD): ")
        try:
            # check valid date
            datetime.strptime(date_str, "%Y-%m-%d")
            return date_str
        except ValueError:
            print("❌ Invalid date! Please use YYYY-MM-DD format.")

def get_valid_type():
    while True:
        tran_type = input("Enter type (income/expense): ").lower()
        if tran_type in ["income", "expense"]:
            return tran_type
        else:
            print("❌ Invalid type! Please enter only 'income' or 'expense'.")

def init_file():
    try:
        with open(filename, "x", newline="") as file:
            writer = csv.writer(file)
            # Add username column
            writer.writerow(["username","date","type","category","amount","description"])
    except FileExistsError:
        pass

def add_transaction(username):
    date = get_valid_date()
    tran_type = get_valid_type()
    category = input("Enter category: ")
    amount = get_valid_amount()
    desc = input("Enter description: ")

    with open(filename, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([username, date, tran_type, category, amount, desc])

    print("✅ Transaction added successfully!")

def view_transactions(username):
    try:
        with open(filename, "r") as file:
            reader = csv.reader(file)
            transactions = list(reader)
            if len(transactions) <= 1:
                print("No transactions found.")
                return

            print("\nDate        Type      Category    Amount   Description")
            print("------------------------------------------------------")
            for row in transactions[1:]:  # skip header
                if row[0] == username:  # show only logged-in user's data
                    print(f"{row[1]:10}  {row[2]:8}  {row[3]:10}  {row[4]:6}   {row[5]}")
            print("\n")
    except FileNotFoundError:
        print("No transaction file found!")


def Summary_Report(username):

    total_income = 0
    total_expense = 0
    try:
        with open(filename, "r") as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                if row[0] != username:
                    continue  # skip other users
                ttype = row[2].lower()
                amount = float(row[4])
                if ttype == "income":
                    total_income += amount
                elif ttype == "expense":
                    total_expense += amount

        balance = total_income - total_expense
        print("\nSummary Report")
        print("--------------")
        print(f"Total Income  : {total_income}")
        print(f"Total Expense : {total_expense}")
        print(f"Balance       : {balance}")
    except FileNotFoundError:
        print("No transaction file found! Please add a transaction first.")

def Export_Data():
    try:
        backup_file = "finance_data_backup.csv"
        shutil.copy(filename, backup_file)
        print(f"✅ Data exported to {backup_file}")
    except FileNotFoundError:
        print("No transaction file found! Please add a transaction first.")
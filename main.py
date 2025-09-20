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


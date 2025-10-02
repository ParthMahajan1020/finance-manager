# Import user authentication functions
from login_register import register_user, login_user
# Import transaction management functions
from transactions import init_file, add_transaction, view_transactions, Summary_Report, Export_Data

# Initialize the CSV file if it doesn't exist yet
init_file()

# Welcome message and main menu
print("\n\n=== Welcome to Personal Finance Manager ===")
print("1. Register\n2. Login")

# Ask user to choose between registering or logging in
choice = int(input("\nChoose option: "))

# Handle registration or login
if choice == 1:
    user = register_user()  # Register a new user and return username
elif choice == 2:
    user = login_user()     # Login existing user and return username
else:
    print("\n❌ Invalid choice!")
    exit()  # Exit program if invalid choice

# If login or registration was successful, enter main transaction menu
if user:
    while True:
        print("\nWhat do you want to do?")
        print("1. Add Transaction\n2. View Transactions\n3. Summary Report\n4. Export Data\n5. Logout")
        
        # Ask user for next action
        choice2 = int(input("Choose option: "))
        print("\n")
        
        # Execute function based on user choice
        if choice2 == 1:
            add_transaction(user)      # Add a new transaction for this user
        elif choice2 == 2:
            view_transactions(user)    # View all transactions for this user
        elif choice2 == 3:
            Summary_Report(user)       # Show summary report (income, expense, balance)
        elif choice2 == 4:
            Export_Data()              # Export/backup the transaction CSV file
        elif choice2 == 5:
            print("Logging out...")
            break                      # Exit the while loop (logout)
        else:
            # Handle invalid option
            print("❌ Invalid choice! Choose between 1 to 5.")

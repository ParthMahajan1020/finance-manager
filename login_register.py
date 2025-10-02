import msvcrt  # Windows-only module to capture single keypresses without requiring Enter

# Function to securely get a 4-digit password from the user
def get_password():
    print("Enter your 4-digit password: ", end="", flush=True)
    password = ""
    while len(password) < 4:
        # Read a single keypress from the user without waiting for Enter
        ch = msvcrt.getch().decode("utf-8")  
        # Explanation:
        # - msvcrt.getch() captures a key immediately, returning a bytes object
        # - decode("utf-8") converts bytes to a string
        # This allows showing '*' for each key pressed instead of the actual digit
        if ch.isdigit():  # Only accept numeric input
            password += ch  # Add digit to password
            print("*", end="", flush=True)  # Print '*' to hide the digit
    print()  # Move to next line after password entry
    return password

# Function to register a new user
def register_user():
    username = input("Enter Username: ")
    password = get_password()  # Get a 4-digit password from the user
    # Save username & password to a CSV file (users.csv)
    with open("users.csv", "a") as f:
        f.write(f"{username},{password}\n")
    print("✅ User registered successfully!")
    return username

# Function to login an existing user
def login_user():
    username = input("Enter Username: ")
    password = get_password()  # Get password for verification
    # Check credentials against users.csv
    try:
        with open("users.csv", "r") as f:
            for line in f:
                u, p = line.strip().split(",")  # Split CSV line into username & password
                if username == u and password == p:  # Verify credentials
                    print(f"✅ Login successful! Welcome, {username}")
                    return username
        print("❌ Invalid username/password!")  # If no match found
        return None
    except FileNotFoundError:  # If users.csv doesn't exist yet
        print("No users found. Please register first.")
        return None

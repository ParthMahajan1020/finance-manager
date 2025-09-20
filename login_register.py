import msvcrt

def get_password():
    print("Enter your 4-digit password: ", end="", flush=True)
    password = ""
    while len(password) < 4:
        ch = msvcrt.getch().decode("utf-8")
        if ch.isdigit():
            password += ch
            print("*", end="", flush=True)
    print()
    return password

def register_user():
    username = input("Enter Username: ")
    password = get_password()
    # save username & password in file (users.csv)
    with open("users.csv", "a") as f:
        f.write(f"{username},{password}\n")
    print("✅ User registered successfully!")
    return username

def login_user():
    username = input("Enter Username: ")
    password = get_password()
    # check users.csv
    try:
        with open("users.csv", "r") as f:
            for line in f:
                u, p = line.strip().split(",")
                if username == u and password == p:
                    print(f"✅ Login successful! Welcome, {username}")
                    return username
        print("❌ Invalid username/password!")
        return None
    except FileNotFoundError:
        print("No users found. Please register first.")
        return None

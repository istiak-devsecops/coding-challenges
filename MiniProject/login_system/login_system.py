# Store a username + password inside your script. Ask the user to enter credentials.

# Read userdata from the file
try:
    with open("user_data.txt", "r") as file:
        credentials = []
        for line in file:
            line = line.strip()
            if ":" in line:
                try:
                    stored_user, stored_pass = line.split(":", 1)
                    credentials.append((stored_user, stored_pass))
                except ValueError:
                    print(f"Skipping malformed line...")
except FileNotFoundError:
    print(f"ERROR:File not found ...")
    exit()
if not credentials:
    print("No valid credintials found in the file.")
    exit()

max_attempts = 3
attempt = 0
authenticated = False

# login attemp loop
while attempt < max_attempts:
    input_user = input("What is the username: ")
    input_pass = input("What is the passcode: ")

    for user, password in credentials:
        if input_user == user and password == password:
            print("Login successfull!")
            authenticated = True
            break
    if authenticated:
        break
    else:
        attempt += 1
        left = max_attempts - attempt
        print(f"You have {left} attemp left.")

if not authenticated:
    print("Too many failed login attempt. Try again later.")

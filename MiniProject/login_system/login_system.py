# Store a username + password inside your script. Ask the user to enter credentials.

# Read userdata from the file
try:
    with open("user_data.txt","r") as file:
        crediantials = []
        for line in file:
            line = line.strip()
            if ":" in line:
                try:
                    username, passcode = line.split(":",1)
                    crediantials.append((username,passcode))
                except ValueError:
                    print(f"Skipping malformed line...")
except FileNotFoundError:
    print(f"ERROR:File not found ...")
    exit()
if not crediantials:
    print("No valid credintials found in the file.")
    exit()

max_attempts = 3
attempt = 0
authenticated = False

#login attemp loop
while attempt < max_attempts:
    user = input("What is the username: ")
    password = input("What is the passcode: ")

    for user, password in crediantials:
        if user == username and password == passcode:
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
# Store a username + password inside your script. Ask the user to enter credentials.

# Read userdata from the file
with open("user_data.txt","r") as file:
    for line in file:
        line = line.strip()
        if ":" in line:
            username, passcode = line.split(":",1)

max_attemps = 3
attemp = 0

while attemp < max_attemps:
    user = input("What is the username: ")
    password = input("What is the passcode: ")


    if user == username and password == passcode:
        print("Login successfull!")
        break
    else:
        attemp += 1
        left = max_attemps - attemp
        print(f"You have {left} attemp left.")

if max_attemps == attemp:
    print("Too many failed login attempt. Try again later.")
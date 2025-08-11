#check for week password from a log file

with open("log.txt", "r") as file:
    content = file.readlines()   #read file line by line

clean_content = []

for word in content:
    clean_content.append(word.strip().split(":")) # add content to the list

weak_user = []

for username, password in clean_content:
    if len(password) < 8:                       #check if the password is below 8 char
        weak_user.append(username)
        continue

    has_upper = any(ch.isupper() for ch in password) 
    has_lower = any(ch.islower() for ch in password)
    has_digit = any(ch.isdigit() for ch in password)
    
    if not (has_upper and has_lower and has_digit): #check password contain lowercase, digit, uppercase
        weak_user.append(username)

print("weak passwords found for: ")
for user in weak_user:
    print(user)


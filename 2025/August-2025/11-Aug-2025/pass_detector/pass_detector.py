#check for week password from a log file

with open("log.txt", "r") as file:
    content = file.readlines()

cleancontent = []

for word in content:
    cleancontent.append(word.strip().split(":"))

strong_user = []

for username, password in cleancontent:
    if len(password) > 8: 
        strong_user.append(username)
        continue

    has_upper = any(chr.isupper() for chr in password)
    has_lower = any(chr.islower() for chr in password)
    has_digit = any(chr.isdigit() for chr in password)

    if not (has_digit and has_lower and has_upper):
        strong_user.append(username)

print("strong password found for: ")
for user in strong_user:
    print(user)


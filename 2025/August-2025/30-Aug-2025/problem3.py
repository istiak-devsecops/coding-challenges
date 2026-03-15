import re

user_input =input("What is your password: ")

# at least 8 chars and one uppercase, one lowercase, one special 
pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[^A-Za-z0-9]).{8,}$'
result = re.findall(pattern,user_input)

if re.match(pattern, user_input):
    print("Strong password")
else:
    print("Weak password")
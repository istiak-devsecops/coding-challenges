# Write a regex that checks if a given string is a valid email format.

import re

user_input = input("what is your email address: ")

pattern = r'^[a-zA-Z0-9._-+]+@[a-zA-Z0-9._]+\.[a-zA-Z]{2,}$'

if re.match(pattern, user_input):
    print("This is a valid email address.")
else:
    print("This is not a valid email. Try again!")
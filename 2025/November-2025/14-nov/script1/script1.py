import re

pattern = r"([a-zA-Z0-9._%+]+@[a-zA-Z0-9._]+\.[a-z]{2,})"

with open("script1.txt", 'r') as file:
    for line in file:
        emails = re.findall(pattern, line)
        for email in emails:
            print(email)
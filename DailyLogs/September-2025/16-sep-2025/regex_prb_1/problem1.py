import re

try:
    with open("data1.txt", "r") as file:
        content = file.read()
    print(content)
except Exception as e:
    print("Caught error:", e)
    content = ""


email_pattern = r"[a-zA-Z0-9+-._]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-]+"
emails = re.findall(email_pattern, content)

print("List of emails are:\n")
for email in emails:
    print("-",email)
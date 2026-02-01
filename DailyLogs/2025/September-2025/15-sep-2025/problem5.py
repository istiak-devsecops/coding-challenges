import re

text = " This is the email: name123@example.co.uk , here are few more email istiak@gmail.com , shoaib@yahoo.com"

pattern = r'\w+\@\w+\.\w+'

email_list = re.findall(pattern, text)

print(email_list)
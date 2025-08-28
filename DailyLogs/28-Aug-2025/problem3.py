import re

text = "Contact us at help@example.com or support@company.org"

result = re.findall(r'[\w.]+@\w+\.\w+',text)
print(result)
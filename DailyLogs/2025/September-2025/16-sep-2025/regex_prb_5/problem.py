import re

try:
    with open("data.txt", "r")as file:
        content = file.read()
except Exception as e:
    print("caught error: ", e)
    content = ""


pattern = r"\s{2,}"
clean_content = re.sub(pattern, " ", content)
print(clean_content)
import re

try:
    with open("data.txt","r")as file:
        content = file.read()
except Exception as e:
    print(f"caught error: {e}")
    content = ""

hashtag_pattern = r"#\w+"
hashtag = re.findall(hashtag_pattern, content)

print("Here are the list of hashtag: ")
for tag in hashtag:
    print("-",tag)
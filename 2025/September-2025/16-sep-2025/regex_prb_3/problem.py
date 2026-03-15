import re
with open("data.txt","r")as file:
    content = file.read()

date_pattern = r"\d{4}\-\d{2}\-\d{2}"
time_pattern = r"\d{2}\:\d{2}\:\d{2}"

date_list = re.findall(date_pattern, content)
time_list = re.findall(time_pattern, content)

for date in date_list:
    print("List of dates:",date)

for time in time_list:
    print("List of times:",time)
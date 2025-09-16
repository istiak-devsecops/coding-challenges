import re
with open("IP.txt","r") as file:
    ips = file.read()

pattern = r"\b(?:(?:25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)\.){3}(?:25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)\b"

ip_list = re.findall(pattern, ips) 

for ip in ip_list:
    print(ip)
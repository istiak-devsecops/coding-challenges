import re

ip_file = "script1.txt"
pattern = r"^([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3})$"


with open(ip_file, "r")as file:
    for line in file:
        ip_addr = re.findall(pattern, line)
        for ip in ip_addr:
            print(ip)
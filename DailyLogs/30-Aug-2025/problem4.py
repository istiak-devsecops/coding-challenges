#Extract all unique IP addresses from the logs.

logs = [
    "192.168.1.10 - ERROR",
    "192.168.1.11 - OK",
    "192.168.1.10 - FAILED",
    "192.168.1.12 - OK",
    "192.168.1.11 - ERROR"]

uniq_ip = set()

#separate ip address from the line
for log in logs:
    ip = log.split()[0]
    uniq_ip.add(ip)

print(uniq_ip)
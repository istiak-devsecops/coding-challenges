# From log = "[2025-08-29 11:20:45] ERROR: Connection refused from 192.168.1.10", 

# extract:
# The timestamp
# The log level (ERROR)
# The IP address

log = "[2025-08-29 11:20:45] ERROR: Connection refused from 192.168.1.10"

import re

#timestamp search pattern
timestamp_pattern = r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}"
times = re.findall(timestamp_pattern,log)

#error search pattern
error_pattern = r"\b[A-Z]+\b"
errors = re.findall(error_pattern,log)

#ip address search pattern
ip_pattern = r"\d+\.\d+\.\d+\.\d+"
ip_addresses = re.findall(ip_pattern,log)

print(times)
print(errors)
print(ip_addresses)
servers = {
    "server1": {"ip": "192.168.1.1", "status": "active"},
    "server2": {"ip": "192.168.1.2", "status": "inactive"}
}

#loop through every key to get the value in a list format
for key, value in servers.items():
    ip = value["ip"]
    status = value["status"]
    print(f"{key}: IP:{ip}({status})")
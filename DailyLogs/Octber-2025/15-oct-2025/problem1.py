import subprocess

disk_usages = subprocess.run(["df", "-h"], capture_output=True, text=True) # shows disk usages
print(disk_usages.stdout)
 
system_status = subprocess.run(["systemctl", "status", "nginx"], capture_output=True, text=True) # shows nginx system status
print(system_status.stdout)



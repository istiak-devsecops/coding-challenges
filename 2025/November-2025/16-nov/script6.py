# Create a Folder Named After Script Argument and Save a Log File Inside

import os
import sys

if len(sys.argv) < 2:
    print(f"Usage: python3 script.py <file/dir name>.")
    sys.exit(1)

dir = sys.argv[1]   # dir name
os.makedirs(dir, exist_ok=True)     # created the dir

log_dir = os.path.join(dir, "log.txt")  # creating the log file inside the dir
with open(log_dir, "w") as file:    # write few lines inside the log file
    file.write("This is a log file\n")
    file.write("This file is created by a python script.\n")

print(f"Log file created at: {log_dir}")

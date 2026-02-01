import sys
import time
import subprocess
from datetime import datetime

if len(sys.argv) < 2:
    print("Usage: python3 script.py <command name>")
    sys.exit(2) # invalid arguments

command = " ".join(sys.argv[1:]) # join the commands to make a single command
result = subprocess.run(command, capture_output=True, shell=True, text=True)
start_time = datetime.now()
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
time.sleep(2)
end_time = datetime.now()
time_difference = start_time - end_time

with open("script_metadata_log.txt", "w")as file:
    file.write(f"Script Metadata log\n")
    file.write(f"Timestamp: {timestamp}\n")
    file.write("======Details=====\n")
    file.write(f"Start time: {start_time}\n")
    file.write(f"End time: {end_time}\n")
    file.write(f"{result.stdout if result.stdout else 'Exit Code = 1(failure)'}\n")
    file.write(f"{result.stderr if result.stderr else 'Exit Code = 0(Success)'}\n")


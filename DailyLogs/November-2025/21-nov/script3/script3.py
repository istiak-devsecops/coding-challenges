import subprocess
import datetime
import sys

if len(sys.argv) < 2:
    print("Usage: python3 script.py <command>")
    sys.exit(2) # invalid arguments

shell_command = sys.argv[1]
shell_command_results = subprocess.run(shell_command, capture_output=True,shell=True, text=True)
timestamp = datetime.datetime.now().strftime("%Y-%m-%d")

with open(f"log_{timestamp}.txt", "w")as file:
    file.write("output log data: \n")
    file.write(f"Output: {shell_command_results.stdout}\n")
    file.write(f"Error: {shell_command_results.stderr}")
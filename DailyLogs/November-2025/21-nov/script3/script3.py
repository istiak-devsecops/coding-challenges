import subprocess
import datetime
import sys

if len(sys.argv) < 2:
    print("Usage: python3 script.py <command>")
    sys.exit(2) # invalid arguments

shell_command = " ".join(sys.argv[1])
shell_command_results = subprocess.run(shell_command, capture_output=True,shell=True, text=True)
timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
log_file = f"log_{timestamp}.txt"

with open(log_file, "w")as file:
    file.write(f"Shell commands: {shell_command}\n")
    file.write(f"Timestamp: {timestamp}\n")
    file.write("output log data: \n")
    file.write("=====Standard Output=====\n")
    file.write(shell_command_results.stdout if shell_command_results.stdout else "(no output)\n")
    file.write("=====Standard Error=====\n")
    file.write(shell_command_results.stderr if shell_command_results.stderr else "(no error)")

print("Logged saved to: ",{log_file})
from datetime import date
import subprocess
import sys


if len(sys.argv) < 2:
    print("Usage: python3 script.py <command>")
    sys.exit(2)  # invalid arguments


command = sys.argv[1:]  # capture all the input except script name
time_stamp = date.today().strftime("%Y-%m-%d")

result = subprocess.run(command, capture_output=True, text=True)

file_name = f"backup_{time_stamp}"  # create the file

with open(file_name, 'w')as file:
    file.write(result.stdout)  # write command output to a file
    print(f'The output has been captured in the file {file_name}')

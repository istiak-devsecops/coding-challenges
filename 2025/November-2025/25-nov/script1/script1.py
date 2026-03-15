import sys
import subprocess
import datetime
import json


if len(sys.argv) < 2:
    print("Usage: python3 script.py <arguments>")
    sys.exit(2) # exit code invalid arguments

command = " ".join(sys.argv[1:]) # make the commands as a single string
result = subprocess.run(command, capture_output=True, shell=True, text=True)
timestamp = datetime.datetime.now().isoformat()
data = {"command" : command , "stdout": result.stdout, "stderr": result.stderr, "timestamp": timestamp}

with open("data.json", "w")as file:
    json.dump(data, file)
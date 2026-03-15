import subprocess
import sys

if len(sys.argv) < 2:
    print("Usage: python3 script.py <commands>")
    sys.exit(2) # invalid arguments


command = sys.argv[1:] # capture all the arguments

result = subprocess.run(command, capture_output=True, text=True)

print("Here is the result: \n",result.stdout)
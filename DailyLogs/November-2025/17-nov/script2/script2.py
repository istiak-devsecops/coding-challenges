import os
import sys

if len(sys.argv) < 2:
    print(f"Usage: python3 script.py <filename>")
    sys.exit(2) # invalid arguments

file = sys.argv[1]

if os.path.isfile(file):
    print(f"File exist.")
    sys.exit(0) # success
else:
    print(f"File doesn't exist.")
    sys.exit(1) # file missing
    
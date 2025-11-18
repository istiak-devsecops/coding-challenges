import sys
import os
import re

if len(sys.argv) < 2:
    print("Usage: python3 script.py <commands>")
    sys.exit(2) # invalid arguments

file_pattern = sys.argv[1]
regex = re.compile(file_pattern)
files = os.listdir()

for file in files:
    if os.path.isfile(file) and regex.match(file):
        print(f"Files been found: {file}.")
    else:
        print("No matching file found!")
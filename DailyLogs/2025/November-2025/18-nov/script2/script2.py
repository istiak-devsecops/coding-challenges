import sys
import os
import re

if len(sys.argv) < 2:
    print("Usage: python3 script.py <commands>")
    sys.exit(2) # invalid arguments

file_pattern = sys.argv[1]

try:
    regex = re.compile(file_pattern)
except re.error:
    print("Invalid regex pattern!")
    sys.exit(1) # missing arguments

files = os.listdir()
mathed_file = []

for file in files:
    if os.path.isfile(file) and regex.search(file):
        mathed_file.append(file)
        
if mathed_file:
    print("Matching files: ")
    for f in mathed_file:
        print(f)
else:
    print("No matchng file found!")
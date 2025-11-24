import re
from pathlib import Path
import sys


# check if there is an arguments
if len(sys.argv) < 3:
    print(f"Usage: python3 script.py <arguments> <pattern>")
    sys.exit(2) # missing arguments

dir_path = Path(sys.argv[1]).resolve() # absoulate path
pattern = sys.argv[2] # regex pattern

regex = re.compile(pattern) # compile the pattern

if not dir_path.exists() or not dir_path.is_file():
    print("Invalid directory.")
    sys.exit(1) # exit code missing directory


# seach the file
for file in dir_path.rglob("*"):
    if file.is_file() and regex.search(file.name):
        print(file)


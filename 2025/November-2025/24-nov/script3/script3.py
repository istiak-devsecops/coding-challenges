from pathlib import Path
import sys

if len(sys.argv) < 2:
    print("usage: python3 script.py <arguments>")
    sys.exit(2) # exit code invalid arguments

dir_path = Path(sys.argv[1])

# check if the path is valid
if not dir_path.exists():
    print(f"{dir_path} is not valid")
    sys.exit(1) # missing path

# check if it is a directory
if not dir_path.is_dir():
    print(f"{dir_path} is not a directory")
    sys.exit(1) # missing directory

print("Here are the file list:\n")
for file in dir_path.rglob("*"):
    print(file)


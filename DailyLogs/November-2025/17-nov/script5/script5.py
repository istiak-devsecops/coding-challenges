import sys

if len(sys.argv) < 2:
    print(f"Usage: python3 script.py <filename>")
    sys.exit(1) # missing file

filename = sys.argv[1]

try:
    with open(filename, "r")as file:
        lines = file.readlines()
        print(f"Number of lines is: {len(lines)}")
        sys.exit(0) # success
except FileNotFoundError as e:
    print(f"{e} is missing.")
    sys.exit(1) # file missing

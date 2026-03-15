# Count Lines in a File Passed via CLI

import module

check if there is 1 argments at least

define filename from CLI

try:
    with open(filename, "r")as file:
        lines = file.readlines()
        print(number of line is len(lines))
except FileNotFoundError as e:
    print("{e} not found")

# Print All Python Files in Current Directory

import module

for file in os.listdir():
    if file.endswith(".py"):
        print(f"-{file}")
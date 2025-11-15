import os
import sys

# Path to search
path_to_search = sys.argv[1]  # or hardcode like path_to_search = "/home/user"

# Initialize counter
count = 0

# Loop through all entries in the path
for dir in os.listdir(path_to_search):
    full_path = os.path.join(path_to_search, dir)
    if os.path.isdir(full_path):
        print(full_path)
        count += 1

print(f"Total directories: {count}")
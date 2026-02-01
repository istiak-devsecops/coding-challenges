import os
import sys
import shutil

if len(sys.argv) != 2:
    print("Usage: python3 script.py <dir name>")
    sys.exit(2) # invalid arguments

dir_name = sys.argv[1]

total_size = 0

for root, dirs, files in os.walk(dir_name):
    for file in files:
        filePath = os.path.join(root, file)

        # skip broken symlinks, just in case
        if not os.path.exists(filePath):
            continue

        total_size += os.path.getsize(filePath)

def format_size(bytes_value):
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if bytes_value < 1024:
            return f"{bytes_value:.2f} {unit}"
        bytes_value /= 1024
import sys
import os
import shutil
from datetime import datetime, timedelta

if len(sys.argv) < 2:
    print("Usage: python3 script.py <Directory name> <days>")
    sys.exit(2) # Invalid arguments

dir_path = sys.argv[1]  # directory name from cli
days = sys.argv[2]  # number of days from cli

time_difference = datetime.now() - timedelta(days=days) # file aged that needs to be removed

deleted_files = 0
deleted_dir = 0

for root, dirs, files in os.walk(dir_path, topdown=False):
    for file in files:  # delete files
        file_path = os.path.join(root, file)
        if os.path.getmtime(file_path) < time_difference:
            os.remove(file_path)
            deleted_files += 1

    for dir in dirs:    # delete directories
        dir_paths = os.path.join(root, dir)
        try:
            if not os.listdir(dir_paths):  # empty dir
                shutil.rmtree(dir_paths)
                deleted_dir += 1
        except FileNotFoundError:
            pass

print(f"Old file cleanup down.\n")
print(f"File deleted: {deleted_files}\n")
print(f"Directory deleted: {deleted_dir}")
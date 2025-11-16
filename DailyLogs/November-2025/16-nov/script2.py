# remove a directory from command line argument
import os
import sys

if len(sys.argv) < 2:
    print("Usage: python script.py <file/directory name>.")
else:
    dir = sys.argv[1]
    if os.path.exists(dir):
        os.rmdir(dir)
        print(f"The directory {dir} has been removed.")
    else:
        print("The directory does not exist.")
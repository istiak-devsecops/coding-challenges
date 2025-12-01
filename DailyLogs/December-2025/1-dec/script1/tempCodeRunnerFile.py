'''
Create a .tar file from a single file

Write a script that:

takes a filename as CLI input

creates output.tar

adds that file inside the tar

'''

import tarfile
import sys
from pathlib import Path

if len(sys.argv) < 2:
    print("Usage: python3 script.py <filename>")
    sys.exit(2) # invalid arguments

file_path = Path(sys.argv[1]).resolve() # full file path

# create a tar file
with tarfile.open("output.tar","w")as tar:
    tar.add(file_path)
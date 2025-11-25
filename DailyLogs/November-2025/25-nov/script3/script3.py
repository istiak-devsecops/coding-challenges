import os
import json 
import datetime
import sys
from pathlib import Path

if len(sys.argv) < 2:
    print("Usage: python3 script.py <filename>")
    sys.exit(2) # exit code invalid arguments

file_name = sys.argv[1]
file_path = Path(file_name)

with open(file_name, 'r')as file:
    file.readlines()
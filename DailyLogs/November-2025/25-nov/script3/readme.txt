Log File to JSON

- Accept a filename via CLI
- Read the file line by line
- Store each line in a JSON array with {"line_number": ..., "content": ...}
- Save to output.json


import os
import json 
import datetime
import sys

if len(sys.argv) < 2:
    print("Usage: python3 script.py <filename>")
    sys.exit(2) # exit code invalid arguments

file_name = sys.argv[1]

with open(file_name, 'r')as file:
    file.readlines()
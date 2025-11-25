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

if not file_path.exists():
    print("File doesn't exist.")
    sys.exit(1) # exit code missing file

lines = []

with file_path.open('r')as file:
    for i, line in enumerate(file, start=1)
        lines.append({
            "line": i,
            "content": line,
            "timestamp": datetime.datetime.now().isoformat()
        })

output_path = Path("output.json")
with output_path.open('w')as file:
    json.dump(line, file, indent=4)

print(f"Saved {len(lines)} lines to '{output_path}'")
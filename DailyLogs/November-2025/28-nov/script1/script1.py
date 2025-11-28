import argparse
from pathlib import Path

# define function  with two argument path and keyword
# check if path exist
# if exist open file and read line by line for keyword

def grep_file(file_path, keyword):
    path = Path(file_path)

    if not path.exists():
        print(f"Error: file doesn't exist")
        return
    
    if not path.is_file():
        print(f"Error: Not a file")
        return
    
    with open(path, 'r')as file:
        for num, line in enumerate(file, start=1):
            if keyword.lower() in line.lower():
                print(f"{num}: {line.rstrip()}")

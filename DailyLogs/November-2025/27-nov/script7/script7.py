import argparse
from pathlib import Path

def file_list(Directory, show_all=True, ext=None):
    dir_path = Path(Directory)

    files = []
    for entry in dir_path.iterdir():
        if entry.is_file():
            if not show_all and entry.name.startswith("."):
                continue

            if ext and entry.suffix != ext:
                continue

            files.append(entry.name)
    
    for f in sorted(files):
        print(f)


def count_file(Directory, show_all=True, ext=None):
    dir_path = Path(Directory)

    count = 0
    for entry in dir_path.iterdir():
        if entry.is_file():
            if not show_all and entry.name.startswith("."):
                continue
            
            if ext and entry.suffix != ext:
                continue

            count += 1

    print(count)
    
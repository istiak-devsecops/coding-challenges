'''
- Write a CLI tool called filetool.py:
- Options:
- --list → list files in a directory.
- --delete PATTERN → delete files matching regex.
- --backup → compress files into a .tar.gz archive.
- Use argparse to handle arguments.


'''
import argparse
import tarfile
import re
from pathlib import Path
import sys
import shutil
from datetime import datetime

def list_files(directory: Path):
    if not directory.exists() or not directory.is_dir():
        print(f"Directory not found: {directory}")
        sys.exit(1)

    for item in sorted(directory.iterdir()):
        if item.is_file():
            print(item.name)
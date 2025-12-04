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

def delete_files(directory: Path, pattern: str):
    regex = re.compile(pattern)

    deleted = []
    for file in directory.iterdir():
        if file.is_file() and regex.search(file.name):
            file.unlink()
            deleted.append(file.name)

    if deleted:
        print("Deleted:")
        for f in deleted:
            print(f"  -", f)
    else:
        print("No matching files found.")


def backup_files(directory: Path, output: Path):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    archive_name = output / f"backup_{timestamp}.tar.gz"

    with tarfile.open(archive_name, "w:gz") as tar:
        for file in directory.iterdir():
            if file.is_file():
                tar.add(file, arcname=file.name)

    print(f"Backup created: {archive_name}")


def main():
    parser = argparse.ArgumentParser(description="Simple file management tool")

    parser.add_argument("--dir", default=".", help="Target directory (default: current directory)")
    parser.add_argument("--list", action="store_true", help="List files in the directory")
    parser.add_argument("--delete", metavar="PATTERN", help="Delete files matching regex pattern")
    parser.add_argument("--backup", action="store_true", help="Create a backup .tar.gz archive")

    args = parser.parse_args()

    directory = Path(args.dir).resolve()

    if args.list:
        list_files(directory)

    if args.delete:
        delete_files(directory, args.delete)

    if args.backup:
        backup_files(directory, directory)


if __name__ == "__main__":
    main()
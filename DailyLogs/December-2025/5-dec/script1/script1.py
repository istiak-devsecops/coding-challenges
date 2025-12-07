import argparse
from pathlib import Path
import shutil
from datetime import datetime

def organize_by_extension(files):
    return sorted(files, key=lambda f: f.suffix.lower())

def organize_by_date(files):
    return sorted(files, key=lambda f: f.stat().st_mtime)

def organize_by_size(files):
    return sorted(files, key=lambda f: f.stat().st_size)

def main():
    parser = argparse.ArgumentParser(description="Organize files in a directory.")
    parser.add_argument("path", help="Directory to organize")
    parser.add_argument("--by", choices=["extension", "date", "size"], default="extension",
                        help="Organize files by this field")
    parser.add_argument("--reverse", action="store_true", help="Reverse sorting order")
    parser.add_argument("--limit", type=int, help="Maximum number of files to process")
    parser.add_argument("--dry-run", action="store_true", help="Only show actions, do not move files")

    args = parser.parse_args()
import argparse
from pathlib import Path
import os
import stat
import datetime


def list_files(directory, show_all = False, long_format=False):
    for entry in sorted(Path(directory).iterdir()): # skip hidden files unless --all

        if not show_all and entry.name.startswith("."):
            continue

        if long_format:
            info = entry.stat()
            permissions = stat.filemode(info.st_mode)
            size = info.st_size
            mtime = datetime.datetime.fromtimestamp(info.st_mtime).strftime("%Y-%m-%d %H:%M")
        else:
            print(entry.name)

parser = argparse.ArgumentParser(description="Directory Lister")
parser.usage("Python3 script.py -- dir home/mastermind/dir_name --all")

parser.add_argument("--dir", default=".", metavar="Directory Name", help="Directory name to check.")
parser.add_argument("-a","--all", action="store_true", help="If you wants to see all the metadata with file.")
parser.add_argument("-l","--long", action="store_true", help="shows all the long list of file")

args = parser.parse_args()

list_files(args.dir, show_all=args.all, long_format=args.long)
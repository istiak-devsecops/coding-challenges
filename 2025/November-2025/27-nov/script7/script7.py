import argparse
from pathlib import Path

def file_list(directory, show_all=True, ext=None):
    dir_path = Path(directory)

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


def count_file(directory, show_all=True, ext=None):
    dir_path = Path(directory)

    count = 0
    for entry in dir_path.iterdir():
        if entry.is_file():
            if not show_all and entry.name.startswith("."):
                continue
            
            if ext and entry.suffix != ext:
                continue

            count += 1

    print(count)
    
parser = argparse.ArgumentParser(description="File utility tool")

subparser = parser.add_subparsers(dest="command", required=True)

list_parser = subparser.add_parser("list", help="shows list of file.")
list_parser.add_argument("directory",help="Target Directory")
list_parser.add_argument("--ext",metavar="EXT",help="filter by extenction")
list_parser.add_argument("--all",action="store_true",help="shows all the hidden file")


count_parser = subparser.add_parser("count", help="count number of files")
count_parser.add_argument("directory", help="Target directory")
count_parser.add_argument("--ext",metavar="EXT",help="filter by extenction")
count_parser.add_argument("--all",action="store_true",help="count all the hidden file")

args = parser.parse_args()

if args.command == "list":
    file_list(args.directory, args.all, args.ext)

elif args.command == "count":
    count_file(args.directory, args.all, args.ext)
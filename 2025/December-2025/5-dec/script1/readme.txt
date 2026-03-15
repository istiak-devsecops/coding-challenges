Write a Python script called organizer.py that uses argparse to organize files in a directory.
Requirements:
- Positional argument:
- path → the directory to organize.
- Optional arguments:
- --by → how to organize files. Choices: extension, date, size. Default: extension.
- --reverse → a flag (store_true) to reverse the sorting order.
- --limit → integer, maximum number of files to process.
- --dry-run → flag to only print what would happen, without actually moving files

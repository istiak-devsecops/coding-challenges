import argparse
from pathlib import Path


# function that will do the search operation
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


# main function that will take the command from CLI
def main():
    parser = argparse.ArgumentParser(description="search for a keyword inside a file.")
    parser.add_argument("--file",required=True,metavar="Full File path", help="Path to the log file.")
    parser.add_argument("--keyword",required=True,metavar="KEYWORD", help="Keyword to search for.")

    args = parser.parse_args()
    grep_file(args.file, args.keyword)

if __name__=="__main__":
    main()
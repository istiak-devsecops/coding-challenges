import tarfile
import pathlib
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 script.py <filename>")
        sys.exit(2) # invalid arguments

    file_path = pathlib.Path(sys.argv[1]).resolve() # create the full path


    # check if directory exist
    if not file_path.exists():
        print(f"{file_path} doesn't exist.")
        sys.exit(1) # missing file

    # check if its a directory
    if not file_path.is_file():
        print(f"{file_path} is not a directory.")
        sys.exit(1) # not a directory

    with tarfile.open(file_path, "r") as tar:
        for member in tar.getmembers():
            print(f"{member.name}\n{member.size}\n{member.mtime}")

if __name__=="__main__":
    main()
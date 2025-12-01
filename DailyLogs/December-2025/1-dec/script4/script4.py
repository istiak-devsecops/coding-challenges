import os
import sys
import tarfile

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 script.py <filename>")
        sys.exit(2) # invalid arguments

    file_path = os.path.abspath(sys.argv[1]) # create the full path


    # check if directory exist
    if not os.path.exists(file_path):
        print(f"{file_path} doesn't exist.")
        sys.exit(1) # missing file

    # check if its a file
    if not os.path.isfile()
        print(f"{file_path} is not a file.")
        sys.exit(1) # not a file

    with tarfile.open(file_path, "r:gz")as tar:
        data = tar.extractfile("etc/host")
        print(data.read().decode())

if __name__=="__main__":
    main()

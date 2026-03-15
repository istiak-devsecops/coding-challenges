import sys
import tarfile
import pathlib

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 script.py <filename>")
        sys.exit(2) # invalid arguments

    dir_path = pathlib.Path(sys.argv[1]).resolve() # create the full path


    # check if directory exist
    if not dir_path.exists():
        print(f"{dir_path} doesn't exist.")
        sys.exit(1) # missing directory

    # check if its a directory
    if not dir_path.is_dir():
        print(f"{dir_path} is not a directory.")
        sys.exit(1) # not a directory

    archive_file = "backup.tar.gz"
    
    with tarfile.open(archive_file, "w:gz")as tar:
        tar.add(dir_path, arcname=dir_path.name)
    
    
    print(f"{dir_path} has been archived at {archive_file}")

if __name__=="__main__":
    main()
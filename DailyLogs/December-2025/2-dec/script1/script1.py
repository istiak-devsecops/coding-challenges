
import sys
import pathlib
import shutil
import platform
from datetime import datetime, timedelta

def main():
    if len(sys.argv) < 2:
        print("usage: python3 script.py <filename>")
        sys.exit(2) # invalid arguments
    
    dir_path = pathlib.Path(sys.argv[1]).resolve()

    if not dir_path.is_dir():
        print(f"{dir_path} is not a directory.")
        sys.exit(1)
    
    if not dir_path.exists():
        print(f"{dir_path} does not exist.")
        sys.exit(1)

    print(f"Scanning directory: {dir_path}\n")
    print(f"Files in directory: ")

    # dir list
    for file in dir_path.iterdir():
        print(f" - {file.name}\n")
        print()

    # system info
    print("System Info:")
    print(f"Python Version: {sys.version}")
    print(f"Platform: {platform.platform()}")
    print()

    # copy text file for backup
    backup_dir  = dir_path / "backup"
    backup_dir.mkdir(exist_ok=True, parents=True)

    print("Copying .txt files to the backup/:")
    for file in dir_path.iterdir():
        if file.is_file() and file.suffix == ".txt":
            shutil.copy2(file, backup_dir)
            print(f"copied: {file.name}")
    print()


    # delete temp files older than 7 days
    print(f"cleaning temp files older than 7 days:")
    time_differ = datetime.now() - timedelta(days=7)


    for file in dir_path.iterdir():
        if file.is_file() and file.suffix in [".tmp", ".temp", ".log"]:
            print(f"Deleting old temp file: {file.name}")
            file.unlink()
    print("\nDone!")

if __name__=="__main__":
    main()



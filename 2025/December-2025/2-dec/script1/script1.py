import sys
import pathlib
import shutil
import platform
from datetime import datetime, timedelta

def main():
    if len(sys.argv) < 2:
        print("usage: python3 script.py <directory>")
        sys.exit(2)

    dir_path = pathlib.Path(sys.argv[1]).resolve()

    # Check existence first
    if not dir_path.exists():
        print(f"{dir_path} does not exist.")
        sys.exit(1)

    if not dir_path.is_dir():
        print(f"{dir_path} is not a directory.")
        sys.exit(1)

    print(f"Scanning: {dir_path}\n")

    print("Files:")
    for file in dir_path.iterdir():
        print(f" - {file.name}")
    print()

    # System info
    print("System Info:")
    print(f"Python: {sys.version}")
    print(f"Platform: {platform.platform()}\n")

    # Backup .txt files
    backup_dir = dir_path / "backup"
    backup_dir.mkdir(exist_ok=True, parents=True)

    print("Backing up .txt files:")
    for file in dir_path.iterdir():
        if file.is_file() and file.suffix == ".txt":
            shutil.copy2(file, backup_dir)
            print(f"Copied: {file.name}")
    print()

    # Delete old temp files
    print("Removing temp files older than 7 days:")
    cutoff_time = datetime.now() - timedelta(days=7)

    for file in dir_path.iterdir():
        if file.is_file() and file.suffix in (".tmp", ".temp", ".log"):
            last_modified = datetime.fromtimestamp(file.stat().st_mtime)
            if last_modified < cutoff_time:
                print(f"Deleting: {file.name}")
                file.unlink()
    print("\nDone!")

if __name__ == "__main__":
    main()

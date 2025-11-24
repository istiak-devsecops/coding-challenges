import sys
import shutil
import datetime
from pathlib import Path

# check if there is a valid arguments
if len(sys.argv) < 2:
    print("Usage: python3 script.py <arguments>")
    sys.exit(2) # exit code invalid arguments

file_path = Path(sys.argv[1]).resolve()
timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M")

backup_dir = Path("backup") # set backup dir name
backup_dir.mkdir(exist_ok=True) # create backup dir

# create backup file name with timestamp and suffix
backup_file = backup_dir/f"{file_path.stem}_{timestamp}{file_path.suffix}"


try:
    # Check if file exists and is a file
    if not file_path.is_file():
        raise FileNotFoundError(f"{file_path} does not exist or is not a file.")
    
    # Copy file
    shutil.copy2(file_path, backup_file)
    print(f"Backup created: {backup_file}")

except FileNotFoundError as e:
    print(f"Error: {e}")
except PermissionError:
    print(f"Error: Permission denied while accessing {file_path} or {backup_file}")
except IsADirectoryError:
    print(f"Error: {file_path} is a directory, not a file.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
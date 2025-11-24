import shutil
import sys
import datetime
from pathlib import Path

# check if there is a arguments
if len(sys.argv) < 2:
    print("usage: python3 script.py <arguments>")
    sys.exit(2) # exit code invalid arguments

abs_path = Path(sys.argv[1]).resolve() # absoulate path
timestamp = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
archive_name = f"{abs_path.stem}_{timestamp}"

# check if the dir exist
if not abs_path.exists():
    print("Directory doesn't exist")
    sys.exit(1) # missing directory

# check if its a directory
if not abs_path.is_dir():
    print("Not a directory.")
    sys.exit(1) # missing directory


shutil.make_archive(archive_name,"zip",abs_path)
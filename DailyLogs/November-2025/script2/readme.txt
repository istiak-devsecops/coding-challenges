Create Timestamped Backup of a File

- Accept filename via CLI
- Use Path to check if file exists
- Generate timestamp string
- Copy file into "backups" folder with timestamp suffix

import sys
import shutil
import datetime
from pathlib import Path

if len(sys.argv) < 2:
    print("Usage: python3 script.py <arguments>")
    sys.exit(2) # exit code invalid arguments

file_path = Path(sys.argv[1])
timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M")
backup_dir = f"backup_{timestamp}"

if file_path.exists():
    shutil.copy2(file_path,backup_dir)

print(f"{file_path} copied to {backup_dir}")


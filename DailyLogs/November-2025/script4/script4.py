import shutil
import sys
import logging
import datetime
from pathlib import Path


# log file
logging.basicConfig(filename="app.log",level=logging.DEBUG, format="%(asctime)s %(levelname)s: %(message)s")

# check if there is a arguments
if len(sys.argv) < 2:
    logging.error("Arguments missing")
    print("usage: python3 script.py <arguments>")
    sys.exit(2) # exit code invalid arguments

dir_path = Path(sys.argv[1]).resolve()  # get the absoulate path
backup_dir = Path.mkdir("Backup-log")   # backup dir for logs
timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")


# check if dir exist
if not dir_path.exists():
    logging.error("Directory doesn't exist.")
    print("Directory doesn't exist")
    sys.exit(1) # exit code missing directory

# check if its a directory
if not dir_path.is_dir():
    logging.error("Not a directory")
    print("Not a directory")
    sys.exit(1) # exit code missing directory

logging.info("Program initiating...")

# logic to find the logs
for log in dir_path.rglob("*.log"):
    backup_file = f"{log.stem}_{timestamp}{log.suffix}"
    shutil.copy(log, backup_dir)
    logging.info(f"{backup_file} moved to {backup_dir}")

logging.info("Backup complete.")

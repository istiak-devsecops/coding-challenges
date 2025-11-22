import os
import shutil
import datetime
import logging
import sys


logging.basicConfig(filename="data.log", level=logging.DEBUG, format="%(asctime)s %(levelname)s: %(message)s")

if len(sys.argv) < 2:
    logging.error("Invalid arguments: Usage:python3 script.py <command>")
    sys.exit(2) # invalid arguments

src_dir = sys.argv[1]
timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M")
backup_dir = f"backup_{timestamp}"

logging.info(f"Source Directory: {src_dir}")
logging.info(f"Backup Directory: {backup_dir}")

if not os.path.exists(src_dir):
    logging.error("Source directory doesn't exist!")
    sys.exit(1) # missing file

try:
    shutil.copytree(src_dir, backup_dir)
    logging.info(f"Backup Successfull!")
    sys.exit(0)  # success
except Exception as e:
    logging.error(f"Backup Failed: {e}")
    sys.exit(1) # failed
 Disk Usage Reporter
Modules: os, logging
- Walk through a directory with os.walk().
- Calculate total size of files.
- Log the results into disk_report.log.


import os
import logging
import sys

logging.basicConfig(filename="disk_usage_report.log",level=logging.DEBUG,format="%(asctime)s %(levelname)s: %(message)s")

# check if arguments is missing
if len(sys.argv) < 2:
    logging.error("Missing arguments...")
    print(f"Usage: python3 script.py <Dir name>")
    sys.exit(2) # exit code for invalid arguments


dir_path = sys.argv[1]

# check if the directory exist
if not os.path.isdir(dir_path):
    logging.error("Directory doesn't exist.")
    print(f"{dir_path} is missing.")
    sys.exit(1) # exit code for missing file

total_size = 0

logging.info("Initiating the program...")

# calculate total file size recursively
for root, dirs, files in os.walk(dir_path):
    for dir in dirs:
        full_dir_path = os.path.join(root,dir)
        dir_size = os.path.getsize(full_dir_path)
        total_size += dir_size
        logging.info(f"The directory size of {full_dir_path} is {dir_size}")

logging.info(f"Total size of the {dir_path} is {total_size}")
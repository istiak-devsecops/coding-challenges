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

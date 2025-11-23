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
    for file in files:
        full_path = os.path.join(root,file)
        try:
            file_size = os.path.getsize(full_path)
            total_size += file_size
            logging.info(f"File: {full_path} | Size: {file_size} bytes")
        except Exception as e;
            logging.error(f"Failed to calculate file size {full_path} | Error: {e}")

logging.info(f"Total size of the {dir_path} is {total_size}bytes")
print(f"File size calcualtion completed. File: {full_path} | Size: {total_size}")
import os
import sys
import logging

logging.basicConfig(filename="backup.log",level=logging.DEBUG,format="%(asctime)s %(levelname)s: %(message)s")

if len(sys.argv) < 2:
    logging.error("Missing Arguments: ")
    print(f"Usage: python3 script.py <arguments>")
    sys.exit(2) # invalid arguments

dir_path = sys.argv[1] #dir name

# check if the directory exist
if not os.path.isfile(dir_path):
    logging.error("Directory doesn't exist.",dir_path)
    print("Directory doesn't exist.")
    sys.exit(1) # missing file

logging.info("Cleaning process begun...")
deleted_files = 0

# loging to check for .tmp file recursively
for root, dirs, files in os.walk(dir_path):
    for file in files:
        if file.endswith(".tmp"):
            fullpath = os.path.join(root,file)
            os.remove(fullpath)
            deleted_files += 1
            logging.info(f"{fullpath} been removed successfully.")
       
logging.info(f"Successfully cleaned {deleted_files} files.")
print(f"Successfully cleaned {deleted_files} files.")


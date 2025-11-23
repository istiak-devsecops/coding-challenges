import os
import sys
import logging

logging.basicConfig(filename="backup.log",level=logging.DEBUG,format="%(asctime)s %(levelname)s: %(message)s")

if len(sys.argv) < 2:
    logging.error("Missing Arguments: ")
    print(f"Usage: python3 script.py <arguments>")
    sys.exit(2) # invalid arguments

dir_name = sys.argv[1] #dir name
dir_path = os.path.join(dir_name) # dir name
logging.info("Cleaning process begun...")

for root, dirs, files in os.walk(dir_path):
    for file in files:
        if file.endswith(".tmp"):
            fullpath = os.path.join(root,file)
            os.remove(fullpath)
            logging.info(f"{fullpath} been removed successfully.")
        else:
            logging.error(f"Not possible to remvoe.")

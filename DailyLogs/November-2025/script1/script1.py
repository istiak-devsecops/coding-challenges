import sys
from pathlib import Path
import logging


logging.basicConfig(filename="script_report.log", level=logging.DEBUG,
                    format="%(asctime)s %(levelname)s: %(message)s")

# check if there is at least one arguments
if len(sys.argv) < 2:
    logging.error("Missing Arguments...")
    print("Usage: python3 script.py <arguments>")
    sys.exit(2) # exit code invalid arguments

dir_path = Path(sys.argv[1]).resolve() # absuloute path

# check if directory exist
if not dir_path.is_dir():
    logging.error("Directory doesn't exist.")
    print(f"{dir_path} is invalid...")
    sys.exit(1) # exit code for missing file

python_file_list = []

logging.info("Program initiating...")

# logic that filter .py files
for item in dir_path.iterdir():
    if item.is_file() and item.suffix == ".py":
        python_file_list.append(item.name)
        logging.info(f"{item.name} added to the list.")

logging.info(f"File list is ready...")
print("Here are the file list start with .py:\n")
for file in python_file_list:
    print(file)
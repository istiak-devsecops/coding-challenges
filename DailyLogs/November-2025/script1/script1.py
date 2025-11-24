import sys
from pathlib import Path
import logging


logging.basicConfig(filename="script_report.log", level=logging.DEBUG,
                    format="%(asctime)s %(levelname)s: %(message)s",
                    handlers=
                    [logging.FileHandler("script_report.log"),
                    logging.StreamHandler()])

if len(sys.argv) < 2:
    logging.error("Missing Arguments...")
    print("Usage: python3 script.py <arguments>")
    sys.exit(2) # exit code invalid arguments

dir_path = Path(sys.argv[1]).resolve() # absuloute path

python_file_list = []

logging.info("Program initiating...")

for files in Path(dir_path).iterdir():
    for file in files:
        if file.endswith(".py"):
            python_file_list.append(file)
            logging.info(f"{file} added to the list.")

logging.info(f"File list is ready...")
print("Here are the file list start with .py:\n",{python_file_list})
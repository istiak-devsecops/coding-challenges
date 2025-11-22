import os
import sys
import shutil
import logging

logging.basicConfig(filename="data.log", level=logging.DEBUG, format="%(asctime)s %(levelname)s: %(message)s")

if len(sys.argv) <2:
    logging.error("Invalid arguments: Usage: python3 script.py <arguments>")
    sys.exit(2) # invalid arguments

target_folder = sys.argv[1]

if not os.path.exists(target_folder):
    logging.error("Target folder does not exist!")
    sys.exit(1)

logging.info(f"Organizing files inside: {target_folder}")

try:
    for filename in os.listdir(target_folder):
        file_path = os.path.join(target_folder, filename)

        # Skip directories
        if os.path.isdir(file_path):
            logging.debug(f"Skipping directory: {filename}")
            continue

        # Extract extension
        _, extension = os.path.splitext(filename)

        if extension == "":
            extension = "no_extension"

        # Create folder based on extension
        ext_folder = os.path.join(target_folder, extension.replace(".", ""))

        if not os.path.exists(ext_folder):
            os.makedirs(ext_folder)
            logging.info(f"Created folder: {ext_folder}")

        # Move file
        shutil.move(file_path, ext_folder)
        logging.info(f"Moved {filename} → {ext_folder}")

    logging.info("File organization completed successfully.")
    sys.exit(0)

except Exception as e:
    logging.error(f"Error while organizing files: {e}")
    sys.exit(1)

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
timestamp = datetime.datetime.now().strftime("%Y-%m-%d")
backup_dir = f"backup_{timestamp}"

src_path = os.path.join(src_dir) # full dir path

if os.path.exists(src_dir):
    shutil.copytree(src_dir, backup_dir)
    logging.info("Directory backup successful.")
else:
    logging.error("Directory doesn't exist!")
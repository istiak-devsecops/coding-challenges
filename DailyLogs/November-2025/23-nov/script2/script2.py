import os
import sys
import shutil
import logging

logging.basicConfig(filename="backup.log",level=logging.DEBUG,format="%(asctime)s %(levelname)s: %(message)s")

if len(sys.argv) < 2:
    logging.error("Missing Arguments: ")
    print(f"Usage: python3 script.py <arguments>")
    sys.exit(2) # invalid arguments
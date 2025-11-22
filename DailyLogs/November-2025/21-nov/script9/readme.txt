File Organizer by Extension

- Import os, shutil
- Accept target folder via sys.argv
- For each file in folder:
    - Get extension (e.g., .txt, .jpg)
    - Create subfolder named after extension if not exists
    - Move file into that subfolder using shutil.move()

    import os
import sys
import shutil
import logging

logging.basicConfig(filename="data.log", level=logging.debug, format="%(asctime)s %(levelname)s: %(message)s")

if len(sys.argv) <2:
    logging.error("Invalid arguments: Usage: python3 script.py <arguments>")
    sys.exit(2) # invalid arguments



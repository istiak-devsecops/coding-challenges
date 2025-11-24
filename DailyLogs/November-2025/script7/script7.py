import sys
import time
import datetime
import subprocess
from pathlib import Path
import logging

logging.basicConfig(filename="script.log",level=logging.DEBUG, format="%(asctime)s %(levelname)s: %(message)s")


# check if there is an arguments
if len(sys.argv) < 2:
    logging.info("Missing arguments.")
    print(f"Usage: python3 script.py <arguments>")
    sys.exit(2) # missing arguments

file_path = Path(sys.argv[1]).resolve()

if not file_path.exists() or not file_path.is_file():
    logging.error(f"{file_path} is not a valid path or file.")
    print("Not a valid path or file.")
    sys.exit(1) # exit code missing file

start_time = datetime.datetime.now()
logging.info("Program initiating...")
logging.info(f"Starting time: {start_time}")
result = subprocess.run([sys.executable, str(file_path)],capture_output=True, text=True)
time.sleep(2)
logging.debug(result.stdout if result.stdout else 'No output')
logging.debug(result.stderr if result.stderr else 'No error')
logging.info("Program ended...")
end_time = datetime.datetime.now()
logging.info(f"End time: {end_time}")
sys.exit(0) # exit code success





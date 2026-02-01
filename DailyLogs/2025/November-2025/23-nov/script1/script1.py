import sys
import logging
import subprocess

logging.basicConfig(filename="app.log",level=logging.DEBUG,format="%(asctime)s %(levelname)s: %(message)s")

if len(sys.argv) < 2:
    logging.error("Missing Arguments: Usage: python3 script.py <arguments>")
    sys.exit(2) # invalid arguments

commands = " ".join(sys.argv[1:]) # join all the commands into a single string

logging.info(f"Shell command is running...")
result = subprocess.run(commands, capture_output=True, shell=True, text=True)

if result.stdout:
    logging.info(f"Result Output: \n{result.stdout}")

if result.stderr:
    logging.error(f"Result Error: \n{result.stderr}")

logging.info(f"Exit code: {result.returncode}")
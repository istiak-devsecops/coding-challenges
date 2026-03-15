import sys
import os
from datetime import datetime

script_name = os.path.basename(sys.argv[0])
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
log_file = f"{script_name}_{timestamp}.log"

with open(log_file, "w")as file:
    file.write(f"Log file created by {script_name} at {timestamp}")

print(f"Log file created {log_file}")
# Cross-Module Scripting Challenge

Goal: Create a script that logs system info into a timestamped file.
Steps:
1. 	Use  to get OS, architecture, and Python version.
2. 	Use  to generate a timestamp.
3. 	Save the info to a file named 

import datetime
import platform
import os

time_stamp = datetime.datetime.now().strftime("%Y-%m-%d")
file_name = os.path.join(f"system_snapshot_{time_stamp}.txt")

with open(file_name, "w")as file:
    file.write("The system info: ")
    file.write(platform.system())
    file.write(platform.machine())
    file.write(platform.version())

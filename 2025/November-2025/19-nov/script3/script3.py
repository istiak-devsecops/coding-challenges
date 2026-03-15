import sys
import os
from datetime import datetime

script_name = sys.argv[0] 
script_path = os.path.abspath(script_name)
current_time = datetime.now().strftime("%Y-%m-%d")

print(f"Script name: {script_name}\nScript path: {script_path}\nScript runtime: {current_time}")
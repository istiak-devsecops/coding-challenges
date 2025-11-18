import os
import shutil
from datetime import datetime

files = os.listdir()    # list all the file in current dir

for file in files:
    if file.endswith(".log") and os.path.isfile(file):
        creation_time = os.stat(file).st_ctime
        date_dir = datetime.fromtimestamp(creation_time).strftime("%Y-%m-%d")

        if not os.path.exists(date_dir):
            os.makedirs(date_dir)

        shutil.move(file, os.path.join(date_dir, file))

print(f"Logged file organized successfully!")





import os
import sys
import datetime

file_name = sys.argv[1]

if os.path.exists(file_name) and os.path.isfile(file_name):

    time_stamp = os.path.getmtime(file_name)
    formatted_time = datetime.datetime.fromtimestamp(time_stamp).strftime("%Y-%m-%d")

   # Split name and extension
    base, ext = os.path.splitext(file_name)
    new_name = f"{base}_{formatted_time}{ext}"

    os.rename(file_name, new_name)
    print(f"Renamed to: {new_name}")
else:
    print("File does not exist or is not a regular file.")


   

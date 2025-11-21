import datetime
import shutil
import os
import sys

time_stamp = datetime.datetime.now().strftime("%Y-%m-%d")

if len(sys.argv) < 2:
    print("Usage: python3 script.py <Directory name to archive>")
    sys.argv(2) # invalid arguments

dir_name = sys.argv[2]      # directory name from CLI
archived_dir_name = os.path.join(f"{dir_name}_{time_stamp}")    # archived directory name
moved_file_to_dir = shutil.copytree(dir_name,archived_dir_name)  # copy whole dir to archive directory
archive_file = shutil.make_archive(f"archive{time_stamp}","zip",archived_dir_name)  # compress the archive folder into archive.zip

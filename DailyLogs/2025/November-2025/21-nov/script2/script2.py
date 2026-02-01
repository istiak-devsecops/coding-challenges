import datetime
import shutil
import sys

time_stamp = datetime.datetime.now().strftime("%Y-%m-%d")

if len(sys.argv) < 2:
    print("Usage: python3 script.py <Directory name to archive>")
    sys.exit(2) # invalid arguments

dir_name = sys.argv[1]      # directory name from CLI
archived_dir_name = f"{dir_name}_backup_{time_stamp}"    # archived directory name
moved_file_to_dir = shutil.copytree(dir_name,archived_dir_name)  # copy whole dir to archive directory
archive_path = shutil.make_archive(f"archive{time_stamp}","zip",dir_name)  # compress the archive folder into archive.zip


print(f"Backup created at: {archived_dir_name}")
print(f"Archive created at: {archive_path}")
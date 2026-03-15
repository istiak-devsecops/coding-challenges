import platform
import datetime
import os
import getpass

operating_system = platform.system()
release = platform.release()
version = platform.version()
arch = platform.machine()
current_working_dir = os.getcwd()
current_user = getpass.getuser()
timestamp = datetime.datetime.now().strftime("%Y/%m/%d:: %H:%M:$S")

with open("platform_info.txt", "w")as file:
    file.write("Platform Info\n")
    file.write(f"TimeStamp: {timestamp}\n")
    file.write(f"==========\n")
    file.write(f"Operating System: {operating_system}\n")
    file.write(f"Release: {release}\n")
    file.write(f"Version: {version}\n")
    file.write(f"Architecture: {arch}\n")
    file.write(f"Current Working Directory: {current_working_dir}\n")
    file.write(f"Current user: {current_user}\n")


# Count Files and Folders Separately

import os
import sys

files = dir = 0     # set initial value as 0
for item in os.listdir():   # list all the iteams in the current dir
    if os.path.isfile(item): # check if the item is a file
        files += 1
    elif os.path.isdir(item): # chekc if the item is a dir
        dir += 1

print(f"Files: {files}, Directory: {dir}")
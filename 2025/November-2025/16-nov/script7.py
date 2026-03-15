# Print Absolute Path of All Files in Current Directory

import os
import sys

print("Absolute path of files:")
for item in os.listdir():       # list all the currently available items
    if os.path.isfile(item):    # check if that is a file
        print(os.path.abspath(item))    # prints its absoulate path
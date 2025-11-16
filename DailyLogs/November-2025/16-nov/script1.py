# create a directory from command line argument

import os
import sys

if len(sys.argv) < 2:   # if there is less the 2 arguments means only 1
    print("usage: python script.py <Directory name>.")
else:
    directory = sys.argv[1]     # store the 2nd arguments in the directory variable
    os.makedirs(directory, exist_ok=True) # created a directory by that name
    print("A directory has been created named", directory) # give a success output message
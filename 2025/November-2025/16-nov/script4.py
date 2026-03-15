# rename a file from CLI

import os
import sys

if len(sys.argv) != 3:  # checking if there is exact 3 arguments
    print(f"Usage: python script.py <old name> <new name>.")
    sys.exit(1)
else:
    old_name, new_name = sys.argv[1], sys.argv[2]   # assign two name
    if os.path.exists(old_name):    # check if the old file exist
        os.rename(old_name,new_name)    # change the old file name to new one
        print(f"Renamed {old_name} to {new_name}.")
    else:
        print("The file not found.")

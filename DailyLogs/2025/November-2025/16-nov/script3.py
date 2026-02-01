# create a directory and list its contents

import os
import sys

if len(sys.argv) < 2:
    print("Usage: python script.py <file/dir name>.")
    sys.exit(1)  # stop the program immediately 

dir = sys.argv[1]  # name of the directory 
os.makedirs(dir,exist_ok=True) # created the directory
print(f"A directory created named {dir}")

print(f"Content of the directory: ")
print(os.listdir(dir))  # print all the content of the directory
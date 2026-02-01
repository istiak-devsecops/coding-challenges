# script 2 pseudocode

Check if a File Exists (from CLI)

import module

if less than 2 arguments:
    print(correct usage message)
    exit the program 

file = sys.argv[1]

if os.path.isfile(file):
    print(File exist)
    exit program
else:
    print(FIle doesn't exist)
    exit program
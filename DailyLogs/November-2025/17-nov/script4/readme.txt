Recursively List All Files in a Directory

import module

define the path and store it in the paths variable,
path will be the arguments from the user and check if there is an arguments

for root(current dir), files(files in that dir), dirs(sub dir) in os.walk(path):
    for file in files:
        print(os.path.join(root,file))
import sys
import os

paths = sys.argv[1] if len(sys.argv) > 1 else "."

for root, files, dirs in os.walk(paths):
    for file in files:
        print(os.path.join(root,file))
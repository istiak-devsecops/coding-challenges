import sys
import os

paths = sys.argv[1] if len(sys.argv) > 1 else "."

for root, files, dirs in os.walk(paths):
    for file in files:
        print(os.path.join(root,file))


script_path = os.path.abspath(sys.argv[0])

print(f"Script path is: {script_path}")
print(f"Script directory name is: {os.path.dirname(script_path)}")
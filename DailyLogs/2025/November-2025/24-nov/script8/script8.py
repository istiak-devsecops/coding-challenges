from pathlib import Path

root = input("Search here: ")
file_name = input("File name: ")

file_path = Path(root).resolve()

found_files = list(file_path.rglob(file_name))

if found_files:
    for f in found_files:
        print(f"{f} found.")
else:
    print(f"file not found.")

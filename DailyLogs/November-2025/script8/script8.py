from pathlib import Path

root = input("Search here: ")
file_name = input("File name: ")

file_path = Path(root).resolve()

found_files = [f for f in file_path.rglob("*") if f.name.lower() == file_name]

if found_files:
    for f in found_files:
        print(f"{f} found.")
else:
    print(f"file not found.")

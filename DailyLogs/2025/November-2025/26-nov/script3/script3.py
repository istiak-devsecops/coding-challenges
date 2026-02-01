import os
import argparse

def main():
    parser = argparse.ArgumentParser(description="File Checker")
    parser.add_argument("file_path", help="Path to the file to check")
    parser.add_argument("--size", action="store_true", help="Print file size if file exists")
    args = parser.parse_args()

    if os.path.isfile(args.file_path):
        print("File exists")
        if args.size:
            size = os.path.getsize(args.file_path)
            print(f"File size: {size} bytes")
    else:
        print("File not found")

if __name__ == "__main__":
    main()
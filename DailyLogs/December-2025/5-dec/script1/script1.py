import argparse
from pathlib import Path
import shutil
from datetime import datetime

def organize_by_extension(files):
    return sorted(files, key=lambda f: f.suffix.lower())

def organize_by_date(files):
    return sorted(files, key=lambda f: f.stat().st_mtime)

def organize_by_size(files):
    return sorted(files, key=lambda f: f.stat().st_size)

def main():
    parser = argparse.ArgumentParser(description="Organize files in a directory.")
    parser.add_argument("path", help="Directory to organize")
    parser.add_argument("--by", choices=["extension", "date", "size"], default="extension",
                        help="Organize files by this field")
    parser.add_argument("--reverse", action="store_true", help="Reverse sorting order")
    parser.add_argument("--limit", type=int, help="Maximum number of files to process")
    parser.add_argument("--dry-run", action="store_true", help="Only show actions, do not move files")

    args = parser.parse_args()

    base = Path(args.path).resolve()

    if not base.exists() or not base.is_dir():
        print("Invalid directory.")
        return

    files = [f for f in base.iterdir() if f.is_file()]

    if args.by == "extension":
        files = organize_by_extension(files)
    elif args.by == "date":
        files = organize_by_date(files)
    elif args.by == "size":
        files = organize_by_size(files)

    if args.reverse:
        files.reverse()

    if args.limit:
        files = files[:args.limit]

    for f in files:
        if args.by == "extension":
            folder_name = f.suffix[1:] if f.suffix else "no_extension"
        elif args.by == "date":
            ts = datetime.fromtimestamp(f.stat().st_mtime)
            folder_name = ts.strftime("%Y-%m-%d")
        else:  # size
            size = f.stat().st_size
            if size < 1_000_000:
                folder_name = "small"
            elif size < 10_000_000:
                folder_name = "medium"
            else:
                folder_name = "large"

        target_dir = base / folder_name

        if args.dry_run:
            print(f"[DRY RUN] Would move: {f.name} → {folder_name}/")
        else:
            target_dir.mkdir(exist_ok=True)
            shutil.move(str(f), str(target_dir))
            print(f"Moved: {f.name} → {folder_name}/")

if __name__ == "__main__":
    main()
import argparse
from pathlib import Path
import shutil

def backup(source: Path, dest: Path, verbose: bool):
    if verbose:
        print(f"[INFO] Backing up {source} to {dest}")

    # Create destination directory if missing
    dest.mkdir(parents=True, exist_ok=True)

    # Copy directory recursively
    shutil.copytree(source, dest / source.name, dirs_exist_ok=True)

    if verbose:
        print("[INFO] Backup completed")


def main():
    parser = argparse.ArgumentParser(description="backup script.", usage="python backup.py /var/log --dest <path> --verbose")

    parser.add_argument("source",type=Path,metavar="PATH", help="provide path to backup dir")
    parser.add_argument("--dest",default="/tmp",metavar="DESTINATION", help="destination path")
    parser.add_argument("--verbose",action='store_true',help="boolean flag")

    args = parser.parse_args()

    backup(args.source, args.dest, args.verbose)

if __name__=="__main__":
    main()


import argparse
import shutil
import tarfile
from pathlib import Path

# validate backup directory
def backup_dir(source, dest, compress=True):
    src = Path(source)
    dst = Path(dest)

    if not src.exists():
        print("Source doesn't exist.")
        return
    
    # create destination dir if not exist
    dst.mkdir(parents=True,exist_ok=True)

    # create dir name inside destination
    backup_name = f"{src.name}_backup"
    backup_d = dst / backup_name

    print(f"Backing up {src} to {backup_d}...")

    # copy directory tree
    if backup_d.exists():
        shutil.rmtree(backup_d)
    shutil.copytree(src, backup_d)


    # compress if flag been used
    if compress:
        tar_file = dst / f"{backup_name}.tar.gz"
        with tarfile.open(tar_file,"w:gx")as tar:
            tar.add(backup_d, arcname=backup_name)
        print(f"Compress to :{tar_file}")

def main():
    parser = argparse.ArgumentParser(description="Backup a directory with optional compression.")
    parser.add_argument("--source", required=True, help="Source directory to back up")
    parser.add_argument("--dest", required=True, help="Destination folder to store backup")
    parser.add_argument("--compress", action="store_true", help="Compress the backup into .tar.gz")

    args = parser.parse_args()

    backup_dir(args.source, args.dest, args.compress)


if __name__ == "__main__":
    main()       
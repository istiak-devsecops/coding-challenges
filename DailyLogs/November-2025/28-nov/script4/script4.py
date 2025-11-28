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
    backup_d = dst / src.name

    print(f"Backing up {src} to {backup_d}...")

    # copy directory tree
    if backup_d.exists():
        shutil.rmtree(backup_d)
    shutil.copytree(src, backup_d)


    # compress if flag been used
    if compress:
        tar_file = dst / f"{backup}.tar.gz"
        with tarfile.open(tar_file,"w:gx")as tar:
            tar.add(backup_d, arcname=backup)
        print(f"Compress to :{tar_file}")
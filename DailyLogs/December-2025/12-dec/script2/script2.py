import argparse
from pathlib import Path

def main():
    parser = argparse.ArgumentParser(description="backup script.", usage="python backup.py /var/log --dest <path> --verbose")

    parser.add_argument("source",type=Path,metavar="PATH", help="provide path to backup dir")
    parser.add_argument("--dest",default="/tmp",metavar="DESTINATION", help="destination path")
    parser.add_argument("--verbose",action='store_true',help="boolean flag")

    args = parser.parse_args()

    if args.verbose:
        print(f"[DEBUG] Source: {args.source}")
        print(f"[DEBUG] Destination: {args.dest}")

if __name__=="__main__":
    main()


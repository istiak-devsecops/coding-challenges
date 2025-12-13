import argparse

def main():
    parser = argparse.ArgumentParser(description="Demo script for multiple argparse flags")

    parser.add_argument("input", help="Input file or string to process.")
    parser.add_argument("-c","--count", type=int, default=1, help="Number of time to repete the task.")
    parser.add_argument("-m","--mode",choices=["fast","safe","debug"],default="safe",help="Execution mode")
    parser.add_argument("-v","--verbose",action="store_true",help="Enable verbose output.")
    parser.add_argument("--dry-run",action='store_true',help="Simulate actions without executing.")

    # mutually exclusive group

    group = parser.add_mutually_exclusive_group()
    group.add_argument("--upper",action="store_true", help="conver input into uppercase.")
    group.add_argument("--lower",action='store_true',help="convert into lowercase.")

    args = parser.parse_args()

    text = args.input

    if args.upper:
        text = text.upper()
    elif args.lower:
        text = text.lower()

    if args.verbose:
        print(f"[DEBUG] Mode: {args.mode}")
        print(f"[DEBUG] Count: {args.count}")
        print(f"[DEBUG] Dry run: {args.dry_run}")

    for _ in range(args.count):
        if args.dry_run:
            print(f"[DRY RUN] Would output: {text}")
        else:
            print(text)


if __name__ == "__main__":
    main()

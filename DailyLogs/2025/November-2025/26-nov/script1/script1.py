import argparse

parser = argparse.ArgumentParser(description="Hello CLI")
parser.add_argument("--name", required=True, help="Your name")
args = parser.parse_args()

print(f"Hello {args.name}")
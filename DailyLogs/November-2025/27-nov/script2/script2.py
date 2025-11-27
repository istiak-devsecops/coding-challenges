import argparse

parser = argparse.ArgumentParser(description="Show name as output")

parser.usage = "Usage: python3 script2.py --name <username>"
parser.add_argument("--name", required=True, metavar="username", help="Write your username.")

args = parser.parse_args()

print("Hello",args.name)
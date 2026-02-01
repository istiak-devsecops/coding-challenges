import argparse

parser = argparse.ArgumentParser(description="Setting Default value")

parser.add_argument("--name",required=True,metavar="Username")
parser.add_argument("--gretting",default="Hello", metavar="Any Grettings")

args = parser.parse_args()

print(f"{args.gretting},{args.name}")



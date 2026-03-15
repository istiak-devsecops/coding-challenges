import argparse

parser = argparse.ArgumentParser(description="Simple calculator.")


parser.add_argument("--a",type=int, required=True, help="First number")
parser.add_argument("--b",type=int, required=True, help="Second number.")
parser.add_argument("--op",choices=["add","sub"], required=True,help="choice: add or sub")

args = parser.parse_args()

if args.op == "add":
    result = args.a + args.b
elif args.op == "sub":
    result = args.a - args.b

print(f"Result: {result}")
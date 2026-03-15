import argparse

parser = argparse.ArgumentParser(description="subcommands with argparse module")

subparsers = parser.add_subparsers(dest="command",required=True)

add_parser = subparsers.add_parser("add", help="add two number.")
add_parser.add_argument("a",type=int)
add_parser.add_argument("b",type=int)

sub_parser = subparsers.add_parser("sub", help="Substract number.")
sub_parser.add_argument("a",type=int)
sub_parser.add_argument("b",type=int)

mul_parser = subparsers.add_parser("multi", help="multiply numbers.")
mul_parser.add_argument("a",type=int)
mul_parser.add_argument("b",type=int)

div_parser = subparsers.add_parser("div", help="divide number.")
div_parser.add_argument("a",type=int)
div_parser.add_argument("b",type=int)

args = parser.parse_args()

a = args.a 
b = args.b 

if args.command == "add":
    print(a + b)
elif args.command == 'sub':
    print(a - b)
elif args.command == "multi":
    print(a * b)
elif args.command == 'div':
    if a == 0 or b == 0:
        print("Error: divison by zero")
    else:
        print(a / b)
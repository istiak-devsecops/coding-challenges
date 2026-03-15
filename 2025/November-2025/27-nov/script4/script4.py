import argparse

parser = argparse.ArgumentParser(description="Boolean flag for argument")

parser.usage = "python3 script4.py <username> [--gretting HI] [uppercase/U]"

parser.add_argument("name",metavar="username",help="put your username.")
parser.add_argument("--gretting",default="Hello",metavar="any grettings")
parser.add_argument("-U", "--uppercase", action="store_true")

args = parser.parse_args()

user_name = args.name
greet = args.gretting
upper_case = args.U

message = f"{greet}{user_name}"

if upper_case:
    message = message.upper()

print(message)
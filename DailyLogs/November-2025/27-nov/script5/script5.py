import argparse

parser = argparse.ArgumentParser(description="simple calculator using CLI")



parser.add_argument("-x", required=True, metavar="number1", type=int, help="Put an integer")
parser.add_argument("-y", required=True, metavar="number2", type=int, help="Put an integer")
parser.add_argument("-op", default="add", choices=["add","sub","multi","div"], required=True, metavar="+-*/")

args = parser.parse_args()

num1 = args.x
num2 = args.y
operation = args.op

if operation == "add":
    result = num1 + num2
elif operation == "sub":
    result = num1 - num2
elif operation == "multi":
    result = num1 * num2
elif operation == "div":
    result = num1 / num2

print(f"Result: {result}")
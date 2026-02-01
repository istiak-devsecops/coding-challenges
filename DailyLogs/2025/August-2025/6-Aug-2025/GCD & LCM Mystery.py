# Euclidean algorithm (for GCD amd LCM)

try:
    num1 = int(input("Pick first number: "))
    num2 = int(input("Pick 2nd number: "))
    if num1 <= 0 or num2 <= 0:
        print("Only Positive number allowed. ")
        exit()
except ValueError:
    print("Write any positive integer number. ") # warning messages for users to put the right input
    exit()

def gcd(a,b):
    while b != 0:             #keep running the loop till a % b == 0
        a , b = b, a % b     # a = b  and b = a % b Euclidean methods
    return a

def lcm(a,b):
    return abs((a * b)// gcd(a,b))     # will return lcm in euclidean methods
    
def main():
    print(f"The GCD of {num1} and {num2} is {gcd(num1, num2)}")
    print(f"The LCM of {num1} and {num2} is {lcm(num1, num2)}")

if __name__ == "__main__":
    main()
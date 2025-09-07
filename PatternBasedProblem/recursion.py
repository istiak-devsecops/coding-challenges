#Write a recursive function to calculate factorial of n.

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)  #keep multiplying till met the smallest number 
    

user_input = int(input("Write down a number you wants to know factorial of: "))

result = factorial(user_input)
print(f"Factorial of {user_input} is {result}")
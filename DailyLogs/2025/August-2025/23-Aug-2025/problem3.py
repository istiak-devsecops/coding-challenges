"""Factorial with Recursion

Write a recursive function to calculate factorial."""

#Define a function to calculate factorial
def factorial_counter(number):
    result = 1
    for num in range(2, number + 1):
        result *= num
    return result

#take user input
number = int(input("Write the number you wants to know factorial value: "))

print(factorial_counter(number))
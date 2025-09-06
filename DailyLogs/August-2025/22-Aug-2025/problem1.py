"""Write a function that returns all prime numbers up to n.
 Input: 20 → Output: [2, 3, 5, 7, 11, 13, 17, 19]"""

user_input = int(input("write down any number: "))

def prime_number_checker(number):
    prime_num = []
    for num in range(2, number + 1):
        is_prime = True
        for n in range(2, int(num**0.5) + 1):
            if num % n == 0:
                is_prime = False
                break
        if is_prime:
            prime_num.append(num)
    return prime_num

print(prime_number_checker(user_input))
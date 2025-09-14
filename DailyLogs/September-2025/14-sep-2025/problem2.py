#Write a function that takes two numbers start and end and returns a list of all prime numbers in that range.

def prime_checker(start,end):
    prime_list = []
    for number in range(start,end):
        if number > 1:
            for i in range(2, int(number ** 0.5) + 1):
                if number % i == 0:
                    break
            else:
                prime_list.append(number)

    return prime_list

primes = prime_checker(3,87)
print(primes)
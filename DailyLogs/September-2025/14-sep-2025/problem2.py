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

#taking input from user


while True:
    #validing the range
    start = int(input("Write the first number: "))
    end = int(input("Write the 2nd number: "))
    if start > end:
        print("range should be in acending order(from low to high). Try again!")
    else:
        primes = prime_checker(start,end)
        print(f"The primes between {start} and {end} are: {primes}")
        user_input = input("You wants to continue or stop?Type 'y/n': ")
        if user_input.lower() == "n":
            break
        else:
            continue



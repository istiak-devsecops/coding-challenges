#Guess the number

import random

secret_num = random.randint(1,10)

def guess():
    while True:
        try:
            user_input = int(input("Guess the number from 1 to 10: "))
            if user_input == secret_num:
                print("This is the correct number.")
                break
            else:
                print("try again!")
        except ValueError:
            print("Enter a valid integer!")

guess()
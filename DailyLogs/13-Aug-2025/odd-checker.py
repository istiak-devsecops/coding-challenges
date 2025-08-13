
def EvenOddChecker(num):        #define a function to check even and odd
    num != 0
    if num % 2 == 0:
        print(f"{num} is a even number.")
    else:
        print(f"{num} is a odd number.")

            
try:                            #added value error
    while True:                    
        user_input = int(input("Put any number to know its even or odd: "))
        EvenOddChecker(user_input)
        user_opinion = input("You wants to continue or break Type 'y/n'.")
        if user_opinion == "y":
            print("Thanks for running the program.")
        elif user_opinion == "n":
            break
except ValueError:
    print("Please type 'y/n' in lower case to proceed")
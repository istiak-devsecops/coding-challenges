
def EvenOddChecker(num):        #define a function to check even and odd
    num != 0
    if num % 2 == 0:
        print(f"{num} is a even number.")
    else:
        print(f"{num} is a odd number.")

            
                          
while True:      
    try:           
        user_input = int(input("Put any number to know its even or odd: "))
        EvenOddChecker(user_input)
    except ValueError:
        print("Hey Put a valid integer. ") #value error added
        continue

    user_opinion = input("if you wants to exit type 'end' and continue type 'start': ").lower()
    
    if user_opinion == "start":         # user opinion to continue or terminate
        continue
    elif user_opinion == "end":
        print("Thanks for running the program.")
        break
    

    
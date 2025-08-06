#FizzBuzz

user_inp = int(input("Pick any number: "))

fizzbuzz = []

for i in range(1, user_inp+1):
    
    if i % 3 == 0 and i % 5 == 0:
        fizzbuzz.append("FizzBuzz") # if multiple of 3 and 5 will add fizzbuzz
    elif i % 3 == 0:
        fizzbuzz.append("Fizz") # if multiple of 3 will add fizz
    elif i % 5 == 0:
        fizzbuzz.append("Buzz") # if multiple of 5 will add buzz
    else:
        fizzbuzz.append(i) # will add i 

print(f"Here are the array {fizzbuzz}")




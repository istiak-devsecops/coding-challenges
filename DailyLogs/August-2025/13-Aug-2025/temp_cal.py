#Temperature converter

user_input = float(input("Enter temperature in celsius: "))

def temp(i):
    tempa = (i * 9/5) + 32
    return tempa            #return temparature in fahrenheit


print(f"Temperature in fahrenheit is: {temp(user_input):.2f}")
# Write a function that accepts any number of numbers (*args) and returns the largest one.

def find_largest_num(*args):
    return max(args)

num1 = []
num2 = []
num3 = []

lists = [num1,num2,num3]
current_list = 0

while True:
    user_input = input("write a number or 'break': " )

    if user_input.lower() == "break":
        break
    
    try:
        number = int(user_input)
    except ValueError:
        print("Write a valid positive number.")
        continue
    
    if current_list < len(lists):
        if len(lists[current_list]) < 3:
            lists[current_list].append(number)
        elif len(lists[current_list]) == 3:
            current_list += 1
    else:
        print("All lines are full.")
        break

print(f"Num1: {num1}\nNum2: {num2}\nNum3: {num3}")

all_number_list = num1 + num2 + num3 
print(f"The largest number from the list is: {find_largest_num(*all_number_list)}")
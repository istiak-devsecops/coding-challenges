# Write a function that accepts any number of numbers (*args) and returns the largest one.

def find_largest_num(*args):  #Take multiple variables as arguments
    return max(args)

num1 = []
num2 = []
num3 = []

lists = [num1,num2,num3]
current_list = 0

while True:
    user_input = input("write a number or 'break': " )

    if user_input.lower() == "break": #if the user call break the loop will break
        break
    
    try:
        number = int(user_input)
    except ValueError:
        print("Write a valid positive number.")  #error handling
        continue
    
    if current_list < len(lists):   #current list can not be higher than lenghth of the lists
        if len(lists[current_list]) < 3:    #list will continue till the current_list is below 
            lists[current_list].append(number)
        else:
            current_list += 1   #start adding value to the next vaiable of the list
    else:
        print("All lines are full.")
        break

print(f"Num1: {num1}\nNum2: {num2}\nNum3: {num3}")

all_number_list = num1 + num2 + num3 
print(f"The largest number from the list is: {find_largest_num(*all_number_list)}")
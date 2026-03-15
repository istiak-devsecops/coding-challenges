# Task 3: Write a function that takes a list of integers and returns a new list
# where each element is replaced by "even" or "odd" depending on its parity.


#without list comprehention
def label_parity(numbers):
    new_list = []
    for num in numbers:
        if num % 2 == 0:
            new_list.append("even")
        else:
            new_list.append("odd")
    return new_list

number_list = [12,34,45,12,5456,567,787,34]
result = label_parity(number_list)
print(result)

#with list comprehention
def label(numbers):
    return ["even" if num % 2 == 0 else "odd" for num in numbers]

numbers = [12,34,45,12,5456,567,787,34]
result = label(numbers)
print(result)
# - Filter Even Numbers

nums = [1,3,4,45,56,22,13,67]

def even_num(num):
    return num % 2 == 0

list_of_even_number = list(filter(even_num, nums))
print(list_of_even_number)

# does the same thing with lambda function
list_of_even_number_2 = list(filter(lambda x:x%2 == 0, nums))
print(list_of_even_number_2)

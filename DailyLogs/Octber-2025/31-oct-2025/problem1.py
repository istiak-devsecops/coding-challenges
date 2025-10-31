# Given a list of integers, return a new list with each number squared.

list_num = [1, 2, 3, 4]

def square_root(nums):
    num2 = []
    for num in nums:
        num2.append(num**2)
    return num2

new_list = square_root(list_num)
print(new_list)

# doing the same thing with map function

def sqr_root(nums):
    return nums**2

new_list2 = list(map(sqr_root,list_num))
print(new_list2)

# using list comprehention

new_list3 = [num**2 for num in list_num]
print(new_list3)
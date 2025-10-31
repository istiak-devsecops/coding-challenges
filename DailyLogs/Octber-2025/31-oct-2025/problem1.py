# Given a list of integers, return a new list with each number squared.

list = [1, 2, 3, 4]

def square_root(nums):
    num2 = []
    for num in nums:
        num2.append(num**2)
    return num2

new_list = square_root(list)
print(new_list)


"""Find Second Largest Number

From a list, return the 2nd largest number."""

num_list = [10, 20, 4, 45, 99]

#remove the largest number
num_list.remove(max(num_list))

#find the largest which is 2nd largest from the list
second_largest_num = max(num_list)

print(f"The 2nd largest number from the list is: {second_largest_num}")
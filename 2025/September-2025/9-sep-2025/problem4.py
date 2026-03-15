nums = [2, 1, 5, 1, 3, 2]
k = 3

start = 0
stop = start + k

total_sub_array_list = []

while stop <= len(nums):
    subarray_list = nums[start:stop]
    total_sub_array_list.append((subarray_list, sum(subarray_list)))
    start += 1
    stop = start + k

max_subarray = max(total_sub_array_list, key=lambda x:x[1])
max_subarray_list, max_subarray_sum = max_subarray

print(f"Max subarray List: {max_subarray_list} \nMax subarray sum: {max_subarray_sum}")

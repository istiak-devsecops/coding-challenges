nums = [2, 1, 5, 1, 3, 2]
k = 3

start = 0
stop = start + k

sub_array_list = []

while stop <= len(nums):
    subarray_sum = nums[start:stop]
    sub_array_list.append((subarray_sum, sum(subarray_sum)))
    start += 1
    stop = start + k

max_subarray = max(sub_array_list, key=lambda x:x[1])
max_subarray_list, max_subarray_sum = max_subarray

print(f"Max subarray List: {max_subarray_list} \nMax subarray sum: {max_subarray_sum}")

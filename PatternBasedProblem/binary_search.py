# Given [1, 3, 5, 7, 9, 11], check if 7 exists using binary search.

nums = [1, 3, 5, 7, 9, 11]
target = 7

start = 0
end = len(nums) - 1

while start <= end:         #loop will continue till start is not greater than end
    mid = (start + end) // 2
    if nums[mid] == target:
        print(f"Found the target")
        break
    elif nums[mid] > target:    #if mid is greater than target then the number is before so move end to the left
        end = mid - 1
    else:
        start = mid + 1         #if mid is smaller than the target then the number is after so move start to the right

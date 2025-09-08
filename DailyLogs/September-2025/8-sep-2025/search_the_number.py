nums = [1, 3, 5, 7, 9]
target = 5


start = 0
end = len(nums) - 1


while start < end:
    mid = (start + end) // 2
    if nums[mid] > target:
        end = mid - 1
    elif nums[mid] < target:
        start = mid + 1
    else:
        print("Target found")
        break





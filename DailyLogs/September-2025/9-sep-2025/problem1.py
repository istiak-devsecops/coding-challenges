nums = [4,5,6,7,0,1,2] 
target = 0

start = 0
end = len(nums) - 1

while start <= end:
    mid = (start + end) // 2

    if nums[mid] == target:
        print(f"Found at index {mid}")
        break

    if nums[start] <= nums[mid]:
        if nums[start] <= target < nums[mid]:
            end = mid - 1
        else:
            start = mid + 1
            

    else:
        if nums[end] >= target > nums[mid]:
            start = mid + 1
        else:
            end = mid - 1


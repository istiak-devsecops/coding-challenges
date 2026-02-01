nums = [1, 2, 4, 6, 10]
target = 8


low = 0
high = len(nums) - 1

while low <= high:
    total = nums[low] + nums[high]
    if total == target:
        print("target found. The two pair is: ", nums[low],nums[high])
        break
    elif total > target:
        high -= 1
    else:
        low += 1

        

nums = [2, 7, 11, 15]
target = 9

start = 0
stop = len(nums) - 1

while start < stop:
    sums = nums[start] + nums[stop]
    if sums == target:
        print("Target found!")
        break
    elif sums > target:
        stop -= 1
    else:
        start += 1
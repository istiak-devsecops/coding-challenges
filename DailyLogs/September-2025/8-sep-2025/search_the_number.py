nums = [1, 3, 5, 7, 9]
target = 6


start = 0
end = len(nums) - 1
not_found = True


while start < end:
    mid = (start + end) // 2
    if nums[mid] > target:
        end = mid - 1           #Move the left one slot left
    elif nums[mid] < target:
        start = mid + 1         #Move the start one slot right
    else:
        print("Target found")
        not_found = False   #Target found so break the loop
        break

if not_found:       #Target not found so send the error messages
    print("The target is not in the list!")





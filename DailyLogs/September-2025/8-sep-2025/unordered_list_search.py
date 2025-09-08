number = [4,5,6,7,0,1,2] 
find_target = 0

def binary_search(nums, target):
    start, end = 0, len(nums) - 1

    while start <= end:
        mid = (start + end) // 2

        if nums[mid] == target:
            return mid
        
        if nums[start] <= nums[mid]:            #check if the left side of the list is sorted
            if nums[start] <= target < nums[mid]:
                end = mid - 1
            else:
                start = mid + 1
        
        else:
            if nums[end] >= target > nums[mid]: #check if the rigth side of the list is sorted
                start = mid + 1
            else:
                end = mid - 1
    return None

result = binary_search(number, find_target)
print(f"The index of the target is: {result}")
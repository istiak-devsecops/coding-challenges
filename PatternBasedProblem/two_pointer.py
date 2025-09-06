# Given a sorted list [1, 2, 4, 7, 11, 15] and a target 15, find two numbers that add up to the target.

number = [1, 2, 4, 7, 11, 15]
targets = 15

def two_pointer(nums, target):
    start = 0
    end = len(nums) - 1

    while start < end:
        current_sum = nums[start] + nums[end]

        if current_sum == target: 
            return (nums[start], nums[end]) #return the pair if found
        
        elif current_sum < target: 
            start += 1  #if the current sum is lower than the target then start will move one index right
        else:
            end -= 1    #if the current sum is greater than the target then end will move one index left
            
    return None #no pair found

result = two_pointer(number,targets)
print(f"Pair found: ",result)
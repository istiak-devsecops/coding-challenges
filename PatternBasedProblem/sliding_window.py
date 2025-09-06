#Find the maximum sum of any subarray of length 3 in [2, 1, 5, 1, 3, 2].

num_list = [2, 1, 5, 1, 3, 2]
length_of_subarray = 3  #subarray length to calculate

start = 0
stop = start + length_of_subarray

sum_of_subarray = [] #append a list of the sum of sumarray

while stop <= len(num_list):  #Loop will keep running till it doesn't exceed list lenght
        subarray = num_list[start:stop]
        sum_of_subarray.append(sum(subarray))
        start += 1                              #move the index by one to the right
        stop = start + length_of_subarray
        
print("Max sum of subarrary is:",max(sum_of_subarray))
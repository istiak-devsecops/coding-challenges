#Given a string, find the length of the longest substring without repeating characters.

s = "abcabcbb"
start = 0
max_length = 0
seen = {}

for end in range(len(s)): # end is the index number 
    char = s[end]       # char is the value of that index number

    # if value of char from the seen dict is euqal to start then increment the value of start
    if char in seen and seen[char] >= start: 
        start = seen[char] + 1 

    # update the char value in the seen dict to a current end index number
    seen[char] = end 

    # from the previous max_length value and the current (end - start + 1) value we are updating the value again with the largest one
    max_length = max(max_length, end - start + 1) 


print(f"The longest substring without repeating characters: {max_length}")
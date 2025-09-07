#Given a string, find the length of the longest substring without repeating characters.

s = "abcabcbb"
start = 0
max_length = 0
longest_substring = ""
seen = {}

for end in range(len(s)): # end is the index number 
    char = s[end]       # char is the value of that index number

    # if value of char from the seen dict is euqal to start then increment the value of start
    if char in seen and seen[char] >= start: 
        start = seen[char] + 1 

    # update the char value in the seen dict to a current end index number
    seen[char] = end 

     
    window_length = end - start + 1

    if window_length > max_length:
        max_length = window_length
        longest_substring = s[start:end + 1]
     
print(f"The longest substring without repeating characters: {longest_substring}: {max_length}")
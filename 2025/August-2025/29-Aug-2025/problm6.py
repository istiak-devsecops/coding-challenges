# Write a function that takes a word and returns the middle character(s):
# If length is odd → 1 char
# If length is even → 2 chars

user_input = input("write a single word: ")

#function to return middle char for odd and even word length
def middle_char_finder(text):
    n = len(text)
    if n ==  0:
       return text[n//2 - 1 : n//2 +1]
    else:
        return text[n//2]
    

print(f"Middle characters: {middle_char_finder(user_input)}")
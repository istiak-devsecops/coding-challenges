# Find the first non-repeating character in "aabbcdeff".

words = "aabbcdeff"
freq = {}

for char in words:
    freq[char] = freq.get(char, 0) + 1

for char in words:
    if freq[char] == 1:
        print(f"The first non repeative character is: {char}")
        break

print(f"Frequency of each character from the list are: {freq}")

import string
from collections import Counter

user_input = input("Write down a sentences: ").lower()

cleaned_input = ""

for char in user_input:
    if char not in string.punctuation and char != " ":
        cleaned_input += char

total_char = Counter(cleaned_input)     #count characters

max_freq = max(total_char.values())     #find max frequency

most_freq_word = [ ]

for char in total_char:
    if total_char[char] == max_freq:    
        most_freq_word.append(char)



print(f"Max Frequency: {max_freq}")
print(f"Most Frequent character: {most_freq_word}")




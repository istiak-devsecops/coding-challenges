#character frequency Counter

import string

user_input = input("Write down any sentence: ").lower()

freq_counter = {}

for word in user_input:
    if word not in string.punctuation and word != " ":
        if word in freq_counter:
            freq_counter[word] += 1
        else:
            freq_counter[word] = 1

for char in sorted(freq_counter.keys()):
    print(f"{char} - {freq_counter[char]}")
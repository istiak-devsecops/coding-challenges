# Normalize and count
import string

input_str = "  Linux   is   powerful. linux IS versatile.   "
word_list = input_str.strip().lower().split()

clean_words = []

for word in word_list:
    clean_word = ""
    for char in word:
        if char not in string.punctuation:
            clean_word += char
    clean_words.append(clean_word)

#store word by their frequency
word_freq = {}
for word in clean_words:
    if word in word_freq:
        word_freq[word] += 1
    else:
        word_freq[word] = 1

print(word_freq)
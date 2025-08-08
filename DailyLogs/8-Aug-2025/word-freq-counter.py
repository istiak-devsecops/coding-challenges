import string

user_input = input("Write a sentence. ").lower().split()

word_count = {}

for word in user_input:
    clean_word = word.strip(string.punctuation)  # remove punctuation
    if clean_word in word_count:
        word_count[clean_word] += 1
    else:
        word_count[clean_word] = 1


print(word_count)

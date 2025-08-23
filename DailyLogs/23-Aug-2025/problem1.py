#Count Unique Words

user_input = input("Write down a sentence to see the uniq word: ").lower().split()

import string

clean_word_list = []
#Remove punctuation and space from the list.
for word in user_input:
    word = word.strip(string.punctuation)
    if word and not word.isspace():
        clean_word_list.append(word)

#use set to remove duplicates to find unique words
unique_words = set(clean_word_list)

print(f"Total unique words are {len(unique_words)} : {unique_words}")


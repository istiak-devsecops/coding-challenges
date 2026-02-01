# Find the longest word in a sentence.

sentence = "This is python. This works better, lets do some prepend not append"

word_list = sentence.lower().split()
max_word = ""

for word in word_list:
    clean_word = "".join(char for char in word if char.isalnum())

    if len(max_word) < len(clean_word):
        max_word = clean_word

print(max_word)
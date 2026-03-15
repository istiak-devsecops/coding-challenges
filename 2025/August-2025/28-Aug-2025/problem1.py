#Extract capitalized word with context


import string

text = "Python is great. Linux and Bash are powerful. DevSecOps is exciting."
text = text.split()

is_start_of_sentence = True # check if the word is in the start of the sentence
word_counter = []

for word in text:
    cleanword = word.strip(string.punctuation)
    if cleanword and cleanword[0].isupper() and not is_start_of_sentence:
         word_counter.append(cleanword)

# A word ends with ".", "?", "!" means the next word is the starting of the sentences
    if cleanword.endswith((".","?","!")): 
         is_start_of_sentence = True
    else:
         is_start_of_sentence = False

print(word_counter)
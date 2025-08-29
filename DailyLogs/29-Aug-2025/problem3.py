# Custom Title Case

input_str = "the art of DevOps and the science of security"
stopwords = ["and", "or", "the", "of"]

words = input_str.split()
word_list = []

for i, word in enumerate(words):
    if i == 0:  # First word of the sentence is always uppercase
        word_list.append(word.title())
    elif word.lower() not in stopwords:
        word_list.append(word.title())
    else:
        word_list.append(word.lower())
   

title_case_word = " ".join(word_list) #join the word together in a line

print(title_case_word)
# Task 5: Write a function that takes a list of strings and returns a dictionary.
# The dictionary should map each string to its length, but only include strings longer than 5 characters.

from collections import Counter

#without list comprehention
def filter_and_map(strings):
    dict_of_strings = {}    #store string longer than 5 in len
    for word in strings:
        if len(word) > 5:
            if word in dict_of_strings:
                dict_of_strings[word] += 1
            else:
                dict_of_strings[word] = 1
    return dict_of_strings

user_input = input("Write down something! ").strip().split()    # remove whitespace and split input seprated by whitespace
list_of_strings = []    # store list of string that doesn't have any special char

for word in user_input:
    clean_word = ""     # store string that doesn't have any special char
    for char in word:
        if char.isalnum():  # check if the char is alpha numeric if it is then it will add it to the clean_word
            clean_word += char
    list_of_strings.append(clean_word)  # finally add that clean word to the list_of_strings
 
result = filter_and_map(list_of_strings)
print(result)




#with list comprehention
def filter_and_map2(strings2):
    return dict(Counter(word for word in strings2 if len(word) > 5))

user_input2 = input("Write down something! ").strip().split()    # remove whitespace and split input seprated by whitespace

list_of_strings2 = []
for word in user_input2:
    clean_word = "".join(char for char in word if char.isalnum())
    list_of_strings2.append(clean_word)

result2 = filter_and_map2(list_of_strings2)
print(result2)




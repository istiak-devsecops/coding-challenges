# Task 5: Write a function that takes a list of strings and returns a dictionary.
# The dictionary should map each string to its length, but only include strings longer than 5 characters.

from collections import Counter
import re

#with list comprehention
def filter_and_map2(strings2):
    return dict(Counter(word for word in strings2 if len(word) > 5))

user_input2 = input("Write down something! ").strip().split()    # remove whitespace and split input seprated by whitespace

list_of_clean_input = []
pattern = r'[^\w\s]'
for word in user_input2:
    clean_input = re.sub(pattern,"", word)
    list_of_clean_input.append(clean_input)

result2 = filter_and_map2(list_of_clean_input)
print(result2)


#Reverse every word

input_str = "DevSecOps mastery through practice"
input_str = input_str.split()

#Empty list to store the reverse word
word_list = [] 

for word in input_str:
    reverse_word  = word[::-1]
    word_list.append(reverse_word)

#join the reverse word to a line
word_list = " ".join(word_list)

print(word_list)


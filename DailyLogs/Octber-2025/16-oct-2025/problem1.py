
sentence = "whole wordl is going to see you. So don't be hollow inside!"

# remove all the o from the string and replace it with x

new_sentence = []
for word in sentence.split():
    table = str.maketrans("o","x") # mapping the replacable char
    new_sentence.append(word.lower().translate(table))

print(" ".join(new_sentence))


# remove all the w and h from the sentence and chance it with 0

new_sentence2 = []
for word in sentence.split():
    table = str.maketrans({"w":"0", "h":"0"}) # map with word with dict
    new_sentence2.append(word.lower().translate(table))

print(",".join(new_sentence2))


#remove all the i and e from the string

new_sentence3 = []
for word in sentence.split():
    table = str.maketrans("","","ie") # map with word with dict
    new_sentence3.append(word.lower().translate(table))

print(",".join(new_sentence3))

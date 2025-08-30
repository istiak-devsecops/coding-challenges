#Trim the n number of word from back and front

def trim_string(text, n):
    return text[n : len(text) - 2]

print(trim_string("Marketing", 2))

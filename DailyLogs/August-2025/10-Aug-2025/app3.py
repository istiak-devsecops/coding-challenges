import string

userInp = input("Write down a sentence: ").lower()

cleantxt = []


for word in userInp:
    new_word = ""
    for char in word:
        if char not in string.punctuation:
            new_word += char
    
    if new_word:
        cleantxt.append(new_word)

charcounter={}

for ch in cleantxt:
    if ch in charcounter:
        charcounter[ch] += 1
    else:
        charcounter[ch]=1

for ch in sorted(charcounter.keys()):
    print(f"{ch}: {charcounter[ch]}")


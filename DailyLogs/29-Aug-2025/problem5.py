sentence = " DevOps requires PRACTICE, Practice, practice. "
clean_sentences = sentence.strip().lower().replace(",","").replace(".","").split()

vowel = "aeiou"
wordlist = []
practice_counter = 0

for word in clean_sentences:
    if word == "practice":  
        practice_counter += 1 #if the word practice it will count it

        #replace the char if its a vowel with *
        custom_word = ""
        for chr in word:
            if chr in vowel:
                custom_word += "*"
            else:
                custom_word += chr
        wordlist.append(custom_word) #append the char if there is any modification
    else:
        wordlist.append(word) #append original word if there are no modification

print(f"All the modified word after replacing vowels: "," ".join(wordlist))
print(f"Total number of practice word: {practice_counter}")
        


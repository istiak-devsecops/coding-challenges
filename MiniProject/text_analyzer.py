# Text analyzer
user_input = input("write few words here: ")
words = []

# Remove punctuation from the sentence for accurate counts
import string
for word in user_input.lower().split():
    clean_word = ""
    for char in word:
        if char not in string.punctuation:
            clean_word += char
    words.append(clean_word)

clean_sentence = " ".join(clean_text)

# Selection menu for user
while True:
    print("Select which operations you wants to perform!")
    print("1. Count characters, words, sentences")
    print("2. Word frequency")
    print("3. Longest/shortest word")
    print("4. Top 5 common words")
    print("5. Vowel & consonant count")
    print("6. Exit")

    choice = input("Select an option from the list by their number.")

    import re
    if choice == "1":
        char_count = 0

        #count total character
        for chr in clean_sentence:
            if chr != " ":
                char_count += 1 
        print(f"Total character count is: {char_count}")

        #count total word
        word_count = len(words)
        print(f"Total word count is: {word_count}")

        #Count sentence
        search_pattern = r'[.?!](?=\s|$)'    
        matches = re.findall(search_pattern,user_input)
        print(f"Total number of sentences is: {len(matches)}")    



    break
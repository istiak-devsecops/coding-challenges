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

clean_sentence = " ".join(words)

# Selection menu for user
while True:
    print("Select which operations you wants to perform!: ")
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
        sentences = re.split(r'[.?!]', user_input)
        sentences = [s.strip() for s in sentences if s.strip()]
        print(f"Total number of sentences is: {len(sentences)}")   

    elif choice == "2":
        word_frequency = {}

        #word frequency counter
        for word in words:
            if word in word_frequency:
                word_frequency[word] += 1
            else:
                word_frequency[word] = 1
        #better formatting
        for word, count in word_frequency.items():
            print(f"{word}: {count}")
    
    elif choice == "3":

        longest_word = []
        shortest_word = []
        max_len = 0
        min_len = float("inf")

        for word in words:
            word_len = len(word)
        
            #Longest word
            if word_len > max_len:
                max_len = word_len
                longest_word = [word]
            elif word_len == max_len:
                longest_word.append(word)

            #short word
            if word_len < min_len:
                min_len = word_len
                shortest_word = [word]
            elif word_len == min_len:
                shortest_word.append(word)
        
        print(f"The longest words are: {longest_word} and the shortest words are: {shortest_word}")
            
    elif choice == "4":

        # Top 5 common word
        from collections import Counter
        word_freq = Counter(words)
        top_5_common_word = word_freq.most_common(5)

        print(f"Top 5 common words are: {top_5_common_word}")

    elif choice == "5":

        vowels = "aeiou"
        vowel_counter = 0
        consonant_counter = 0

        #vowels and consonent count
        for word in words:
            for char in word:
                if char in vowels:
                    vowel_counter += 1
                else:
                    consonant_counter += 1
        print(f"Total vowels in the sentences are: {vowel_counter} \nToal consonant in the sentences are {consonant_counter}")

    #break the loop 
    elif choice == "6":
        print(f"Thank you for using the service!")
        break

    else:
        print("Your choice is invalid. Try again...")
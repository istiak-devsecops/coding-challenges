def longest_word(text):
    words = text.split()
    longest = max(words, key=len)
    return longest

sentence = "Python is amazing"
print("Longest word:", longest_word(sentence))
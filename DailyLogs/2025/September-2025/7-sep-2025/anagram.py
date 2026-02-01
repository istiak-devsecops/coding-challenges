# anagram checker


def anagram_checker(word1, word2):

    if len(word1) != len(word2):
        return False
    
    freq1 = {}
    freq2 = {}

    for char in word1:
        freq1[char] = freq1.get(char, 0) + 1

    for char in word2:
        freq2[char] = freq2.get(char, 0) + 1

    if freq1 == freq2:
        return "Anagram"
    else:
        return "Not anagram"


text1 = input("write 1st word: ")
text2 = input("write 2nd word: ")

print(f"{text1},{text2} are {anagram_checker(text1,text2)}")


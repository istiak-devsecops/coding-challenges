# Write a function that takes a string and returns a dictionary with each word and how many times it appears.

def word_counter():
    note_book = {}
    while True:
        U_input = input("write a word('exit' to stop): ")
        if U_input.lower().strip() == "exit":
            break
        
        words = U_input.strip().split()
        for word in words:
            word = word.lower()
            note_book[word] = note_book.get(word, 0) + 1

    return note_book

word_freq = word_counter()
print(word_freq)




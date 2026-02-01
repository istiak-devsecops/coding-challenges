# Task 7: Write a function that reads a text file and returns the number of lines,
# words, and characters in the file. Handle the case where the file doesn't exist.

from collections import Counter

def file_summary(filename):
    try:
        with open(filename, "r") as file:
            line = file.readlines()
            total_lines = len(line)
            total_words = sum(len(word.split()) for word in line)
            total_char = sum(len(char) for word in line for char in word if not char.isspace())

        return {"lines": total_lines,
                "words": total_words,
                "character": total_char}
    
    except FileNotFoundError:
        return "ERROR: file missing"
    
my_file = "notes.txt"

print(file_summary(my_file))


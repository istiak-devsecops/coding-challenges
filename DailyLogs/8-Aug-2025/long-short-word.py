# Longest & Shortest Word Finder

import string

user_input = input("Write a sentence here: ").split()  # split the string

word_list = []

for word in user_input:
    clean_word = word.strip().lower().strip(string.punctuation)  # remove punctuation
    if clean_word:
        word_list.append(clean_word)  # added word to the list

Longest_word = max(word_list, key=len)
shortest_word = min(word_list, key=len)


def main():
    print(f"The longest word is: {Longest_word} = {len(Longest_word)}")
    print(f"The shortest word is: {shortest_word} = {len(shortest_word)}")


if __name__ == "__main__":
    main()

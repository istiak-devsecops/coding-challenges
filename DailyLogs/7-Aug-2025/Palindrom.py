# Check for Palindrome words in a sentence

# input is a sentence > Remove the punction > split the sentence
# and store it in a list > with for loop check if its a palindrom >
# show the total number of palindrom word and the list of palindromo word


user_input = input("Write a sentence here: ").lower()  # lowercase the words

text_list = user_input.replace(".", "").split()  # replace (.) and split into list

palindrom_count = 0
palindrom_words = []

for word in text_list:
    if word == word[::-1]:  # check if the word is a palindor
        palindrom_count += 1
        palindrom_words.append(word)


def main():
    print(f"Total numnber of palindrom word: {palindrom_count}")
    print(f"All the palindrom word: {palindrom_words}")


if __name__ == "__main__":
    main()

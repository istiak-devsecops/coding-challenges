# Check if a string is a palindrome.

text = "madam"

def palindrom_checker(text):
    clean_word = "".join(char.lower() for char in text if char.isalnum())
    if clean_word == clean_word[::-1]:
        return "is palindrom"
    else:
        return "isn't palindrom"

print(palindrom_checker(text))


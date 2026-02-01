# Text Reverser → User enters text → program prints the reversed text + number of characters.

user_input = input("Write few lines!: ")

def reverse_text_preserve_all(text):
    reversed_text = text[::-1]
    total_characters = sum(1 for char in text if char != " ")
    return reversed_text, total_characters

reversed_text, total_characters = reverse_text_preserve_all(user_input)
print("Reversed text:", reversed_text)
print("Total characters:", total_characters)



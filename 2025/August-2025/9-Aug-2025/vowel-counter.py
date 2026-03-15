import string

user_input = input("Write down a sentence in here: ").lower()

clean_input = user_input

vowel = "aeiou"

vowel_count = 0
consonent_count = 0

for char in clean_input:
    if char.isalpha():
        if char in vowel:
            vowel_count += 1
        else:
            consonent_count += 1


print(f"Vowels; {vowel_count}, \nconsonenet; {consonent_count}")

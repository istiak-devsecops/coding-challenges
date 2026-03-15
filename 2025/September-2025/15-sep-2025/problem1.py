# Reverse a string without using slicing ([::-1]).

def reverse_text(text):
    reverse = ""
    for char in text:
        reverse = char + reverse
    return reverse

text = "market"
print(reverse_text(text))
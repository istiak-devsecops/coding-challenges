# Build a Caesar cipher (shift each letter by 2).

def caesar_cipher_translate(text, shift=2):
    import string

    # Create original and shifted alphabets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase

    shifted_lower = lowercase[shift:] + lowercase[:shift]
    shifted_upper = uppercase[shift:] + uppercase[:shift]

    # Build translation table
    translation_table = str.maketrans(lowercase + uppercase, shifted_lower + shifted_upper)

    # Apply translation
    return text.translate(translation_table)

# Example usage
user_input = input("Enter text to encrypt: ")
encrypted = caesar_cipher_translate(user_input)
print("Encrypted text:", encrypted)

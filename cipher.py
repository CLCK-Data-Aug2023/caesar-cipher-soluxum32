# add your code here
def caesar_cipher(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            # Determine if the character is uppercase or lowercase
            if char.isupper():
                # Encrypt uppercase letters
                encrypted_char = chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))
            else:
                # Encrypt lowercase letters
                encrypted_char = chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
        else:
            # Keep special characters as they are
            encrypted_char = char
        encrypted_text += encrypted_char
    return encrypted_text

plain_text = input("Please enter a sentence: ")
shift = 5
encrypted_text = caesar_cipher(plain_text, shift)

print("The encrypted sentence is:", encrypted_text)

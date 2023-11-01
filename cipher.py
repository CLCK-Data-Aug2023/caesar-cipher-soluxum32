# add your code here
def caesar_cipher(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            is_upper = char.isupper()
            char_offset = ord('A' if is_upper else 'a')
            encrypted_char = chr((ord(char) - char_offset + shift) % 26 + char_offset)
        else:
            encrypted_char = char
            encrypted_text += encrypted_char
    return encrypted_text

plain_text = input("Please enter a sentence: ")
shift = 5
encrypted_text = caesar_cipher(plain_text, shift)

print("The encrypted sentence is:", encrypted_text)

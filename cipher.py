# add your code here
def caesar_cipher(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            is_upper = char.isupper()
            char_offset = ord('A' if is_upper else 'a')
            encrypted_char = chr(((ord(char) - char_offset + shift) % 26) + char_offset)
            encrypted_text += encrypted_char if is_upper else encrypted_char.lower()
        else:
            encrypted_text += char
    return encrypted_text

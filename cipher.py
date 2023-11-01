# add your code here

def caesar_cipher(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            is_upper = char.isupper()
            shift_amount = shift % 26
            char = char.lower()
            encrypted_char = chr(((ord(char) - ord('a') + shift_amount) % 26) + ord('a'))
            if is_upper:
                encrypted_char = encrypted_char.upper()
        else:
            encrypted_char = char
        encrypted_text += encrypted_char
    return encrypted_text

plain_text = input("Please enter a sentence: ")
encrypted_text = caesar_cipher(plain_text, 5)
print("The encrypted sentence is:", encrypted_text)



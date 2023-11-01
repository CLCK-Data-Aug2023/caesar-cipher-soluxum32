# add your code here

def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            if char.islower():
                result += chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
            else:
                result += chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))
        else:
            result += char
    return result

text = "A sentence with Capital letters."
shift = 5  # You can change the shift value according to your needs

ciphered_text = caesar_cipher(text, shift)
print("Ciphered text:", ciphered_text)


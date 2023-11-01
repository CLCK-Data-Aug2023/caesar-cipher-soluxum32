# add your code here

def caesar_decrypt(encrypted_text, shift):
    decrypted_text = ""
    for char in encrypted_text:
        if char.isalpha():
            is_upper = char.isupper()
            char_offset = ord('A' if is_upper else 'a')
            char = char.lower()  # Convert the character to lowercase for comparison
            decrypted_char = chr(((ord(char) - char_offset - shift) % 26) + char_offset)
            if is_upper:
                decrypted_text += decrypted_char.upper()
            else:
                decrypted_text += decrypted_char
        else:
            decrypted_text += char
    return decrypted_text

encrypted_sentence = 'f xjsyjshj bnym hfunyfq qjyyjwx.'
shift = 5
decrypted_sentence = caesar_decrypt(encrypted_sentence, shift)

print("The decrypted sentence is:", decrypted_sentence)




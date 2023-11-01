# add your code here
def caesar_cipher_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            is_upper = char.isupper()
            char = char.lower()
            encrypted_char = chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
            if is_upper:
                encrypted_char = encrypted_char.upper()
        else:
            encrypted_char = char
        encrypted_text += encrypted_char
    return encrypted_text

def main():
    sentence = input("Please enter a sentence: ")
    encrypted_sentence = caesar_cipher_encrypt(sentence, 5)
    print("The encrypted sentence is:", encrypted_sentence)

if __name__ == "__main__":
    main()

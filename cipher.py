# add your code here
def caesar_cipher_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            # Determine whether the character is uppercase or lowercase
            if char.isupper():
                char_offset = ord('A')
            else:
                char_offset = ord('a')
            # Apply the Caesar cipher shift
            shifted_char = chr((ord(char) - char_offset + shift) % 26 + char_offset)
            encrypted_text += shifted_char
        else:
            # Keep special characters unchanged
            encrypted_text += char
    return encrypted_text

def main():
    plain_text = input("Please enter a sentence: ")
    shift = 5
    encrypted_text = caesar_cipher_encrypt(plain_text, shift)
    print("The encrypted sentence is:", encrypted_text)

if __name__ == "__main":
    main()

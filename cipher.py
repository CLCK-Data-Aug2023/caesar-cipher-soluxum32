# add your code here
def caesar_cipher(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():  # Check if the character is an alphabet letter
            is_upper = char.isupper()  # Check if the character is uppercase
            char = char.lower()  # Convert to lowercase for easy shifting
            shifted = chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
            if is_upper:
                shifted = shifted.upper()  # Restore the case if it was uppercase
            encrypted_text += shifted
        else:
            encrypted_text += char  # Special characters remain unchanged
    return encrypted_text

def main():
    plain_text = input("Enter a sentence to encrypt: ")
    shift = 5  # Right shift by 5 positions

    encrypted_text = caesar_cipher(plain_text, shift)
    print("Encrypted text: " + encrypted_text)

if __name__ == "__main":
    main()

# add your code here
import string

def caesar(text, shift, alphabets):
    def shift_alphabet(alphabet):
        return alphabet[shift:] + alphabet[:shift]

shifted_alphabets = tuple(map(shift_alphabet, alphabets))
final_alphabet = ' '.join(alphabets)
final_shifted_alphabet = ''.join(shifted_alphabets)
table = srt.maketrans(final_alphabet, final_shifted_alphabet)
return text.translate(table)

plain_text = "Crazy!"
print(caesar(plain_text, 5, [string.ascii_lowercase, string.ascii_uppercase, string.punctuation]))

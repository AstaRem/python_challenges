# Encrypt/Decrypt

# Write two functions: encrypt(text,key) and decrypt(text,key).

# To encrypt a message, add the key to each character. For example, with a key of 1, A becomes B and e becomes f. With a key of 4, A becomes E, etc.

"""
This code is only for checking purpose

letter = "u"
number_value = ord(letter)
print(f"Letter {letter} converts to number {number_value}")
letter_value = chr(number_value)
print(f"Number {number_value} converts to letter {letter_value}")
"""

def encrypt(letter, key):
    new_number = ord(letter) + key
    new_letter = chr(new_number)
    print(f"Encrypted letter is {new_letter}")

encrypt("u", 2)

def decrypt(letter, key):
    original_number = ord(letter) - key
    original_letter = chr(original_number)
    print(f"Decrypted letter is {original_letter}")

decrypt("w", 2)
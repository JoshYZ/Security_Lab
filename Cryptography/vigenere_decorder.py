"""
Vigenère Cipher Decoder
Author: JoshYZ
Purpose: Decrypts polyalphabetic ciphers using a provided keyword.
"""

def vigenere_decrypt(ciphertext, key):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    result = ""
    key_index = 0
    
    for char in ciphertext.lower():
        if char in alphabet:
            shift = alphabet.find(key[key_index % len(key)].lower())
            index = alphabet.find(char)
            new_index = (index - shift) % 26
            result += alphabet[new_index]
            key_index += 1
        else:
            result += char
    return result

if __name__ == "__main__":
    # Example: Key 'WUKONG'
    print(vigenere_decrypt("Lyp fbu g mnvb!", "WUKONG"))
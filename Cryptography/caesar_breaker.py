"""
Caesar Cipher Brute-Forcer
Author: JoshYZ
Purpose: Analyzes ciphertext by testing all 26 possible alphabetical shifts.
"""

def caesar_brute_force(ciphertext):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    print(f"--- Analyzing Ciphertext: {ciphertext} ---")
    
    for shift in range(26):
        result = ""
        for char in ciphertext.lower():
            if char in alphabet:
                index = alphabet.find(char)
                new_index = (index - shift) % 26
                result += alphabet[new_index]
            else:
                result += char
        print(f"Shift {shift:2}: {result}")

if __name__ == "__main__":
    # Test with the cipher
    caesar_brute_force("Xv dshuwx vxp xqup dshuwxp.")
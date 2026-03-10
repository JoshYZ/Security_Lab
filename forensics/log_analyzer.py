"""
Hex-Encoded Log Analyzer
Author: JoshYZ
Purpose: Decodes hex-formatted data captured from system logs.
"""

def decode_log_payload(hex_list):
    """Translates a list of hex strings into ASCII characters."""
    decoded_string = ""
    for hex_val in hex_list:
        try:
            # Convert hex to int, then int to character
            decoded_string += chr(int(hex_val, 16))
        except ValueError:
            continue
    return decoded_string

if __name__ == "__main__":
    # Sample evidence found in 'breach_attempt.log'
    evidence = ["42", "61", "6E", "64", "69", "74"]
    print(f"Decoded Evidence: {decode_log_payload(evidence)}")
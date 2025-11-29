"""
Caesar Cipher Algorithm

Caesar Cipher is a simple substitution cipher where each letter in the plaintext
is shifted a certain number of places down the alphabet. It's one of the earliest
known encryption techniques.

Time Complexity: O(n) where n is length of text
Space Complexity: O(n)

Note: This is not secure for modern applications but is useful for learning
cryptography basics. Rot13 is a special case where shift = 13.
"""


def caesar_cipher_encrypt(text, shift):
    """
    Encrypts text using Caesar cipher.
    
    Args:
        text: Plaintext to encrypt
        shift: Number of positions to shift (can be negative)
    
    Returns:
        Encrypted ciphertext
    """
    result = []
    
    for char in text:
        if char.isalpha():
            # Determine base (A or a)
            base = ord('A') if char.isupper() else ord('a')
            # Shift and wrap around alphabet
            shifted = (ord(char) - base + shift) % 26
            result.append(chr(base + shifted))
        else:
            # Keep non-alphabetic characters unchanged
            result.append(char)
    
    return ''.join(result)


def caesar_cipher_decrypt(ciphertext, shift):
    """
    Decrypts text encrypted with Caesar cipher.
    
    Args:
        ciphertext: Encrypted text
        shift: Shift used for encryption
    
    Returns:
        Decrypted plaintext
    """
    # Decryption is encryption with negative shift
    return caesar_cipher_encrypt(ciphertext, -shift)


def rot13(text):
    """
    Rot13 is a special case of Caesar cipher with shift = 13.
    It's its own inverse (encrypting twice returns original text).
    
    Args:
        text: Text to encode/decode
    
    Returns:
        Rot13 encoded/decoded text
    """
    return caesar_cipher_encrypt(text, 13)


# Example usage
if __name__ == "__main__":
    # Caesar Cipher example
    plaintext = "Hello, World!"
    shift = 3
    
    print(f"Caesar Cipher (shift={shift}):")
    print(f"  Plaintext: {plaintext}")
    
    encrypted = caesar_cipher_encrypt(plaintext, shift)
    print(f"  Encrypted: {encrypted}")
    
    decrypted = caesar_cipher_decrypt(encrypted, shift)
    print(f"  Decrypted: {decrypted}")
    
    # Rot13 example
    print(f"\nRot13:")
    print(f"  Original: {plaintext}")
    encoded = rot13(plaintext)
    print(f"  Encoded: {encoded}")
    decoded = rot13(encoded)
    print(f"  Decoded: {decoded}")


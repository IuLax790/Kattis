def decrypt_vigenere(encrypted_message, key):
    """
    Decrypts a message encrypted using Yraglac's modified Vigenère cipher.

    Args:
      encrypted_message: The encrypted message.
      key: The key used for encryption.

    Returns:
      The decrypted message.
    """
    decrypted_message = ""
    for i, (char, key_char) in enumerate(zip(encrypted_message, key)):
        shift = ord(key_char) - ord('A') 
        if i % 2 == 0:  # Even index
            decrypted_char = chr(((ord(char) - ord('A') - shift) % 26) + ord('A'))
        else:  # Odd index
            decrypted_char = chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))
        decrypted_message += decrypted_char
    return decrypted_message

if __name__ == "__main__":
    encrypted_message = input()
    key = input()
    decrypted_message = decrypt_vigenere(encrypted_message, key)
    print(decrypted_message)

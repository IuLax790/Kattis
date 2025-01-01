def encode_message(message, multiplier):
  """
  Encodes a message using the MKIA cipher.

  Args:
    message: The message to be encoded.
    multiplier: The secret number string.

  Returns:
    The encoded message.
  """
  encoded_message = ""
  for i in range(len(message)):
    char_num = ord(message[i]) - ord('A')  # Get character's numerical value
    multiplier_digit = int(multiplier[i])
    encrypted_num = (char_num * multiplier_digit) % 26  # Apply modulo 26
    encrypted_char = chr(encrypted_num + ord('A'))
    encoded_message += encrypted_char
  return encoded_message

if __name__ == "__main__":
  multiplier = input()
  n = int(input())
  for _ in range(n):
    message = input()
    encoded_message = encode_message(message, multiplier)
    print(encoded_message)

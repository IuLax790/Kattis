import math

def decode_message(encoded_message):
    n = int(math.sqrt(len(encoded_message)))  # Determine the side length of the square
    matrix = []

    # Create a matrix from the encoded message
    for i in range(0, n * n, n):
        matrix.append(list(encoded_message[i:i+n]))

    # Rotate the matrix 90 degrees clockwise
    rotated_matrix = list(zip(*matrix))[::-1]  # Corrected rotation

    # Extract the decoded message
    decoded_message = ''.join(''.join(row) for row in rotated_matrix)
    return decoded_message

if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        encoded_message = input()
        decoded_message = decode_message(encoded_message)
        print(decoded_message)

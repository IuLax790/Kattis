# 1. Read the inputs
# We read N, though in Python we don't strictly need it for string processing
n = int(input())
gibberish = input()

# 2. Define the two keyboard layouts as strings
# We concatenate the rows: 10 keys + 9 keys + 7 keys = 26 keys
# ABC layout (What was typed/Input)
abc_layout = "abcdefghijklmnopqrstuvwxyz"

# QWERTY layout (What was intended/Output)
qwerty_layout = "qwertyuiopasdfghjklzxcvbnm"

# 3. Decode the message
decoded_message = ""

for char in gibberish:
    if char == ' ':
        decoded_message += ' '
    else:
        # Find where the character exists on the ABC board
        index = abc_layout.find(char)
        
        # Grab the character from the same spot on the QWERTY board
        decoded_message += qwerty_layout[index]

# 4. Print the result
print(decoded_message)

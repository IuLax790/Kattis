# Input reading
n = int(input().strip())  # Number of bites
words = input().strip().split()  # Words spoken by Arild

# Verify if the counting makes sense
makes_sense = True
for i in range(1, n + 1):
    if words[i - 1] != "mumble":
        if int(words[i - 1]) != i:
            makes_sense = False
            break

# Output the result
if makes_sense:
    print("makes sense")
else:
    print("something is fishy")

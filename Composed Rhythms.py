# Function to decompose the rhythm into groups of 2 and 3
def decompose_rhythm(n):
    groups = []

    # Use as many groups of 3 as possible, leaving remainder as groups of 2
    while n > 0:
        if n % 2 == 0:
            groups.append(2)
            n -= 2
        else:
            groups.append(3)
            n -= 3

    return groups

# Decompose the rhythm
result = decompose_rhythm(n)

# Output the number of groups and the groups themselves
print(len(result))
print(" ".join(map(str, result)))

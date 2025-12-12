# 1. Read the number of letters (we don't strictly need this in Python loop, but we must read it to clear the buffer)
n = int(input())

# 2. Read the strings
previous = input()
current = input()

total_moves = 0

# 3. Loop through the strings simultaneously using range
for i in range(n):
    # Get the ASCII value of the characters at position i
    # We subtract ord('A') to treat 'A' as 0, 'B' as 1, etc.
    val_prev = ord(previous[i]) - ord('A')
    val_curr = ord(current[i]) - ord('A')
    
    # Calculate the raw distance between them
    diff = abs(val_prev - val_curr)
    
    # Calculate the shortest path (Direct vs Wrap-around)
    # Wrap around is always (26 - diff)
    shortest_path = min(diff, 26 - diff)
    
    total_moves += shortest_path

print(total_moves)

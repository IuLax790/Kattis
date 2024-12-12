# Input reading
n = int(input().strip())  # Number of people in the group

# Initialize minimum and maximum possible temperature range
min_pref = 0  # Lowest possible temperature
max_pref = 2 * 10**5  # Highest possible temperature

# Process each person's preference range
for _ in range(n):
    a, b = map(int, input().strip().split())
    min_pref = max(min_pref, a)  # Update the minimum to the highest low preference
    max_pref = min(max_pref, b)  # Update the maximum to the lowest high preference

# Determine the result
if min_pref <= max_pref:
    num_options = max_pref - min_pref + 1
    print(num_options, min_pref)
else:
    print("bad news")

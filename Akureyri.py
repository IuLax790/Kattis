# Input reading and processing
n = int(input())  # Number of contestants

# Dictionary to store location counts
location_counts = {}

# Iterate through the input to process name and location pairs
for _ in range(n):
    name = input().strip()  # Read contestant's name (but we don't use it)
    location = input().strip()  # Read contestant's location

    # Increment the count for this location in the dictionary
    if location in location_counts:
        location_counts[location] += 1
    else:
        location_counts[location] = 1

# Output the results
for location, count in location_counts.items():
    print(location, count)

# Input: Number of green herbs and red herbs
green, red = map(int, input().split())

# Calculate maximum health boost
health_boost = 0

# Step 1: Use green + red recipe (1 green, 1 red -> 10 boost)
mix_count = min(green, red)
health_boost += mix_count * 10
green -= mix_count
red -= mix_count

# Step 2: Use 3 green recipe (3 green -> 10 boost)
while green >= 3:
    health_boost += 10
    green -= 3

# Step 3: Use 2 green recipe (2 green -> 3 boost)
if green >= 2:
    health_boost += 3
    green -= 2

# Step 4: Use 1 green recipe (1 green -> 1 boost)
if green == 1:
    health_boost += 1

# Output the result
print(health_boost)

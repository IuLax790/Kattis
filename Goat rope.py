import math

def minimum_distance_to_house(x, y, x1, y1, x2, y2):
    # Clamp the fence post's coordinates to the rectangle's boundaries
    closest_x = min(max(x, x1), x2)
    closest_y = min(max(y, y1), y2)
    
    # Calculate the distance to the closest point
    distance = math.sqrt((x - closest_x) ** 2 + (y - closest_y) ** 2)
    return distance

# Input parsing
x, y, x1, y1, x2, y2 = map(int, input().split())

# Compute the result
result = minimum_distance_to_house(x, y, x1, y1, x2, y2)

# Output the result with precision up to 3 decimal places
print(f"{result:.3f}")

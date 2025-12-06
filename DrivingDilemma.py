# 1. Get the input
mph = int(input())          # Speed limit in Miles Per Hour
distance_needed = float(input())   # Distance to intersection in Feet
time_available = float(input())    # Time until red light in Seconds

# 2. Convert Speed to Feet Per Second (fps)
# We multiply by 5280 (feet in a mile) and divide by 3600 (seconds in an hour)
speed_fps = mph * (5280 / 3600)

# 3. Calculate how far Rishi can travel in the available time
# Distance = Speed * Time
distance_possible = speed_fps * time_available

# 4. Compare the distances
# If the distance he can travel is greater than or equal to the distance needed
if distance_possible >= distance_needed:
    print("MADE IT")
else:
    print("FAILED TEST")

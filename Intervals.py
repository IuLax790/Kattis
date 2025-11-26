# 1. Read N (users) and K (threshold)
n, k = map(int, input().split())

# 2. Create a list of 24 zeros to represent the hours of the day
# Index 0 represents 00:00-01:00, Index 23 represents 23:00-24:00
hours_activity = [0] * 24

# 3. Process each user
for _ in range(n):
    start, end = map(int, input().split())
    
    # Loop through the specific hours this user was active
    # range(start, end) includes start but stops before end
    for hour in range(start, end):
        hours_activity[hour] += 1

# 4. Count how many hours met the threshold
qualifying_hours = 0

for count in hours_activity:
    if count >= k:
        qualifying_hours += 1

print(qualifying_hours)

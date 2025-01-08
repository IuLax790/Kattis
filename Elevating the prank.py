# Input Reading
A, B = map(int, input().split())  # Starting floor and destination floor
N = int(input())  # Number of additional floors the elevator will stop at
pressed_floors = [int(input()) for _ in range(N)]

# Calculate the travel time
travel_time = abs(A - B) * 4

# Calculate stop time
if A <= B:
    valid_stops = [floor for floor in pressed_floors if A < floor < B]
else:
    valid_stops = [floor for floor in pressed_floors if B < floor < A]

stop_time = len(valid_stops) * 10

# Total time spent in the elevator
total_time = travel_time + stop_time

print(total_time)

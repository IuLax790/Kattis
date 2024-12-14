# Input reading
n, r, c = map(int, input().strip().split())
seating = [input().strip().split() for _ in range(r)]
attendance = [input().strip() for _ in range(n)]

# Track the current index in the attendance list
attendance_index = 0
results = []

# For each row, determine the passing direction
for row in seating:
    # Extract the names for the current row from the attendance list
    attendance_row = attendance[attendance_index:attendance_index + c]
    attendance_index += c

    # Compare attendance order with seating row order
    if attendance_row == row:
        results.append("left")
    elif attendance_row == row[::-1]:
        results.append("right")
    else:
        # This should never occur given valid input
        raise ValueError("Invalid attendance list order.")

# Output results
print("\n".join(results))

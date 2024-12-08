# Input reading
n = int(input().strip())  # Number of callouts

callouts = []
for _ in range(n):
    callouts.append(input().strip())

# Initialize variables
absent_students = []
previous_call = None

# Process the callouts
for call in callouts:
    if call == "Present!":
        previous_call = None  # Reset the previous call as the student responded
    else:
        if previous_call:  # If the previous call did not have "Present!", it means absent
            absent_students.append(previous_call)
        previous_call = call  # Update the previous call to the current student name

# If the last student called did not respond, they are absent
if previous_call:
    absent_students.append(previous_call)

# Output results
if absent_students:
    print("\n".join(absent_students))
else:
    print("No Absences")

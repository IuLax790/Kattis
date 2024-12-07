# Input reading
total_seconds = int(input().strip())  # Duration in seconds

# Initialize hours, minutes, and seconds
hours = 0
minutes = 0
seconds = 0

# Calculating hours, minutes, and seconds if total_seconds is larger than respective thresholds
if total_seconds >= 3600:
    hours = total_seconds // 3600  # Calculate the number of hours
    total_seconds %= 3600  # Update remaining seconds

if total_seconds >= 60:
    minutes = total_seconds // 60  # Calculate the number of minutes
    total_seconds %= 60  # Update remaining seconds

seconds = total_seconds  # Remaining seconds

# Output the result in the desired format
print(f"{hours} : {minutes} : {seconds}")

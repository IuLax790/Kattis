import sys

def solve():
    # Read all standard input at once and split by whitespace.
    # This handles cases where inputs are on newlines or spaces.
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    # Parse the integers from the input list
    # Scenario 1:
    w1 = int(input_data[0]) # Number of workers
    t1 = int(input_data[1]) # Time taken
    v1 = int(input_data[2]) # Volume dug

    # Scenario 2:
    w2 = int(input_data[3]) # New number of workers
    v2 = int(input_data[4]) # New target volume

    # Step 1: Calculate the rate of a SINGLE worker per hour
    # Total Man-Hours used in Scenario 1 = w1 * t1
    # Rate = Volume / Total Man-Hours
    single_worker_rate = v1 / (w1 * t1)

    # Step 2: Calculate the combined rate of the new team
    new_team_rate = single_worker_rate * w2

    # Step 3: Calculate the time required for the new team
    # Time = Target Volume / Rate
    time_needed = v2 / new_team_rate

    # Output the result
    print(time_needed)

if __name__ == "__main__":
    solve()

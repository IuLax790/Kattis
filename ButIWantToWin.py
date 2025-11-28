import sys

# Setting up input reading for cleaner execution
try:
    N = int(sys.stdin.readline())
    # Read the vote counts and convert to integers
    votes = [int(v) for v in sys.stdin.readline().split()]
except:
    # Handle empty input case gracefully if necessary for some environments
    exit()

# 1. Separate the Mayor and the Winner (Front-runner)
# Sort the list to easily identify the top two
votes.sort()

# Mayor is the 2nd highest, Winner is the highest.
# We pop them off the list, leaving only the candidates to be eliminated.
winner_score = votes.pop()
mayor_score = votes.pop()

rounds = 0
simulation_list = votes  # This list contains all other candidates' votes

# 2. Main Simulation Loop
while True:
    # A. Check for Victory Condition (Majority Win)
    # The current total pool of votes changes as candidates are eliminated.
    current_total = mayor_score + winner_score + sum(simulation_list)
    
    # RCV Rule 1: Win if score > 50% of current total
    if mayor_score > current_total / 2:
        break

    # B. Check for Final Two-Candidate Runoff Condition
    if len(simulation_list) == 0:
        # If only the Mayor and Winner are left, the one with more votes wins.
        if mayor_score > winner_score:
            break  # Mayor wins the runoff!
        else:
            # Mayor cannot beat the front-runner in the final round.
            rounds = "IMPOSSIBLE TO WIN"
            break

    # C. Elimination Round (If no winner and more than 2 candidates remain)
    
    # 1. Find the minimum vote count among the remaining candidates
    min_votes_to_remove = min(simulation_list)
    eliminated_votes_sum = 0
    
    # 2. Sum up ALL candidates tied for the minimum and remove them (RCV Rule)
    i = 0
    while i < len(simulation_list):
        if simulation_list[i] == min_votes_to_remove:
            # Pop the tied candidate's votes and add them to the elimination sum
            eliminated_votes_sum += simulation_list.pop(i)
            # Do NOT increment i because the list shifted, the next element is now at index i
        else:
            i += 1  # Move to the next index
            
    # 3. Transfer eliminated votes to the mayor (The problem's core assumption)
    mayor_score += eliminated_votes_sum
    rounds += 1


# 3. Output the Final Result
if rounds == "IMPOSSIBLE TO WIN":
    print("IMPOSSIBLE TO WIN")
else:
    print(rounds)

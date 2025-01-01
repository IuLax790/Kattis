def gerrymandering(p, d, precincts):
    from collections import defaultdict
    
    # Organize votes by district
    district_votes = defaultdict(lambda: {"A": 0, "B": 0})
    for di, ai, bi in precincts:
        district_votes[di]["A"] += ai
        district_votes[di]["B"] += bi

    total_votes = 0
    wasted_A = 0
    wasted_B = 0
    results = []

    for district_id in range(1, d + 1):
        votes_A = district_votes[district_id]["A"]
        votes_B = district_votes[district_id]["B"]
        total_votes_district = votes_A + votes_B
        total_votes += total_votes_district
        
        # Determine the winner and majority needed
        majority = total_votes_district // 2 + 1
        if votes_A > votes_B:
            winner = "A"
            wasted_votes_A = votes_A - majority
            wasted_votes_B = votes_B
        else:
            winner = "B"
            wasted_votes_A = votes_A
            wasted_votes_B = votes_B - majority
        
        wasted_A += wasted_votes_A
        wasted_B += wasted_votes_B
        results.append(f"{winner} {wasted_votes_A} {wasted_votes_B}")
    
    # Calculate the efficiency gap
    efficiency_gap = abs(wasted_A - wasted_B) / total_votes
    
    return results, efficiency_gap

# Input Reading
p, d = map(int, input().split())
precincts = [tuple(map(int, input().split())) for _ in range(p)]

# Compute Results
results, efficiency_gap = gerrymandering(p, d, precincts)

# Output Results
for result in results:
    print(result)
print(f"{efficiency_gap:.10f}")

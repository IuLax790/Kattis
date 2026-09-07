import sys

def solve():
    # Read all lines from standard input
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return
        
    # The first token is the number of workstations
    n = int(input_data[0])
    
    # The rest are the workstation coordinates
    workstations = input_data[1:n+1]
    
    total_distance = 0
    
    # Loop through each adjacent pair of workstations in the route
    for i in range(1, n):
        prev = workstations[i-1]
        curr = workstations[i]
        
        # Calculate row difference using ord() to get the ASCII value of the letter
        row_diff = abs(ord(curr[0]) - ord(prev[0]))
        
        # Calculate column difference using ord() 
        col_diff = abs(ord(curr[1]) - ord(prev[1]))
        
        # Add the Manhattan distance to the total
        total_distance += (row_diff + col_diff)
        
    # Print the final calculated total distance
    print(total_distance)

if __name__ == '__main__':
    solve()

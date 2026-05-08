import sys
from collections import deque

def solve():
    # Read width and height
    try:
        line1 = sys.stdin.readline().split()
        if not line1: return
        w, h = map(int, line1)
    except ValueError:
        return

    grid = [sys.stdin.readline().strip() for _ in range(h)]
    
    start_pos = None
    exits = []
    
    # Find the starting point and identify exit locations
    for r in range(h):
        for c in range(w):
            if grid[r][c] == '*':
                start_pos = (r, c)
            elif grid[r][c] == 'E':
                exits.append((r, c))

    if not start_pos:
        print("NOT POSSIBLE")
        return

    # Distance matrix initialized to infinity
    # dist[r][c] stores the minimum doors to reach that tile
    dist = [[float('inf')] * w for _ in range(h)]
    r_start, c_start = start_pos
    dist[r_start][c_start] = 0
    
    # Deque for 0-1 BFS
    queue = deque([(r_start, c_start)])
    
    min_doors_to_exit = float('inf')
    
    while queue:
        r, c = queue.popleft()
        
        # If we reached an exit, update the global minimum
        if grid[r][c] == 'E':
            min_doors_to_exit = min(min_doors_to_exit, dist[r][c])
            continue

        # Explore neighbors (Up, Down, Left, Right)
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr, nc = r + dr, c + dc
            
            # Check bounds and walls
            if 0 <= nr < h and 0 <= nc < w and grid[nr][nc] != '#':
                # Determine cost to enter this tile
                weight = 1 if grid[nr][nc] == 'D' else 0
                
                if dist[r][c] + weight < dist[nr][nc]:
                    dist[nr][nc] = dist[r][c] + weight
                    if weight == 0:
                        queue.appendleft((nr, nc)) # Priority processing
                    else:
                        queue.append((nr, nc)) # Standard processing

    if min_doors_to_exit == float('inf'):
        print("NOT POSSIBLE")
    else:
        print(min_doors_to_exit)

if __name__ == "__main__":
    solve()

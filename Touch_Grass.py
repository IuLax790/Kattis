import sys
from collections import deque

def solve():
    # Read height (H) and width (W)
    input_data = sys.stdin.read().splitlines()
    if not input_data:
        return
        
    h, w = map(int, input_data[0].split())
    grid = input_data[1:h+1]
    
    start_r, start_c = -1, -1
    
    # Find the starting position 'S'
    for r in range(h):
        for c in range(w):
            if grid[r][c] == 'S':
                start_r, start_c = r, c
                break
        if start_r != -1:
            break

    # BFS setup
    # Queue stores tuples of (row, col, current_steps)
    queue = deque([(start_r, start_c, 0)])
    visited = set([(start_r, start_c)])
    
    # Movement vectors for North, South, East, West
    directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    
    while queue:
        r, c, steps = queue.popleft()
        
        # If we reached the grass, we are done!
        if grid[r][c] == 'G':
            print(steps)
            return
            
        # Explore neighbors
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            
            # Check boundaries and if it's a valid, unvisited cell
            if 0 <= nr < h and 0 <= nc < w:
                if grid[nr][nc] != '#' and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    queue.append((nr, nc, steps + 1))
                    
    # If the queue is empty and we haven't touched grass
    print("thralatlega nettengdur")

if __name__ == '__main__':
    solve()

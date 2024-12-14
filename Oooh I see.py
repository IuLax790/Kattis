def find_treasure(grid):
    rows, cols = len(grid), len(grid[0])
    treasure_locations = []

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == '0':
                if (
                    (i > 0 and grid[i - 1][j] == 'O') and 
                    (i < rows - 1 and grid[i + 1][j] == 'O') and 
                    (j > 0 and grid[i][j - 1] == 'O') and 
                    (j < cols - 1 and grid[i][j + 1] == 'O') and 
                    (i > 0 and j > 0 and grid[i - 1][j - 1] == 'O') and 
                    (i > 0 and j < cols - 1 and grid[i - 1][j + 1] == 'O') and 
                    (i < rows - 1 and j > 0 and grid[i + 1][j - 1] == 'O') and 
                    (i < rows - 1 and j < cols - 1 and grid[i + 1][j + 1] == 'O')
                ):
                    treasure_locations.append((i + 1, j + 1))  # 1-based indexing

    if not treasure_locations:
        return "Oh no!"
    elif len(treasure_locations) > 1:
        return f"Oh no! {len(treasure_locations)} locations"
    else:
        return " ".join(map(str, treasure_locations[0]))

if __name__ == "__main__":
    rows, cols = map(int, input().split())
    grid = [list(input()) for _ in range(rows)]
    result = find_treasure(grid)
    print(result)

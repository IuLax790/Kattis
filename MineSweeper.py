# Input reading
n, m, k = map(int, input().strip().split())  # Rows, columns, number of mines

# Initialize the Minesweeper board
board = [['.' for _ in range(m)] for _ in range(n)]

# Read mine locations and update the board
for _ in range(k):
    y, x = map(int, input().strip().split())
    board[y - 1][x - 1] = '*'  # Place mine, adjusting for 0-based index

# Print the board
for row in board:
    print(''.join(row))

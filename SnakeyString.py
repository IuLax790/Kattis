import sys

def solve():
    # Read all standard input at once and split by whitespace.
    # This handles newlines, spaces, and trailing whitespace robustly.
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    iterator = iter(input_data)
    
    try:
        # Parse R (rows) and C (columns)
        R = int(next(iterator))
        C = int(next(iterator))
    except StopIteration:
        return

    # Prepare a list to hold the character for each column.
    # The problem guarantees the string has length C (one letter per column).
    result_chars = [''] * C
    
    # Iterate through each row of the grid
    for r in range(R):
        try:
            row_str = next(iterator)
        except StopIteration:
            break
            
        # Scan the row for characters
        for c, char in enumerate(row_str):
            # Safety check to ensure we don't exceed the expected column count
            if c < C:
                if char != '.':
                    result_chars[c] = char

    # Join the list to form the final string and print it
    print("".join(result_chars))

if __name__ == "__main__":
    solve()

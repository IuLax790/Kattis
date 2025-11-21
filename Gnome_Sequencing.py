import sys

def check_order(a, b, c):
    """
    Checks if three numbers (beard lengths) are strictly ordered.

    Ordering can be strictly ascending (a < b < c) or
    strictly descending (a > b > c).

    Args:
        a (int): The first beard length.
        b (int): The second beard length.
        c (int): The third beard length.

    Returns:
        bool: True if ordered, False otherwise.
    """
    # Check for strictly ascending order (shortest to longest)
    is_ascending = (a < b) and (b < c)
    
    # Check for strictly descending order (longest to shortest)
    is_descending = (a > b) and (b > c)
    
    # The group is ordered if it's either ascending or descending
    return is_ascending or is_descending

def main():
    """
    Reads the number of groups, processes the beard lengths for each group,
    and prints whether each group is 'Ordered' or 'Unordered'.
    """
    # Use sys.stdin.readlines() to read all input lines at once
    try:
        input_lines = sys.stdin.readlines()
    except EOFError:
        # Handle case where no input is provided
        return

    if not input_lines:
        return

    # The first line contains the number of groups (N)
    try:
        # Strip potential whitespace and get the number of groups
        num_groups = int(input_lines[0].strip())
    except ValueError:
        # If the first line is not a valid integer, stop
        return

    # Print the mandatory title line
    print("Gnomes:")

    # Process the subsequent N lines
    # Start loop from index 1 to skip the N count line
    for i in range(1, len(input_lines)):
        line = input_lines[i].strip()
        if not line:
            continue

        try:
            # Split the line into three parts and convert them to integers
            lengths = list(map(int, line.split()))
            
            # We expect exactly three distinct lengths
            if len(lengths) == 3:
                a, b, c = lengths[0], lengths[1], lengths[2]
                
                # Check the order
                if check_order(a, b, c):
                    print("Ordered")
                else:
                    print("Unordered")
            
            # Stop processing once we've handled the number of groups specified
            if i >= num_groups:
                break

        except ValueError:
            # Skip lines that do not contain valid numbers
            continue

if __name__ == "__main__":
    main()

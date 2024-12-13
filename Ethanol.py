# Input reading
c = int(input().strip())  # Number of carbon atoms

# Function to generate the alkanol structure
def generate_alkanol(c):
    if c == 0:
        return ["Invalid input: Number of carbon atoms must be at least 1."]

    lines = []

    # First hydrogen row
    first_row = "  " + " ".join(["H"] * c)
    lines.append(first_row)

    # Vertical connections
    vertical_row = "  " + " ".join(["|"] * c)
    lines.append(vertical_row)

    # Carbon chain with hydroxyl group at the end
    if c == 1:
        carbon_row = "H-C-OH"
    else:
        carbon_row = "H-" + "-".join(["C"] * (c - 1)) + "-C-OH"
    lines.append(carbon_row)

    # Vertical connections
    lines.append(vertical_row)

    # Last hydrogen row
    last_row = "  " + " ".join(["H"] * c)
    lines.append(last_row)

    return lines

# Generate and print the alkanol structure
alkanol_structure = generate_alkanol(c)
for line in alkanol_structure:
    print(line)

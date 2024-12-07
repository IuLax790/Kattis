# Input reading
import math

t = int(input().strip())  # Number of test cases

# Function to check if a number is a perfect square
def is_perfect_square(x):
    if x < 0:
        return False
    root = int(math.sqrt(x))
    return root * root == x

# Process each test case
results = []
for _ in range(t):
    n = int(input().strip())
    is_odd = (n % 2 != 0)
    is_square = is_perfect_square(n)

    if is_odd and is_square:
        results.append("OS")
    elif is_odd:
        results.append("O")
    elif is_square:
        results.append("S")
    else:
        results.append("EMPTY")

# Output results
for result in results:
    print(result)

import sys


def solve():
  # Read all inputs from standard input efficiently
  input_data = sys.stdin.read().split()
  if not input_data:
    return

  # The first element is the number of test cases
  t = int(input_data[0])

  # Process each test case
  for i in range(1, t + 1):
    n = int(input_data[i])
    # Based on the sample (1 -> 'shh', 10 -> 11 'h's), 
    # the output is 's' followed by n + 1 'h's.
    print("s" + "h" * (n + 1))


if __name__ == "__main__":
  solve()

def count_real_roots(a, b, c):
  """
  Calculates the number of real roots of a second-degree polynomial.

  Args:
    a: The coefficient of the x^2 term.
    b: The coefficient of the x term.
    c: The constant term.

  Returns:
    The number of real roots (0, 1, or 2).
  """

  discriminant = b**2 - 4 * a * c
  if discriminant > 0:
    return 2  # Two real roots
  elif discriminant == 0:
    return 1  # One real root (repeated)
  else:
    return 0  # No real roots

if __name__ == "__main__":
  a = int(input())
  b = int(input())
  c = int(input())
  num_roots = count_real_roots(a, b, c)
  print(num_roots)

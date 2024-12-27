def count_triple_numbers(N):
    """
    Counts the number of triple numbers less than N.

    Args:
      N: The upper limit for triple numbers.

    Returns:
      The number of triple numbers less than N.
    """
    count = 0
    for a in range(1, int(N**(1/3)) + 1):  # Iterate through possible 'a' values
        product = a * (a + 1) * (a + 2)
        if product < N:
            count += 1
        else:
            break  # No need to check further as products will increase

    return count

if __name__ == "__main__":
    N = int(input())
    num_triples = count_triple_numbers(N)
    print(num_triples)

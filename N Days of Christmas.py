def christmas_gifts(N):
    """
    Calculates the number of gifts received on the Nth day and the total gifts received.

    Args:
      N: The number of days of Christmas.

    Returns:
      A tuple containing the number of gifts received on the Nth day 
      and the total number of gifts received.
    """
    gifts_on_day = N * (N + 1) // 2  # Number of gifts on the Nth day
    total_gifts = (N * (N + 1) * (N + 2)) // 6  # Sum of the series 1 + (1+2) + (1+2+3) + ... 

    return gifts_on_day, total_gifts

if __name__ == "__main__":
    N = int(input())
    gifts_on_day, total_gifts = christmas_gifts(N)
    print(gifts_on_day)
    print(total_gifts)

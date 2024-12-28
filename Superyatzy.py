def can_get_yatsy(dice,M):
        """
    Checks if Emma can get Yatzy by cheating at most M times.

    Args:
      dice: A list of integers representing the initial values of the dice.
      M: The maximum number of dice Emma can change.

    Returns:
      "Ja" if Yatzy can be achieved, "Nej" otherwise.
    """
    counts = [dice.count(i) for i in range(1,7)]
    max_count = max(counts)
    if max_count + M >=N:
        return "Ja"
    else:
        return "Nej"
        
if __name__=="__main__":
    N,M = map(int,input().split())
    dice = [int(input()) for _ in range(N)]
    result = can_get_yatsy(dice,M)
    print(result)

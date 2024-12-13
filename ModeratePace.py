def find_median_distances(k, a, b):
    """
    Finds the median distance for each day given three runners' desired distances.

    Args:
      k: List of distances desired by the first runner.
      a: List of distances desired by the second runner.
      b: List of distances desired by the third runner.

    Returns:
      A list of median distances for each day.
    """
    n = len(k)
    median_distances = []
    for i in range(n):
        distances = [k[i], a[i], b[i]]
        distances.sort()
        median_distances.append(distances[1])  # Select the middle value
    return median_distances

if __name__ == "__main__":
    n = int(input())
    k = list(map(int, input().split()))
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    median_distances = find_median_distances(k, a, b)
    print(*median_distances)

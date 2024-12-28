import math

def max_layers(test_cases):
    results = []
    for tiles in test_cases:
        L = int((math.sqrt(tiles + 1) - 1) // 2)
        results.append(L)
    return results

# Input
N = int(input())
test_cases = [int(input()) for _ in range(N)]

# Output
results = max_layers(test_cases)
for res in results:
    print(res)

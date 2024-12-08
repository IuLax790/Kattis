def find_gold_stack(w, s):
    expected_weight = s * (s + 1) // 2 * 29260
    difference = w - expected_weight
    gold_stack = difference // 110 + 1  # Add 1 to account for 1-based indexing
    return gold_stack

if __name__ == "__main__":
    w, s = map(int, input().split())
    gold_stack = find_gold_stack(w, s)
    print(gold_stack-1)

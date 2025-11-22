import sys

def solve():
    # Read all input from stdin
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    # Create an iterator to read through the input sequentially
    iterator = iter(input_data)
    
    try:
        # 1. Read N and M (number of people in left and right queues)
        n = int(next(iterator))
        m = int(next(iterator))
        
        # 2. Calculate total time for the LEFT queue
        left_total_time = 0
        for _ in range(n):
            left_total_time += int(next(iterator))
            
        # 3. Calculate total time for the RIGHT queue
        right_total_time = 0
        for _ in range(m):
            right_total_time += int(next(iterator))
            
        # 4. Compare and Output
        if left_total_time < right_total_time:
            print("left")
        elif right_total_time < left_total_time:
            print("right")
        else:
            print("either")
            
    except StopIteration:
        # This handles cases where input might be malformed or ends unexpectedly
        return

if __name__ == "__main__":
    solve()

def hitting_the_targets():
    # Number of targets
    m = int(input())
    targets = []

    # Parse target descriptions
    for _ in range(m):
        parts = input().split()
        if parts[0] == "rectangle":
            x1, y1, x2, y2 = map(int, parts[1:])
            targets.append(("rectangle", x1, y1, x2, y2))
        elif parts[0] == "circle":
            x, y, r = map(int, parts[1:])
            targets.append(("circle", x, y, r))

    # Number of shots
    n = int(input())
    shots = []

    # Parse shots
    for _ in range(n):
        x, y = map(int, input().split())
        shots.append((x, y))

    # Process each shot
    results = []
    for sx, sy in shots:
        hit_count = 0
        for target in targets:
            if target[0] == "rectangle":
                _, x1, y1, x2, y2 = target
                if x1 <= sx <= x2 and y1 <= sy <= y2:
                    hit_count += 1
            elif target[0] == "circle":
                _, x, y, r = target
                if (sx - x) ** 2 + (sy - y) ** 2 <= r ** 2:
                    hit_count += 1
        results.append(hit_count)

    # Output results
    for result in results:
        print(result)


# Call the function
if __name__ == "__main__":
    hitting_the_targets()

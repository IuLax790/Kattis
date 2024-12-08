def find_square_corners(x, y, r):
    side_length = 2 * r
    half_side = side_length // 2

    top_left = (x - half_side, y + half_side)
    top_right = (x + half_side, y + half_side)
    bottom_right = (x + half_side, y - half_side)
    bottom_left = (x - half_side, y - half_side)

    return top_left, top_right, bottom_right, bottom_left

if __name__ == "__main__":
    x, y = map(int, input().split())
    r = int(input())

    corners = find_square_corners(x, y, r)
    for corner in corners:
        print(*corner)

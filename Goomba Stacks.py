def can_escape(n, rooms):
    current_goombas = 0

    for goombas, required in rooms:
        current_goombas += goombas
        if current_goombas < required:
            return "impossible"

    return "possible"

if __name__ == "__main__":
    n = int(input())
    rooms = []
    for _ in range(n):
        g, b = map(int, input().split())
        rooms.append((g, b))

    print(can_escape(n, rooms))

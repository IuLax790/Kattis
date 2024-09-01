def isWithinBounds(x, y):
    return 0 <= x < width and 0 <= y < height


def get(map, x, y):
    if isWithinBounds(x, y):
        return map[y][x]
    else:
        return None


size = input().split()
height = int(size[0])
width = int(size[1])
truckheight = 2
truckwidth = 2

map = []
for _ in range(height):
    row = input()
    map.append(row)
options = {}
for row in range(height):
    for column in range(width):
        numberOfCars = 0
        wasBlocked = False
        for truckY in range(truckheight):
            for truckX in range(truckwidth):
                x = column + truckX
                y = row + truckY
                entry = get(map, x, y)
                if entry == None or entry == "#":
                    wasBlocked = True
                elif entry == "X":
                    numberOfCars += 1
        if not wasBlocked:
            options[numberOfCars] = options.get(numberOfCars, 0) + 1

for numberOfCars in range(5):
    numberOfPossibilites = options.get(numberOfCars, 0)
    print(numberOfPossibilites)

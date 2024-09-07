while True:
    data = int(input())
    if data == -1:
        break

    totalDistance = 0
    previousMilesElapsed = 0
    for _ in range(data):
        dataPoint = input().split()
        speed = int(dataPoint[0])
        totalTimeElapsed = int(dataPoint[1])

        timeElapsed = totalTimeElapsed - previousMilesElapsed
        previousMilesElapsed = totalTimeElapsed
        totalDistance += speed*timeElapsed

    print("{} miles".format(totalDistance))

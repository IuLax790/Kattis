n = int(input())
pTime = None
pValue = None
totalArea = 0
for _ in range(n):
    data = input().split()
    time = int(data[0])
    value = float(data[1])
    if pTime is not None and pValue is not None:
        area = (pValue+value)/2*(time-pTime)
        totalArea +=area
    pTime = time
    pValue = value
print(totalArea/1000)

import math
cases = int(input())
for i in range(cases):
    data = input().split()
    b = int(data[0])
    p = float(data[1])
    bpm = 60*b/p
    difference = 60/p
    lowerBPM = bpm - difference
    upperBPM = bpm + difference
    print("{} {} {}".format(
    round(lowerBPM,4),
          round(bpm,4),
          round(upperBPM,4)
    ))

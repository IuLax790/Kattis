import math
inp = input().split()
h,v = int(inp[0]),int(inp[1])
radiants = math.radians(v)
ladderLength = math.ceil(h/math.sin(radiants))
print(ladderLength)

import math
a,b = input().split()
a = int(a);b=int(b)
if a*math.sqrt(2)<=2*b:
    print("fits")
else:
    print("nope")

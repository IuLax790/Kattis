l = []
s = int(input())
l.append(s)
while s>-1:
    s = int(input())
    l.append(s)
else:
    print(max(l))

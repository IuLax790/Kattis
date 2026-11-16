l = []
a,b = input().split()
a = int(a);b=int(b)
for i in range(b):
    i = int(input())
    l.append(i)
if (sum(l)%a)==0:
    print(1)
else:
    print(0)

inp = input().split()
count = 0
n,k = int(inp[0]),int(inp[1])
for i in range(n):
    i = input().split()
    s = set(i)
    if len(i)>len(s):
        count +=(len(i)-len(s))

print(count)
